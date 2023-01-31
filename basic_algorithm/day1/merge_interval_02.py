# 区间合并 02
n = int(input())
segs, res = [], []
for _ in range(n):
    l, r = map(int, input().split())
    if l != r:
        segs.append((l, r))

segs.sort()


def merge(res, segs):
    for i in range(len(segs)):
        if res:
            # res中最后一项的右端点 > segs中的左端点（包含了3种）
            if res[-1][1] >= segs[i][0]:
                # 更新维护区间
                res[-1][1] = max(res[-1][1], segs[i][1])

            else:
                res.append([segs[i][0], segs[i][1]])
        else:
            res.append([segs[0][0], segs[0][1]])
    return len(res)

print(merge(res, segs))
