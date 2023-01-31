# 一维差分
"""
in:
6 3
1 2 2 1 2 1
1 3 1
3 5 1
1 6 1
out:
3 4 5 3 4 2
"""
N = 100010
n, m = map(int, input().split())
arr = [0] * N # 前缀和数组
brr = [0] * N # 差分数组

# 初始化前缀和数组
arr[1:n+1] = list(map(int, input().split()))

# 利用前缀和数组更新(初始化)差分数组
for i in range(1, n+1):
    brr[i] = arr[i] - arr[i-1]

def insert(l, r, c):
    # 最左端+c,最右端r+1 -c (保证在前缀和的定义基础上在[l, r]内操作)
    brr[l] += c
    brr[r + 1] -= c

# 在[l, r]区间内对差分数组进行插入操作
for i in range(m):
    l, r, c = map(int, input().split())
    insert(l, r, c)

# 差分数组操作完成, 利用差分与前缀和定义求前缀和数组即a[i]
for i in range(1, n+1):
    brr[i] += brr[i-1]
    print(brr[i], end=" ")
