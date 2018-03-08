
# coding:utf-8
import re

line ="i am a super man!"

print(line.split(" "))
print(re.split(" ",line))
#以空格和m 来分割
print (re.split("[ m]",line))
