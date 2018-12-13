from django.contrib import admin


# # Register your models here.
# class MyAdminSite(admin.AdminSite):
#     site_header = '管理系统'  # 此处设置页面显示标题
#     site_title = '运维'  # 此处设置页面头部标题
#
#
# admin_site = MyAdminSite(name='management')
# admin_site.register(MyAdminSite)
admin.site.site_header = '运维管理后台'
admin.site.site_header = '运维管理后台'