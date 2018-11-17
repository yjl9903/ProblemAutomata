#coding=utf-8

import os
import time
from threading import Thread

def setTimeLimit(maxTime):
    def wrapper(func):
        def _wrapper(*args, **kw):
            flag = 0
            class LimitTime(Thread):
                def __init__(self):
                    Thread.__init__(self)
                def run(self):
                    func(*args, **kw)
                def stop(self):
                    if self.is_alive():
                        Thread._Thread__stop(self)
                        # raise Exception("Time Limit Exceeded")
            t = LimitTime()
            start = time.time()
            t.start()
            t.join(timeout = maxTime)
            end = time.time()
            last = 1000 * (end - start)

            if t.is_alive():
                t.stop()
                last = "Time Limit Exceeded"
                # raise Exception("Time Limit Exceeded")

            # print(last)
            return last

        return _wrapper
    return wrapper

# if __name__ == "main":

# @setTimeLimit(1.99)
# def f():
#     time.sleep(3)
#     print("ok")

# ti = f()
# print ti