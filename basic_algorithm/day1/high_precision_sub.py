# 高精度减法
A = list(map(int, input()))[::-1]
B = list(map(int, input()))[::-1]

# 判断是否 A>=B
def com(A, B):
    # A, B位数不同,比较长度
    if len(A) != len(B):
        return len(A) > len(B)
    # A, B位数相同，从高到低比较每一位大小
    else:
        i = len(A) - 1
        while i >= 0:
            if A[i] != B[i]:
                return A[i] > B[i]
            i -= 1
    # A = B
    return True


# Sub
def sub(A, B):
    res = []
    t = 0 # 进位
    for i in range(len(A)):
        t = A[i] - t
        if i < len(B): t = t - B[i]

        res.append((t + 10) % 10)

        # 判断是否需要进位
        if t >= 0: t = 0
        else: t = 1

    # 去除后缀0 (也是去除前导0, 后面逆序接收)
    """
    pop () 函数用于移除列表中的一个元素（默认最后一个元素），并且返回该元素的值。 
    语法：list.pop (obj=list [-1]) //默认为 index=-1，删除最后一个列表值
    """
    while len(res) > 1 and res[-1] == 0:
        res.pop()
    return res

if com(A, B):
    res = sub(A, B)[::-1]
    print("".join(map(str, res)))
else:
    res = sub(B, A)[::-1]
    print("-" + "".join(map(str, res)))