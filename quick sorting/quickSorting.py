#!/usr/bin/python
# -*- coding: UTF-8 -*-
#《算法图解》(原书《grokking algorithms》)
# 快排
def quickSort(array):
    if len(array) <2:
        return array
    else:
        flag = array[0]
        print('flag is :',flag)
        less = [i for i in array[1:] if i< flag]
        greater = [i for i in array[1:] if i >= flag]
        print('less is :',less,'greater is : ' , greater)
        return quickSort(less) + [flag]+ quickSort(greater)
def main():
    print quickSort([9,8,7,6,5,4,3,2,1])
if __name__ == "__main__":
    main()
