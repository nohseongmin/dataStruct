def inters(l1, l2):
    s1 = set(l1)
    s2 = set(l2)
    #return list(s1.intersection(s2)) #교집합
    #return list(s1.union(s2))        #합집합
    #return list(s1 & s2)             #차집합 다른 집합도 + / 등 사용가능
    return list(s1.difference(s2))    #차집합


l1 = [45, 5, 22, 31, 7, 19]
l2 = [22, 1, 4, 2, 5, 23, 30, 13, 41, 19]
print(inters(l1,l2))

