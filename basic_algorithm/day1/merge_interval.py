# 区间合并

n = int(input())
segs = []
# 数据读入
for _ in range(n):
    l, r = map(int, input().split())
    if l != r:
        segs.append((l, r))

# 区间排序
segs = sorted(segs, key=lambda x:(x[0], x[1]))
print(segs)
def merge(segs):
    res = []
    # 初始区间在[-无穷, +无穷]
    st, ed = -2e9, -2e9
    for i in range(len(segs)):
        # 无交集（区间左端点严格小于下一个区间的右端点）
        if ed < segs[i][0]:
            # 非初始化区间,
            if st != -2e9:
                res.append((st, ed))
            # 更新维护区间为下一个区间左右端点
            st = segs[i][0]
            ed = segs[i][1]
        # 有交集, 区间合并
        else:
            # 更新维护区间为2个区间的并集
            ed = max(ed, segs[i][1])
    # 最后剩余一个区间为对比
    if st != -2e9:
        res.append((st, ed))
    return res

segs = merge(segs)
print(len(segs))
