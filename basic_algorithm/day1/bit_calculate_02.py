# 位运算:
# 统计x中1出现的个数
"""
    1. lowbit返回x最右边为1之后的所有数字 x & -x
                                             x = 1010 lowbit(x) = 10
                                             x = 1010001000 lowbit(x) = 1000
"""
n = int(input())
arr = list(map(int, input().split()))


def lowbit(x):
    return x & -x


for i in range(n):
    ans = 0
    # 依次处理每一个数字
    while arr[i]:
        # 依次减掉为最右边为1的数字
        arr[i] -= lowbit(arr[i])
        # 减掉一次说明最右边含1
        ans += 1
    print(ans)
