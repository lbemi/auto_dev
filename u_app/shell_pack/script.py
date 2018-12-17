import os
import time
from u_app.shell_pack import up13_update_file
def update(hostname, id):
    result = "功能正在调试中....."
    if hostname == 'test2.13':
        if id == '1':
            os.system('pwd')
            up13_update_file.update_mzservice()
            up13_update_file.update_mzapi()
            time.sleep(5)
            result = "mz-serverice和mzapi更新完成！！！！"
        elif id == '2':
            up13_update_file.update_mzbiz()
            result = "mzbiz更新完成！！！！"
    elif hostname == 'test2.2':
        if id == '1':
            os.system('who')
            result = "正在执行脚本1，请稍后....."
        elif id == '2':
            os.system('id')
            time.sleep(5)
            result = "正在执行脚本2，请稍后....."
    elif hostname == 'test98':
        if id == '1':
            # up13_update_file.update_mzservice()
            # up13_update_file.update_mzapi()
            result = "正在执行更新脚本，请稍后....."
        elif id == '2':
            os.system('ls -l')
            result = "功能正在调试中....."
    else:
        result = "功能正在调试中....."

    return result