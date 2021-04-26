# import threading
# import queue
# import re
# import urllib.request
#
# # Number of threads
# n_thread = 10
# # Create queue
# queue = queue.Queue()
#
#
# class ThreadClass(threading.Thread):
#     def __init__(self, queue):
#         threading.Thread.__init__(self)
#         super(ThreadClass, self).__init__()
#
#         # Assign thread working with queue
#         self.queue = queue
#
#
# def run(self):
#     while True:
#         # Get from queue job
#         host = self.queue.get()
#         print(self.getName() + ":" + host)
#         try:
#             # print("当前代理IP " + host)
#             proxy = urllib.request.ProxyHandler({"http": host})
#             opener = urllib.request.build_opener(proxy, urllib.request.HTTPHandler)
#             urllib.request.install_opener(opener)
#             url = "http://www.baidu.com"
#             data = urllib.request.urlopen(url).read().decode('utf-8', 'ignore')
#             print("通过")
#
#             print("-----------------------------")
#         except Exception as err:
#             print(err)
#             print("-----------------------------")
#
#         # signals to queue job is done
#         self.queue.task_done()
#
#
# # Create number process
# for i in range(n_thread):
#     t = ThreadClass(queue)
#     t.setDaemon(True)
#     # Start thread
#     t.start()
#
# # Read file line by line
# hostfile = open("thebigproxylist-17-12-20.txt", "r")
# for line in hostfile:
#     # Put line to queue
#     queue.put(line)
# # wait on the queue until everything has been processed
# queue.join()
