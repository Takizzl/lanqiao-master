# 双指针02：
"""
template:
    while i < n:
        while j <= i and check(i, j):
            j += 1
        res = max(res, i - j + 1)

"""
N = 300010
n = int(input())
arr = list(map(int, input().split()))

index = [0] * N
i, j, ans = 0, 0, 0

for i in range(n):
    # 记录arr[i]出现次数
    index[arr[i]] += 1
    # 判断是否出现重复数字
    while j < i and index[arr[i]] > 1:
        # 出现重复数字后, 将该数字之前的数字全部删除,从下一位开始扫描
        index[arr[j]] -= 1
        # 将j的位置更新为最后一个重复的数字上
        j += 1
    # 更新最长序列
    ans = max(ans, i - j + 1)

print(ans)