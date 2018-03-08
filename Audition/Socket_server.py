#coding:utf-8

#服务器


import  socket


s = socket.socket()
s.bind(("127.0.0.1",5555))

#等待客户端连接
s.listen(5)

while True:
    c,addr = s.accept()
    print '连接地址',addr
    c.send('welecome')
    #关闭连接
    c.close()

'''
   服务端：
    打开套接字  socket.socket()
    绑定        s.bind
    等待监听    s.listemn()
    
   where循环       
    接收               a=s.accept   
    发生消息给客户端   a=.send("ssss")
    关闭               a.close
    
    --------------------------------------
    客户端：
     打开套接字   s=socket.socket()
     连接地址     s.connect("127.0.0.1",5555)
     接收消息     s.revc()  
     关闭        s.close
'''