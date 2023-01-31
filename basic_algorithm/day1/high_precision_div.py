# 高精度除法
"""
高精度大数除以低精度小数
"""
A = list(map(int, input()))[::-1]
b = int(input())


def div(A, b):
    res = []
    r = 0  # 余数
    # A已经为逆序, 从后往前遍历A
    for i in range(len(A) - 1, -1, -1):
        r = r * 10 + A[i]
        # 整除得商
        res.append(r // b)
        # 取模得余
        r %= b

    res = res[::-1] # 19,24可不用(本来就是正序res)
    return res, r


res, r = div(A, b)
res = res[::-1]
print("".join(map(str, res)))
print(r)
