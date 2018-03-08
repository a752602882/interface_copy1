#coding:utf-8
from sys import getrefcount

#引用计数
a1 = 100000
a2 = 100000

s1 =("aaa","sss","sss")
s2 =("aaa","sss","sss")
#print id(a1)
#print id(a2)

print id(s1)
print id(s2)

#print  a1 is a2

print  s1 is s2
#print  getrefcount(a1)
print  getrefcount(s1)