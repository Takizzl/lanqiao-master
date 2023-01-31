# 高精度乘法

""""
大数和小数相乘。主要思想是把小数b看成一个整体，用A去乘（A每位去乘）
"""
A = list(map(int, input()))[::-1]
b = int(input())

def mul(A, b):
    res = []
    t = 0 # 进位
    for i in range(len(A)):
        # x = A的每一位乘以b + 前一位的进位
        t += A[i] * b
        # 取模得余数
        res.append(t % 10)
        # 整除得进位
        t //= 10

    while t:
        res.append(t % 10)
        t //= 10
    return res


res = mul(A, b)[::-1]
print("".join(map(str, res)))