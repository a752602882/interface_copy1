#coding:utf-8
class Data_Config:

      id=0
      name=1
      url = 2
      is_run = 3
      request_way = 4
      header = 5
      case_depend = 6
      data_depend = 7
      field_depend = 8
      data =9
      expect=10
      result= 11

def get_id():
    return Data_Config.id

def get_url():
    return Data_Config.url

def get_run():
    return Data_Config.is_run

def get_run_way():
    return Data_Config.request_way

def get_header():
    return Data_Config.header

def get_case_depend():
    return Data_Config.case_depend

def get_data_depend():
    return Data_Config.data_depend

def get_field_depend():
    return Data_Config.field_depend

def get_data():
    return Data_Config.data

def get_expect():
    return Data_Config.expect

def get_result():
    return Data_Config.result
