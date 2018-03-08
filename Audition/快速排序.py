#coding:utf-8

def fast_sort(l_list,left,right):

     if left >= right:
      return l_list

    #定义游标
     low= left
     high = right

    #取一个参考标志，最左边的元素
     key = l_list[low]
     while low<high:
        #从右侧向左移动，如果右侧的大于key值，继续移动，如果小于，就停下
         while low<high and l_list[high]>=key:
                high-=1

        #从最左侧向右，依次和标志元素对比，如果左侧的元素小于标志元素
         while low < high and l_list[low] <= key:
                #左侧加1
                low += 1

       #此时的情况有两种：low=high,还有就是分别找到比左侧基准值大和小的是
         if (low!=high):
                l_list[low],l_list[high]  = l_list[high],l_list[low]

     if(low ==high):
      #定位基准值
      l_list[high]=key
           #处理左侧元素

      fast_sort(l_list, left, low - 1)
      #处理右侧元素
      fast_sort(l_list, low + 1, right)
      return l_list

alist = [0, 10, 88, 19, 9, 1, 7]
print(fast_sort(alist, 0, 6))