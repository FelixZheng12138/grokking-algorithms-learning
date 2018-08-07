#!/usr/bin/python
# -*- coding: UTF-8 -*-
#《算法图解》(原书《grokking algorithms》)
# 选择排序

def findSmallest(array):
    smallestItem = array[0]
    for item in array:
        if item < smallestItem:
            smallestItem = item
    return smallestItem
def selectionSorting(array,retrunArr):
    if len(array)==0:
        print('final retrun : %s' % (retrunArr))
        return retrunArr
    else:
        smallestItem = findSmallest(array)
        retrunArr.append(smallestItem)
        array.remove(smallestItem)
        print('find smallestItem: %s, rest array: %s' % (smallestItem,array ))
        return selectionSorting(array,retrunArr)
def main():
    retrunArr = []
    array = [6,5,4,3,2,1]
    selectionSorting(array,retrunArr)
if __name__ == "__main__":
    main()
