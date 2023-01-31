#  归并排序
"""
1. 递归左右两边  2.划分左右两边 x = (l + r) // 2 3.先让左半 < 右半，存入tmp,最后未对比完的追加合并即可
"""

n = int(input())
a = list(map(int, input().split()))


def merge_sort(a, l, r):
    if l >= r: return
    mid = (l + r) // 2
    # 递归左右两边
    merge_sort(a, l, mid)
    merge_sort(a, mid + 1, r)
    # tmp存对比答案、i和j分别为左右两边的起点
    tmp, i, j = [], l, mid + 1

    while i <= mid and j <= r:
        # 左半 < 右半, 指针前进
        if a[i] <= a[j]:
            # 相等时装右边, 保证其归并排序的稳定性(等值索引不变)
            tmp.append(a[i])
            i += 1
        else:
            tmp.append(a[j])
            j += 1
    # 右半指针到终点, 将下标为i之后的所有元素追加
    if i <= mid: tmp += a[i:mid + 1]
    # 左半指针到终点，将下标为j之后的所有元素追加
    if j <= r: tmp += a[j:r + 1]
    # 将答案复制到res a中
    a[l:r + 1] = tmp[:]


merge_sort(a, 0, n-1)
print(' '.join(map(str, a)))
