# 二维差分

N = 1010

# 初始化二维数组
arr = [[0]*N for _ in range(N)] #  前缀和数组
brr = [[0]*N for _ in range(N)] #  差分数组

# 数据读入
n, m, q = map(int, input().split())


# 1. 利用前缀和数组更新差分数组
# 2. 在[x1, y1, x2, y2]内进行插入数据操作
def insert(x1, y1, x2, y2, c):
    brr[x1][y1] += c
    brr[x1][y2+1] -= c
    brr[x2+1][y1] -= c
    brr[x2+1][y2+1] += c

# 初始化前缀和数组
for i in range(1, n+1):
    arr[i][1:m+1] = list(map(int, input().split()))

# 初始化差分数组
for i in range(1, n+1):
    for j in range(1, m+1):
        insert(i, j, i, j, arr[i][j])

# 插入数据进行q操作
while q>0:
    x1, y1, x2, y2, c = map(int, input().split())
    insert(x1, y1, x2, y2, c)
    q -= 1

# 差分数组求前缀和求a[i][j]
for i in range(1, n+1):
    for j in range(1, m+1):
        brr[i][j] += brr[i][j-1] + brr[i-1][j] - brr[i-1][j-1]
        print(brr[i][j], end=" ")
    print()
