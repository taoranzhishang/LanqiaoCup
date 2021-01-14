# -*-coding:utf-8-*-
# @Author:  陶然至上
# @Email:   taoranzhishang@hotmail.com
# @File:    03.py
# @Time:    2021/1/14 17:21
# @Software:PyCharm
"""
样题 2：特别数的和（编程大题）
【问题描述】 小明对数位中含有 2、0、1、9 的数字很感兴趣（不包括前导 0），
在 1 到 40 中这 样的数包括 1、2、9、10 至 32、39 和 40，共 28 个，他们的和是 574。
请问，在 1 到 n 中，所有这样的数的和是多少？
"""

ans = 0
num = eval(input())

for i in range(1, num + 1):
    for j in "2019":
    #if '2' in str(i) or '0' in str(i) or '1' in str(i) or '9' in str(i):
        if j in str(i):
            ans += i
            break
print(ans)
