import subprocess
from threading import Timer
rs = subprocess.Popen('ls -l', True)
rs.wait()
print('')

# class test(object):
#     def __init__(self):
#         self.stdout = []
#         self.stderr = []
#         self.timeout = 6
#         self.is_timeout = False
#         pass
#
#     def timeout_callback(self, p):
#         print ('exe time out call back')
#         try:
#             p.kill()
#             # os.killpg(p.pid, signal.SIGKILL)
#         except Exception as error:
#             print (error)
#
#     def run(self,cmd):
#         stdout = open('/tmp/subprocess_stdout', 'wb')
#         stderr = open('/tmp/subprocess_stderr', 'wb')
#
#         p = subprocess.Popen(cmd, stdout=stdout.fileno(), stderr=stderr.fileno())
#         my_timer = Timer(self.timeout, self.timeout_callback, [p])
#         my_timer.start()
#         print (p.pid)
#         try:
#             print ("start to count timeout; timeout set to be %d \n" % (self.timeout,))
#             p.wait()
#         finally:
#             my_timer.cancel()
#             stdout.flush()
#             stderr.flush()
#             stdout.close()
#             stderr.close()
#
# if __name__ == '__main__':
#     s = test()
#     cmd = ['bash', 'ping www.baidu.com']
#     s.run(cmd)