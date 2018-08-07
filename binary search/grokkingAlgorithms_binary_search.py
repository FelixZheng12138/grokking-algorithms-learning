#!/usr/bin/python
# -*- coding: UTF-8 -*-
#《算法图解》(原书《grokking algorithms》)
# 二分查找
#书里是用循环来写的，这边是递归的版本，影响不大，本质思想是一样的
import sys
def main():
    for i in range(1, len(sys.argv)):
        print('para %s is：%s' % (i, sys.argv[i]))
    array = [9,8,7,6,5,4,3,2,1,0]
    goal = 5
    #可以改进为读取参数查找
    binnary_search(array,goal)
def binnary_search(array,goal):
    index = len(array)/2
    if goal == array[index]:
        print('find goal %s' % (array[index]))
        return True
    if goal < array[index]:
        print('%s < goal'%(array[index]))
        array = array[index:]
        print('new array: %s'%(array))
        return binnary_search(array,goal)
    if goal > array[index]:
        print('%s > goal'%(array[index]))
        array = array[0:index]
        print('new array: %s'%(array))
        return binnary_search(array,goal)
if __name__ == "__main__":
    main()
