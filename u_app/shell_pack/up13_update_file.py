#! /usr/bin/python3

import paramiko
import os
import sys
import datetime
import time

hostname = '192.168.2.13'
# hostname = '192.168.7.98'
port = 22
user = 'root'
password = '1'
local_dir = '/home/apps/2.13/update'
# local_dir = '/home/wjl/gx/2.13/update'
mzservice_dir = '/www/servers/mzservice'
mzapi_dir = '/www/servers/mzapi'
mzbiz_dir = '/www/servers'

def remote_file_if(ssh, remote_dir, remote_dir_file):
    cmd = 'ls -d ' + remote_dir + '/' + remote_dir_file
    stdin, stdout, stderr = ssh.exec_command(cmd)
    result = stderr.read()
    # print(len(result))
    # if (len(result) == 0):
        # print(result)
    bak_cmd = 'mv ' + remote_dir + '/' + remote_dir_file + ' /www/back/' + remote_dir_file + '_bak_`date +%Y%m%d_%H%M%S`'
    print('备份文件:' + remote_dir_file + ' ---> /www/back 目录下')
    stdin, stdout, stderr = ssh.exec_command(bak_cmd)
        # ssh.close()


def upload(dockername):
    try:
        files = os.listdir(local_dir)
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(hostname=hostname, port=port, username=user, password=password)
        if dockername == 'mzapi':
            filename = 'mzapi'
            remote_dir = mzapi_dir
        elif dockername == 'mzservice':
            filename = 'mz-service'
            remote_dir = mzservice_dir
        elif dockername =='mzbiz':
            filename = 'mzbiz'
            remote_dir = mzbiz_dir
        else:
            sys.exit(1)

        for f in files:
            # print('---'+ra)
            if filename in f:
                ra = remote_dir + '/' + f
                print('-' * 80)
                print('Begin to upload file  to %s ' % hostname)
                start = datetime.datetime.now()
                print(start)
                remote_file_if(ssh, remote_dir, f)
                print('上传文件： ' + f + '--->' + remote_dir)
                t = paramiko.Transport((hostname, port))
                t.connect(username=user, password=password)
                sftp = paramiko.SFTPClient.from_transport(t)
                sftp.put(os.path.join(local_dir, f), ra)
                if f == 'mzbiz-web.zip':
                    print('---------biz------')
                    ssh.exec_command("cd /www/servers && unzip -o mzbiz-web.zip")
                    ssh.exec_command('mv /www/servers/mzbiz-web /www/servers/mzbiz')
                t.close()
                print('共耗时：' + str(datetime.datetime.now() - start))
                exec_restart_docker(ssh, dockername)
                # log_print(ssh, dockername)
        ssh.close()
        print('-' * 80)
    except Exception as e:
        print("Error: " + str(e))


def exec_restart_docker(ssh, dockername):
    try:
        ssh.exec_command('docker restart ' + dockername)
        # std_in, std_out, std_err = ssh.exec_command('tail -f /data/logs/'+dockername+'/debug.log')
        # while True:
        #     print(std_out.readline())
    except Exception as e:
        print('Error + exec_restart_docker : ' + str(e))


def log_print(ssh, dockername):
    try:
        std_in, std_out, std_err = ssh.exec_command('tail -f /data/logs/' + dockername + '/debug.log')
        while True:
            print(std_out.readline())
    except Exception as e:
        print('Error + log_print  :' + str(e))
    except KeyboardInterrupt:
        pass


def update_mzbiz():
    dockername = 'mzbiz'
    upload(dockername)

def update_mzservice():
    dockername = 'mzservice'
    upload(dockername)
    time.sleep(5)

def update_mzapi():
    dockername = 'mzapi'
    upload(dockername)
    time.sleep(5)

