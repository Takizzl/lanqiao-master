# acwing.785 快速排序
# 快速排序
"""
1. 取值q[l], q[r], q[(l + r) // 2] 2. 划分边界左右两边  3.递归左右两边
"""
# python data input
n = int(input())
# q = [int(x) for x in input()]
q = list(map(int, input().split()))  # 输入多行数据


def quick_sort(q, l, r):
    # 边界判断
    if l >= r:
        return
    # 边界值确定 q[l], q[r], q[(l+r)/2]
    x = max(min(q[l], q[r]), q[(l + r) // 2])
    # 指针在数组范围外，方便遍历
    i, j = l - 1, r + 1
    # 迭代寻找左右两半
    while i < j:
        i += 1
        j -= 1
        # 满足右半
        while q[i] < x: i += 1
        # 满足左半
        while q[j] > x: j -= 1
        # 指针停止，说明右半与左半条件不满足，交换
        if i < j: q[i], q[j] = q[j], q[i]
    # 递归分界左右两边
    quick_sort(q, l, j)
    quick_sort(q, j + 1, r)


if __name__ == "__main__":
    quick_sort(q, 0, n - 1)
    print(' '.join(map(str, q)))
    print("ok")
