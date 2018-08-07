#!/usr/bin/python
# -*- coding: UTF-8 -*-
#《算法图解》(原书《grokking algorithms》)
# 递归
#这章没有好写的例子
#不过栈讲的很好，把递归的栈调用输出一下吧


def fact(number):
    if number == 1:
        print('push(入栈): fact(%s)' % (number - 1))
        return 1
    else:
        print('push(入栈): fact(%s)' % (number - 1))
        return number * fact(number - 1)
def main():
    fact(5)
if __name__ == "__main__":
    main()
