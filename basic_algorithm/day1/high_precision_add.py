# 高精度加法
"""
"""
# 逆序读入数据进行存储(从低位到高位)
n = list(map(int, input()[::-1]))
print(n)
m = list(map(int, input()[::-1]))
print(m)

def add(n, m):
    res = []
    t = 0  # 进位(初始最后一位为0)
    i, j = 0, 0
    # 遍历两个list，进行加法
    while i < len(n) or j < len(m):
        if i < len(n):
            t += n[i]
            i += 1

        if j < len(m):
            t += m[j]
            j += 1
        # for i in range(0, len(n)) or range(0, len(m)):
        #     if i < len(n):
        #         t += n[i]
        #     if i < len(m):
        #         t += m[i]
        # 每一位的和位n[i] + m[i] + t
        res.append(t % 10)  # 取n[i] + m[i] 余数
        t //= 10  # 进位1 or 0
    # if t: res.append(1)
    if t: res.append(t)
    return res


res = add(n, m)[::-1]
print("".join(map(str, res)))
