#coding=utf-8
import json


class CommonUnit:
    def is_contain(self,str_one,str_two):
        str_one = str_one.encode('unicode-escape').decode('string-escape')
        if str_one in str_two:
            flag =True
        else:
            flag =False
        return flag

    def is_equal_dict(self,dict_one,dict_two):
        '''
		判断两个字典是否相等
		'''
        if isinstance(dict_one,str):
            dict_one = json.loads(dict_one)
        if isinstance(dict_two,str):
            dict_two = json.loads(dict_two)
        return cmp(dict_one,dict_two)