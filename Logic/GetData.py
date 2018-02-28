#coding:utf-8
from  Unit.OperationExecl import OperationExecl
from  Modle import Data_Config
from Unit.OperationJson import OperationJson


class GetData:
    def __init__(self):
        self.oper_execl = OperationExecl()


    def get_case_size(self):
        return self.oper_execl.get_rows()

    def get_url(self,row):
        col = Data_Config.get_url()
        return self.oper_execl.get_cell_value(row,col)

    def get_is_run(self,row):
       flag =None
       col = Data_Config.get_is_run()
       is_run =  self.oper_execl.get_cell_value(row,col)
       if is_run=='yes':
           flag =  True
       else:
           flag = False
       return flag

    def get_request_way(self,row):

        col = Data_Config.get_request_way()
        request_way =  self.oper_execl.get_cell_value(row,col)
        return request_way

    def get_header(self,row):
        col = Data_Config.get_header()
        header =  self.oper_execl.get_cell_value(row,col)
        if header=='':
            header=None
        return header

    def get_case_depend(self,row):
        col = Data_Config.get_case_depend()
        case_depend = self.oper_execl.get_cell_value(row,col)
        if case_depend =='':
            return None
        else:
            return case_depend


    def get_key_depend(self,row):
        col =Data_Config.get_key_depend()
        depend_key =self.oper_execl.get_cell_value(row,col)
        if depend_key=='':
            return None
        else:
            return depend_key


    def get_field_depend(self,row):
        col = Data_Config.get_case_depend()
        field = self.oper_execl.get_cell_value(row,col)
        if field =='':
            return  None
        else:
            return  field

    def get_data_for_json(self,row):
        request_json=None
        oper_json = OperationJson()
        data=self.get_data(row)
        if data!=None:
          request_json = oper_json.get_data(data)
        return  request_json

    #返回的是data
    def get_data(self,row):
        col= Data_Config.get_data()
        data = self.oper_execl.get_cell_value(row,col)
        if data =='':
           return None
        return  data


    def get_expect(self,row):
      col= Data_Config.get_expect()
      expect = self.oper_execl.get_cell_value(row,col)
      return expect

    def write_result(self,row,value):
      col =Data_Config.get_result()
      self.oper_execl.write_value(row,col,value)
