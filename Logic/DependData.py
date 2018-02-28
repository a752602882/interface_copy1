#coding=utf-8
import json

from  Unit.OperationExecl import OperationExecl
from  Logic.GetData import GetData
from RunMethod import RunMethod
from jsonpath_rw import jsonpath,parse
class DependData:

    def __init__(self,case_id):
        self.case_id = case_id
        self.opera_execl = OperationExecl()
        self.data = GetData()

    def run_depend(self):
       run_method = RunMethod()

       #获取依赖行的行号，获得该行的值
       row_num = self.opera_execl.get_row_num(self.case_id)

       #header = self.data.is_header(row_num)
       request_data = self.data.get_data_for_json(row_num)
       method = self.data.get_request_way(row_num)
       url = self.data.get_url(row_num)
       res = run_method.run_main(method,url,request_data)
       print '>>>>>>>>>>>>>>>>>>>>>>>>>'
       print type(res)
       print res
       return res


    #返回的是依赖行的数据
    def get_case_line_data(self):
       row_data = self.opera_execl.get_row_data(self.case_id)
       return row_data


    def get_data_for_key(self,row):
        key_depend = self.data.get_key_depend(row)

        response_data =self.run_depend()
        json_exe = parse(key_depend)

        print type(key_depend)
        print type(response_data)
        print response_data
        madle = json_exe.find(response_data)
        return [math.value for math in madle][0]


if __name__ == '__main__':
        order = {
            "data": {
                "_input_charset": "utf-8",
                "body": "慕课网订单-1710141907182334",
                "it_b_pay": "1d",
                "notify_url": "http://order.imooc.com/pay/notifyalipay",
                "out_trade_no": "1710141907182334",
                "partner": "2088002966755334",
                "payment_type": "1",
                "seller_id": "yangyan01@tcl.com",
                "service": "mobile.securitypay.pay",
                "sign": "kZBV53KuiUf5HIrVLBCcBpWDg%2FnzO%2BtyEnBqgVYwwBtDU66Xk8VQUTbVOqDjrNymCupkVhlI%2BkFZq1jOr8C554KsZ7Gk7orC9dDbQlpr%2BaMmdjO30JBgjqjj4mmM%2Flphy9Xwr0Xrv46uSkDKdlQqLDdGAOP7YwOM2dSLyUQX%2Bo4%3D",
                "sign_type": "RSA",
                "string": "_input_charset=utf-8&body=慕课网订单-1710141907182334&it_b_pay=1d&notify_url=http://order.imooc.com/pay/notifyalipay&out_trade_no=1710141907182334&partner=2088002966755334&payment_type=1&seller_id=yangyan01@tcl.com&service=mobile.securitypay.pay&subject=慕课网订单-1710141907182334&total_fee=299&sign=kZBV53KuiUf5HIrVLBCcBpWDg%2FnzO%2BtyEnBqgVYwwBtDU66Xk8VQUTbVOqDjrNymCupkVhlI%2BkFZq1jOr8C554KsZ7Gk7orC9dDbQlpr%2BaMmdjO30JBgjqjj4mmM%2Flphy9Xwr0Xrv46uSkDKdlQqLDdGAOP7YwOM2dSLyUQX%2Bo4%3D&sign_type=RSA",
                "subject": "慕课网订单-1710141907182334",
                "total_fee": 299
            },
            "errorCode": 1000,
            "errorDesc": "成功",
            "status": 1,
            "timestamp": 1507979239100
        }

        res = "data.out_trade_no"
        json_exe = parse(res)
        print '>>>>>>>>>>>>>>>>>>>>>>>>'
        print type(order)
        print order
        print type(res)
        madle = json_exe.find(order)
        print [math.value for math in madle][0]
