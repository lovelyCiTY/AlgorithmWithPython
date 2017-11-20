#!/usr/bin/env python3
# -*- coding: utf-8 -*-


'''

question：

Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

'''

# first method
# we can solve it in two way
# fistone solve it with dictionary speciality dictionary is hashable
class soulution(object):
    def towSum(self,nums,target):
        if len(nums) <= 1:
            return False
        dic = {}
        for i,value in enumerate(nums):
            if value in dic :
                if i < dic[value]:
                    return [i,dic[value]]
                else:
                    return [dic[value],i]
            else:
                dic[target - value] = i

        return False

 # second method
#  We can solve it with head and tail
    def towSumMethodTwo(self,nums,target):
        if len(nums) <= 1:
            return False

        head = 0
        tail = len(nums) - 1
        isfind = False
        while head < tail:
            if nums[head] + nums[tail] > target:
                tail = tail - 1
            elif nums[head] + nums[tail] < target:
                head = head + 1
            else:
    # if question tell you array can have same element ，you should have a constant to recorder it have finished
                isfind = True
                break
        if isfind :
            array = [head, tail]
            return array
        else:
            return False




