
#coding:utf-8
'''
 *args是一个可变的参数
 *kvarg是一个可变的键值对
'''

def  test_args(frist,*args):
 print frist
 for v in args:
     print "args ", v


def test_kwarg(frist,*args,**kwargs):
    print frist
    for v in args:
        print "args",v

    for k,v in kwargs.items():
        print "kwargs",(k,v)




test_args(1,2,3,4,5,6)
print "--------------------"
test_args(1,2,3,4)
print "--------------------"

test_kwarg(1,2,3,4,k0=3,k1=4,k2=5)
