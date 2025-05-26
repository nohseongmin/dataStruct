from collections import deque

d = deque([91, 3, 77])
d.append(-13)
d.append(100)
d.append(99)
for _ in range(len(d)):
    print(d.popleft(), end="->")