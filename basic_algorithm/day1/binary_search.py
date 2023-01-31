# 整数二分
n, m = map(int, input().split())
q = list(map(int, input().split()))


def check(mid):  # 检查查找的x是否满足某种性质
    pass


# [l, r]被划分成[l, mid] [mid+1, r]
def binary_search_01(l, r):
    while l < r:
        mid = (l + r) // 2
        if check(mid):
            r = mid  # 检查mid是否满足某种性质
        else:
            l = mid + 1
    return l


# [l, r]被划分为[l, mid-1] [mid, r]
def binary_search_02(l, r):
    while l < r:
        mid = (l + r + 1) // 2  # l = r - 1
        if check(mid):
            l = mid
        else:
            r = mid - 1
    return l
