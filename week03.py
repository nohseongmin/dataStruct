def inters(l1, l2):
    l3 = []
    for v in l1:
        if v in l2:
            l3.append(v)
    return l3


l1 = [45, 5, 22, 31, 7, 19]
l2 = [22, 1, 4, 2, 5, 23, 30, 13, 41, 19]
print(inters(l1,l2))

