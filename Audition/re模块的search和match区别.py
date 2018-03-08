#coding:utf-8
import re

test_string = "helloworld mhellworld "
s1="hello"
s2="world"

#search查找的是整个字符串
print(re.search(s2,test_string))
print(re.search(s2,test_string).group())

#match查找的是字符串开头
print(re.match(s2,test_string))
print(re.match(s2,test_string).group())