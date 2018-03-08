#coding:utf-8



'''
  index (1,2,3,4,5)
  sub(1,2,3,4)
-----------------------
  index (1,2,3,4,)
  sub(1,2,3)
----------------------
  index (1,2,3)
  sub(1,2,)
-----------------------
  index (1,2)
  sub(1)
----------------------
  index (1)
  sub(0)
'''

def bubble_sort(l_list):

    count = len(l_list)-1;
    print count

    for index in range(count,0,-1):
       #index永远不会等于 0
       for sub  in range(index):

          if l_list[sub]>l_list[sub+1]:

              l_list[sub] ,l_list[sub+1] =l_list[sub+1],l_list[sub]

    return l_list



alist =[123,23,54,32,777,2]
bubble_sort(alist)

print alist