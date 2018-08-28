import sys
import time
import logging
import random
import threading
from threading import Thread

# def cuntdown(n): # 启动一个线程
#     while n:
#         print("倒数开始:",n)
#         time.sleep(1)
#         n -= 1
#
# def countdown2(n, threadnumber): # 启动多个线程
#     while n:
#         print("第 %s 个线程,倒数开始: %s"%(threadnumber, n))
#         time.sleep(1)
#         n -= 1
#
# def cuntdown3(n, threadnumber): # 获取线程的名字
#     while n:
#         print("第 %s 个线程的名字: %s, 倒数开始: %s"%(threadnumber, threading.current_thread().name, n))
#         n -= 1
#         time.sleep(1)
#
# logging.basicConfig(
#     level=logging.DEBUG,
#     format="%(threadName)-10s: %(message)s"
# )
#
# def countdown4(n):
#     while n:
#         logging.debug("倒数开始:%s"%n)
#         time.sleep(n)
#         n -= 1
#
# class MyThread(Thread):
#
#     def __init__(self, name, count):
#         Thread.__init__(self)
#         self.name = name
#         self.count = count
#
#     def run(self):
#         try:
#             lock.acquire()
#             logging.debug("lock...")
#             countdown3(self.count)
#         finally:
#             lock.release()
#             logging.debug('open again')
#
# lock = threading.Lock()
# TOTAL = 0
#
# def add_plus():
#     global TOTAL
#     with lock:    # 锁的新方法，使用之后可以自动关闭
#         logging.debug("before add: %s"%(TOTAL))
#         wait = random.randint(1,3)
#         time.sleep(wait)
#         print("执行了 %ss 之后"%wait)
#         TOTAL += 1
#         logging.debug("after add: %s"%TOTAL)
#
# def main():
#
#     thread_list = []
#     logging.debug("start...")
#     for i in range(10):
#         t = Thread(target=cuntdown3, args=(5, i+1))
#         t.start()
#         thread_list.append(t)
#
#     for t in thread_list:
#         t.join()
#     logging.debug("end...")
#
# if __name__ == '__main__':
#     main()

# exitFlag = 0
# threads = []
# threadLock = threading.Lock()
#
# class MyThread(threading.Thread):
#     def __init__(self, threadID, name, counter):
#         threading.Thread.__init__(self)
#         self.threadID = threadID
#         self.name = name
#         self.counter = counter
#         print("**************")
#         print("self.getName:"+self.getName())
#         print("self.setName:",self.setName(self.getName().upper()))
#         print("self.getName:" + self.getName())
#         print("current threading is alive:",self.isAlive())
#         print("**************")
#
#     def print_time(self, name, counter, delay):
#         while counter:
#             if exitFlag:
#                 sys.exit()
#             print("%s %s"%(name, time.ctime(time.time())))
#             time.sleep(delay)
#             counter -= 1
#             # exitFlag += 1
#
#     def run(self):
#         threadLock.acquire()
#         self.print_time(self.name, self.counter, 2)
#         threadLock.release()
#
# thread1 = MyThread(1, "thread-1", 2)
# thread2 = MyThread(2, "thread-2", 2)
#
# thread1.start()
# thread2.start()
#
# threads.append(thread1)
# threads.append(thread2)
#
# for t in threads:
#     t.join()

logging.basicConfig(
    level=logging.DEBUG,
    format=("%(threadName)-5s: %(message)s")
)

TOTAL = 0
exitFlag = 0
threads = []

class MyThread(Thread):
    def __init__(self, name, count):
        Thread.__init__(self)
        self.name = name
        self.count = count

    def run(self):
        try:
            lock.acquire()
            self.print_time(self.name, self.count)
        finally:
            lock.release()
            logging.debug("END")

    def add1(self):
        global TOTAL
        with lock:
            TOTAL += 1
            logging.debug("ADD1 TOTAL: %s" % TOTAL)

    def add2(self):
        global TOTAL
        with lock:
            TOTAL += 1
            logging.debug("ADD2 TOTAL: %s" % TOTAL)
            self.add1()
            return TOTAL

    def print_time(self, name, count):
        global exitFlag
        while count:
            if exitFlag:
                sys.exit()
            logging.debug("%s %s %s" % (name, self.getName(), time.ctime(time.time())))
            count -= 1
            if self.add2()<20:
                wait = random.randint(1, 3)
                logging.debug("Delay %ss" % wait)
                time.sleep(wait)
            # else:
            #     exitFlag += 1

lock = threading.RLock()

def main():
    for i in range(10):
        thread = MyThread("thread-%s" % (i+1), i+1)
        thread.start()
        threads.append(thread)
    for t in threads:
        t.join()

if __name__ == '__main__':
    main()
