#coding:utf-8

#服务器


import  socket


s = socket.socket()
s.connect(("127.0.0.1",5555))
print s.recv(1025)
s.close()

