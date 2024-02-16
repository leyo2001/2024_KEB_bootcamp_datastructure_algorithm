from collections import deque
n = int(input())
l = int(input())

g = [[0 for _ in range(n+1)] for _ in range(n+1)]
v = [0 for _ in range(n+1)]

for _ in range(l):
    a, b = map(int, input().split())
    g[a][b] += 1
    g[b][a] += 1

q = deque()
q.append(1)
v[1] = 1
while q:
    i = q.popleft()
    for j in range(1,len(g)):
        if g[i][j] == 1 and not v[j]:
            q.append(j)
            v[j] = 1

cnt = 0
for i in range(1,len(v)):
    if v[i] == 1:
        cnt += 1

print(f'{cnt-1}')


