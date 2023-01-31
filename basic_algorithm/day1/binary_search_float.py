# 浮点数二分

# acwing 790. 数的三次方根
n = float(input())
l, r = -10000, 10000

while (l - r) < -1e-8:
    mid = (l+r) / 2

    if mid ** 3 >= n:
        r = mid

    else:
        l = mid

print("{:.6f}".format(l))

