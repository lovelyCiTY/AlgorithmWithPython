#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Given a string, find the length of the longest substring without repeating characters.

Examples:

Given "abcabcbb", the answer is "abc", which the length is 3.

Given "bbbbb", the answer is "b", with the length of 1.

Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.

题意 找到最大长度不重复的连续的长度
'''


#this is my answer
#思路 O(N) 每隔字符查找一遍进行解决 最开始的设想使用 SET  但是存在很多问题....
class Solution(object):
    def lengthOfLongestSubstring1(self, s):
        if len(s) == 1:
            return len(s)
        beforeArray = []
        newArray = []
        sets = set()
        for c in s:
            # print(c)
            beforeArray.append(c)
            sets.add(str(c))
            if len(beforeArray) != len(sets):
                print(len(beforeArray))
                print(len(sets))
                repeatItem = beforeArray[-1]
                for index,item in enumerate(beforeArray):
                    if item == repeatItem and index != len(beforeArray) - 1:
                        print(len(beforeArray))
                        if len(beforeArray) > 2:
                            array1 = beforeArray[0:len(beforeArray) - 2]
                        else:
                            array1 = beforeArray[-1]
                        print('array1 == %s' % array1)
                        if len(array1) >= len(newArray):
                            print('begins')
                            newArray = array1
                            print(newArray)
                            print('index === %s' % index)
                            if len(beforeArray) > 2:
                                beforeArray = beforeArray[index:]
                            else:
                                beforeArray = [beforeArray[-1]]
                            newset = set()
                            for value in beforeArray:
                                set().add(str(value))
                            sets = newset
                            print('end')
                        break

        print(newArray)
        return len(newArray)



result = Solution()


### 后来在 subssion 中找到的高效答案
### 总结错误原因  题目理解不清晰  题目要求找出相应的长度  而我以为是打印出对应的字符串 而且当时确实没想到下边的简便方案


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        maxlength = start = 0
        values = {}

        for i in range(len(s)):
            #如果 i 在 values 中存在 那么就代表查找出重复 且放置 i = 0 进入的情况
            if s[i] in values and start <= values[s[i]]:
                # 有重复则从重复的点下一位开始
                start = values[s[i]]
            else:
                # 的初当前最大长度
                maxlength = max(maxlength,i - start + 1)

            values[s[i]] = i

        return maxlength