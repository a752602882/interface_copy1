#coding:utf-8

test_list={'key1':1,"key2":2,"key3":3}
print type(test_list)


l= test_list.items()
print l
#print next(l)

itor= test_list.iteritems()
print  next(itor)
print  next(itor)
print  next(itor)