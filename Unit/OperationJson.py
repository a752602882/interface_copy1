#coding=utf-8
import json

class OperationJson:

    def  __init__(self,file_path=None):
        if file_path  == None:
            self.file_path = '../DataConfig/user.json'
        else:
            self.file_path = file_path
        self.data = self.read_data()

    #读取json文件
    def read_data(self):
        with open(self.file_path) as fp:
            data = json.load(fp)
        return  data

    #读取json中的详细数据
    def get_data(self,id):
        return  self.data[id]


    def write_data(self,data):
        with open("../DataConfig/cookie.json","w") as fp:
            fp.write(json.dumps(data))

