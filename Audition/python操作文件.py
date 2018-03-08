#coding:utf-8



fp=open("./test.txt","wt");
fp.write("你好，傻子")
fp.close()


with open("./test.txt","at") as fp:
    fp.write("aaaaa")

with open("./test.txt","rt") as fp:
    print fp.read()