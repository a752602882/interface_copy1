#coding:utf-8

#进程

from multiprocessing import Process
import threading

def foo(i):
    print("this is process:",i)

def foo1(i):
    print ("this is thread:",i)

if __name__ == '__main__':
    for i in range(5):

        #线程
        p = Process(target=foo,args=(i,))
        p.start()
        #进程
        t= threading.Thread(target=foo1,args=(i,))
        t.start()
        #携程
