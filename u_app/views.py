from django.shortcuts import render, render_to_response
from u_app.forms import UserForm,RegisterForm,AlterForm,hostadimnForm,monitorForm,autoArrMinionForm
from django.contrib import auth
from .models import hostinfo
from django.http import HttpResponse, HttpResponseRedirect
import json
from django.core.paginator import Paginator
from django.contrib.auth.models import User
from django.db.models import Count,Sum
import time
from django.contrib.auth.decorators import login_required

# Create your views here.

def login(req):
    nowtime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    if req.method == 'GET':
        uf = UserForm()
        return render(req, 'login.html', {'uf': uf, 'nowtime': nowtime})
    else:
        uf = UserForm(req.POST)
        if uf.is_valid():
            username = req.POST.get('username', '')
            password = req.POST.get('password', '')
            user = auth.authenticate(username=username, password=password)
            if user is not None and user.is_active:
                auth.login(req, user)
                return render(req, 'index.html')
            else:
                return render(req, 'login.html', {'uf': uf, 'nowtime': nowtime, 'password_is_wrong': True})
        else:
            return render(req, 'login.html', {'uf': uf, 'nowtime': nowtime})
    return render(request, 'login.html')
@login_required
def index(req):
    return render(req, 'index.html')
@login_required
def logout(req):

    auth.logout(req)
    return HttpResponseRedirect('login.html')
@login_required
def serverList(request, id=0):
    if id != 0:
        hostinfo.objects.filter(id = id).delete()

    if request.method == 'POST':
        all_list = hostinfo.objects.all()
        pageSize = request.POST.get('pageSize')  # how manufactoryy items per page
        pageNumber = request.POST.get('pageNumber')
        offset = request.POST.get('offset')  # how many items in total in the DB
        search = request.POST.get('search')
        sort_column = request.POST.get('sort')  # which column need to sort
        order = request.POST.get('order')
        if search:  # 判断是否有搜索字
            all_records = hostinfo.objects.filter(id=search, asset_type=search, business_unit=search, idc=search)
        else:
            all_records = hostinfo.objects.all()  # must be wirte the line code here

        if sort_column:  # 判断是否有排序需求
            sort_column = sort_column.replace('asset_', '')
            if sort_column in ['id', 'asset_type', 'sn', 'name', 'management_ip', 'manufactory',
                               'type']:  # 如果排序的列表在这些内容里面
                if order == 'desc':  # 如果排序是反向
                    sort_column = '-%s' % (sort_column)
                all_records = hostinfo.objects.all().order_by(sort_column)
            elif sort_column in ['salt_minion_id', 'os_release', ]:
                # server__ 表示asset下的外键关联的表server下面的os_release或者其他的字段进行排序
                sort_column = "server__%s" % (sort_column)
                if order == 'desc':
                    sort_column = '-%s' % (sort_column)
                all_records = hostinfo.objects.all().order_by(sort_column)
            elif sort_column in ['cpu_model', 'cpu_count', 'cpu_core_count']:
                sort_column = "cpu__%s" % (sort_column)
                if order == 'desc':
                    sort_column = '-%s' % (sort_column)
                all_records = hostinfo.objects.all().order_by(sort_column)
            elif sort_column in ['rams_size', ]:
                if order == 'desc':
                    sort_column = '-rams_size'
                else:
                    sort_column = 'rams_size'
                all_records = hostinfo.objects.all().annotate(rams_size=Sum('ram__capacity')).order_by(sort_column)
            elif sort_column in [
                'localdisks_size', ]:  # using variable of localdisks_size because there have a annotation below of this line
                if order == "desc":
                    sort_column = '-localdisks_size'
                else:
                    sort_column = 'localdisks_size'
                # annotate 是注释的功能,localdisks_size前端传过来的是这个值，后端也必须这样写，Sum方法是django里面的，不是小写的sum方法，
                # 两者的区别需要注意，Sum（'disk__capacity‘）表示对disk表下面的capacity进行加法计算，返回一个总值.
                all_records = hostinfo.objects.all().annotate(localdisks_size=Sum('disk__capacity')).order_by(
                    sort_column)

            elif sort_column in ['idc', ]:
                sort_column = "idc__%s" % (sort_column)
                if order == 'desc':
                    sort_column = '-%s' % (sort_column)
                all_records = hostinfo.objects.all().order_by(sort_column)

            elif sort_column in ['trade_date', 'create_date']:
                if order == 'desc':
                    sort_column = '-%s' % sort_column
                all_records = User.objects.all().order_by(sort_column)

        if not offset:
            offset = 0
        if not pageSize:
            pageSize = 10
        response_data = {'total':all_list.count(),'rows': []}
        pageinator = Paginator(all_list, pageSize)
        page = int(int(offset) / int(pageSize) + 1)
        for server_li in pageinator.page(page):
            response_data['rows'].append({
                "id": server_li.id if server_li.id else "",
                "hostname": server_li.hostname if server_li.hostname else "",
                "IP": server_li.IP if server_li.IP else "",
                "Port": server_li.Port if server_li.Port else "",
                "Host_user": server_li.Host_user if server_li.Host_user else "",
            })
        return HttpResponse(json.dumps(response_data))
    return render(request, 'serverlist.html')




