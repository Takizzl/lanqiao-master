# 双指针：
"""
template:
    i, j = 0, 0
    while i < n:
        while j < i and check(i, j):
            j += 1
        i += 1
    i, j = 0, 0
"""
arr = input()
i, n = 0, len(arr)

while i < n:
    j = i
    # 内部指针j遍历arr直至空格
    while j < n and arr[j] != " ":
        j += 1
    # j移动到空格
    """
    去除abc   ddd中多个空格
    if arr[i] != " ":
    if i != j:
        a = arr[i:j]
        print(a)
    """
    # 不去除abc   ddd中多个空格，保持原序列
    a = arr[i:j]
    print(a)
    # 外部指针i直接移动至j(即空格处), 遍历下一个单词
    i = j
    i += 1

