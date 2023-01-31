# 一维前缀和
N = 100010
n, m = map(int, input().split())

a = [0] + list(map(int, input().split()))
s = [0] * N

for i in range(1, n+1):
    s[i] = s[i-1] + a[i]

for _ in range(m):
    l, r = map(int, input().split())
    print(s[r] - s[l-1])