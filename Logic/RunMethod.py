
import requests
class RunMethod:

    def run_main(self,method,url,data,header=None):
       res =None
       if method =='Post':
           res = self.post_main(url,data,header)
       else:
           res = self.get_main(url,data,header)
       return res.json()


    def get_main(self,url,data,header):
        res = None
        if header != None:
            res = requests.get(url=url,data = data,header = header)
        else:
            res = requests.get(url=url,data = data)
        return res

    def post_main(self,url,data,header):
        res = None
        if header != None:
            res = requests.post(url=url,data = data,header = header)
        else:
            res = requests.post(url=url,data = data)
        return res
