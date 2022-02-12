#https://www.acmicpc.net/problem/status/18352
from collections import deque

#도시의 개수 N, 도로의 개수 M, 거리 정보 K, 출발 도시의 번호 X 입력
n, m, k, x = map(int, input().split())
graph = [[] for _ in range (n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

# 방문한 도시 최단거리 정리
visited = [-1] * (n+1)
visited[x] = 0

queue = deque()
queue.append(x)
while queue:
    now = queue.popleft()
    if visited[now] < 0:
         continue
    #현재 도시에 연결되있는 도시중 방문하지 않은 도시가 있다면
    for connected_city in graph[now]:
        if visited[connected_city] == -1:
            visited[connected_city] = visited[now] + 1
            queue.append(connected_city)
exist = 0
for i in range(1, n+1):
    if visited[i] == k:
        print(i)
        exist = 1
if exist == 0:
    print(-1)


