# 位运算:
"""
    1. n >> k&1 返回n的二进制第k位是多少(10 1010) 高到低位
"""
n, k = map(int, input().split())

while k>=0:
    print(n >> k&1, end= " ")
    k -= 1
