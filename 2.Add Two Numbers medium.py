#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8

'''

# the meaning of question is give values 342 and 465 ,now plus them with result 807 and  expression it with link

class listNode(object):
    def __init__(self,x):
        self.value = x
        self.next = None

#My first resolve plan
# the result is Time Limit Exceeded
class Solution(object):
    def addTwoNumbers1(self, l1, l2):
        if not l1 and not l2:
            return None

        isNeedAddOne = False
        resultnode = listNode(-1)
        result = []
        while l1 or l2:
            if not l1:
                value1 = l1.val
                l1 = l1.next
            else:
                value1 = 0

            if not l2:
                value2 = l2.val
                l2 = l2.next
            else:
                value2 = 0

            if value1 + value2 >= 10:
                nodeValue = value1 + value2 - 10
                if isNeedAddOne:
                    nodeValue = nodeValue + 1
                result.append(nodeValue)
                isNeedAddOne = True
            else:
                nodeValue = value1 + value2
                if isNeedAddOne:
                    nodeValue = nodeValue + 1
                result.append(nodeValue)
                isNeedAddOne = False
            if not l1 and not l2:
                break

        for i in result:
            if not resultnode:
                resultnode.val = i
            else:
                nodeItem = listNode(i)
                resultnode.next = nodeItem

        return resultnode

# discuss 中的解决方案

class Soulution(object):
    def addTwoNumbs(self,l1,l2):
        # 浅拷贝
        carry = 0
        root = node = listNode(0)
        while l1 or l2 or carry:
            value1 = value2 = 0
            if l1:
                value1 = l1.val
                l1 = l1.next
            if l2:
                value2 = l2.val
                l2 = l2.next
            # divmod 是 python 提供的一个计算函数 前边的结果为整除值 后边的结果为余数
            carry, value = divmod(value1 + value2 + carry, 10)
            # 这里很巧妙的运用了浅拷贝的概念
            # 产生了新的对象 进行了赋值
            node.next = listNode(value)
            node = node.next

        return root



