#coding:utf-8
from Logic.DependData import DependData
from Logic.GetData import GetData
from Logic.RunMethod import RunMethod
from Unit.OperationHeader import OperationHeader
from Unit.CommonUnit import CommonUnit
from Unit.OperationJson import OperationJson


class RunTest:
    def __init__(self):
        self.runMethod = RunMethod()
        self.data = GetData()
        self.comm = CommonUnit()


    def go_to_run(self):
       pass_count = []
       fail_count = []
       row_count = self.data.get_case_size()
       for i in range(1,row_count):
           is_run  = self.data.get_is_run(i)
           if is_run:
               url = self.data.get_url(i)
               method = self.data.get_request_way(i)
               request_data  = self.data.get_data_for_json(i)
               expect = self.data.get_expect(i)
               header = self.data.get_header(i)
               depend_case = self.data.get_case_depend(i)
               if depend_case!=None:
                   self.depend_response_data = DependData(depend_case)
                   #获取的依赖响应数据
                   depend_response_data=self.depend_response_data.get_data_for_key(i)
                   #field依赖
                   field_depend = self.data.get_field_depend(i)
                   request_data[field_depend] = depend_response_data

               if header == 'write':
                   res = self.runMethod.run_main(method,url,request_data)
                   op_header = OperationHeader(res)
                   op_header.write_cookie()
               elif header=='yes':
                   op_json =OperationJson('../DataConfig/cookie.json')
                   cookie = op_json.get_data('apsid')
                   cookies = {
                       'apsid':cookie
                   }
                   res= self.runMethod.run_main(method,url,request_data,cookies)
               else:
                   res = self.runMethod.run_main(method,url,request_data)

               print res
               if self.comm.is_equal_dict(expect,res):
                   self.data.write_result(i,"pass")
                   pass_count.append(i)
               else:
                   self.data.write_result(i,'fail')
                   pass_count.append(i)
               #self.send_mai.send_mainsend_main(pass_count,fail_count)









if __name__ == '__main__':
    run = RunTest()
    run.go_to_run()

