from django.contrib import admin
from u_app.models import hostinfo

class Hostinfo(admin.ModelAdmin):
    list_display = ['hostname','IP','Port','Host_user','Work_dir','Out_port']

admin.site.site_header = '运维管理后台'
admin.site.site_header = '运维管理后台'
admin.site.register(hostinfo, Hostinfo)