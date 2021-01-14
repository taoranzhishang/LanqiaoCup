# -*-coding:utf-8-*-
# @Author:  陶然至上
# @Email:   taoranzhishang@hotmail.com
# @File:    03.py
# @Time:    2021/1/14 18:33
# @Software:PyCharm
"""
<p> [问题描述] <br>将 LANQIAO中的字母重新排列，可以得到不同的单词，如LANQIAO、
AAILNOQ等，注意这7个字母都要被用上，单词不一-定有具体的英文意义。<br>请问，总共
能排列如多少个不同的单词。<br>
7个字母的全排列，7个都要用上，即是7! = 7 * 6 * 5 * 4 * 3 * 2 * 1 = 5040。
这里由于A有2个，所以我们需要再处于A22,即5040/2 = 2520即答案为2520
"""
num = 7
ans = 1
while num > 0:
    ans *= num
    num -= 1
print(ans // 2)
