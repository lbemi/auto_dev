from django.db import models

# Create your models here.


class hostinfo(models.Model):
    hostname = models.CharField(u'主机名',max_length=255)
    IP = models.CharField(u'IP地址',max_length=50)
    Port = models.IntegerField(u'端口')
    Host_user = models.CharField(u'用户名',max_length=255)
    Password = models.CharField(u'密码', max_length=50)
    Work_dir = models.CharField(u'工作目录', max_length=255)
    Out_port = models.CharField(u'对外开放端口', max_length=255)


    def __str__(self):
        return self.hostname