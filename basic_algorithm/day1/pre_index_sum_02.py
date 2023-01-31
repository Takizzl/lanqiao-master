# 二维前缀和
N = 1010
n, m, q = map(int, input().split())

# 初始化原数组和前缀和数组
a = [[0]*N for _ in range(N)]
s = [[0]*N for _ in range(N)]

# 输入数据
for i in range(1, n+1):
    a[i][1:] = map(int, input().split())

# 前缀和计算
for i in range(1, n+1):
    for j in range(1, m+1):
        s[i][j] = s[i-1][j] + s[i][j-1] - s[i-1][j-1] + a[i][j]

# 针对每次query进程前缀和处理
for _ in range(q):
    x1, y1, x2, y2 = map(int, input().split())
    ans = s[x2][y2] - s[x2][y1-1] - s[x1-1][y2] + s[x1-1][y1-1]
    print(ans)