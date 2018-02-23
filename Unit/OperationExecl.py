#coding=utf-8
import xlrd
from xlutils.copy import copy

class OperationExecl:


    def __init__(self,file_name= None,sheet_id=None):
        if file_name:
            self.file_name =file_name
            self.sheet_id = sheet_id
        else:
            self.file_name = '../dataConfig/case.xlsx'
            self.sheet_id = 0
        self.data = self.get_data()

    #获得sheet表内容
    def get_data(self):
        data = xlrd.open_workbook(self.file_name)
        table = data.sheet()[self.sheet_id]
        return table

    #获取单元格格数
    def get_rows(self):
        return self.data.nrows


    #读取某一个单元格内容
    def get_cell_value(self,row,col):
       return self.data.cell_value(row,col)


    #为某一单元格写入内容
    def write_value(self,row,col,value):
        read_data = xlrd.open_workbook(self.file_name)
        write_data =copy(read_data)
        sheet_data = write_data.getsheet(0)
        sheet_data.write(row,col,value)
        write_data.save(self.file_name)


    #根据对应的caseid找到对应行的内容 (默认时候是从第一列找出包含列的行号)
    def get_row_data(self,case_id):
        row_num = self.get_row_num(case_id)
        return self.get_row_data(row_num)


    #根据caseid找到对应的行号
    def get_row_num(self,case_id):
        num =1
        cols_data = self.get_col_data()
        for col_data in cols_data:
            if case_id in col_data:
                return  num
            num=num+1

    #获取某一列的值
    def get_col_data(self,col_id=None):
        cols_vlaue=None
        if col_id!= None:
          cols_vlaue = self.data.col_values(col_id)
        else:
          cols_vlaue = self.data.col_values(0)
        return cols_vlaue

    #根据行号找到对应行的值
    def get_row_value(self,num):
       return self.data.row_values(num)


