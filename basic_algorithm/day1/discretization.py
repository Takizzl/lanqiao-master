# 离散化
"""
template:
    # 离散序列去重+排序：
    alls = list(set(alls))
    alls.sort()
    # 二分查找x在离散序列上的位置：
    l, r = 0, len(alls) - 1
    while l < r:
        mid = (l + r) // 2
        if (alls[mid] >= x): r = mid
        else: l = mid + 1
    return r + 1 (前缀和序列: 1,2,3,4,......n)

"""
N = 300000 + 10  # 数据范围n + 2m e5
n, m = map(int, input().split())
a = [0] * N
s = [0] * N
alls, add, query = [], [], []

for _ in range(n):
    x, c = map(int, input().split())
    add.append((x, c))
    alls.append(x)

for _ in range(m):
    l, r = map(int, input().split())
    query.append((l, r))
    alls.append(l)
    alls.append(r)
# 离散序列去重, 排序
alls = list(set(alls))
alls.sort()


# 找到x在离散序列中的坐标(二分)
def find(x):
    l, r = 0, len(alls) - 1
    while l < r:
        mid = (l + r) // 2
        if alls[mid] >= x:
            r = mid
        else:
            l = mid + 1
    return r + 1


# 将数据在对应的离散序列中插入
for x, c in add:
    index = find(x)
    a[index] += c

# 处理在数据范围内的前缀和
for i in range(1, N):
    s[i] = s[i - 1] + a[i]

# 将[l, r]映射到离散区间后, 利用前缀和进行处理
for l, r in query:
    l = find(l)
    r = find(r)
    print(s[r] - s[l - 1])
