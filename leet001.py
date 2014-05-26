#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'florije'

if __name__ == '__main__':
    '''
    abc def形式的字符串翻转成def abc，并且去掉多余的空格。
    '''
    des = 'abc def'[::-1].split(' ')
    target_list = []
    for w in des:
        target_list.append(w[::-1])
    target_str = ' '.join(target_list)
    print target_str

    print ' '.join([word[::-1] for word in 'abc  def'[::-1].split()])

    # a = "abc def"
    # listA = a.split(' ')
    # print listA
    # b = ''
    # for item in listA:
    #     b = item + ' '+ b
    #
    # print b
    a, b = 1, 2
    a, b = b, a + b
    print a, b

    print ' '.join('abc  def'.split()[::-1])