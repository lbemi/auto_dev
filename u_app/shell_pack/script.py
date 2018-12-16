import os

def update(hostname, id):

    if hostname == 'test2.13':
        if id == '1':
            os.system('pwd')
            result = "正在执行脚本1，请稍后....."
        elif id == '2':
            os.system('ls -l')
            result = "正在执行脚本2，请稍后....."
    elif hostname == 'test2.2':
        if id == '1':
            os.system('who')
            result = "正在执行脚本1，请稍后....."
        elif id == '2':
            os.system('id')
            result = "正在执行脚本2，请稍后....."
    else:
        result = "功能正在调试中....."
    return result