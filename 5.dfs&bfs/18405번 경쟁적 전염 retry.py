from collections import deque

n, k = map(int, input().split())

graph = [] # 전체 보드 정보를 담는 리스트
virus_info = [] # 바이러스에 대한 정보를 담는 리스트

for i in range(n):
    # 보드 정보를 한 줄 단위로 입력
    graph.append(list(map(int, input().split())))
    for j in range(n):
        # 해당 위치에 바이러스가 존재하는 경우
        if graph[i][j] != 0:
            # (바이러스 종류, 시간, 위치 X, 위치 Y) 삽입
            virus_info.append((graph[i][j], 0, i, j))
virus_info.sort()
que = deque(virus_info)

target_s, target_x, target_y = list(map(int, input().split()))

#movements
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

while que:
    virus, s, x, y = que.popleft()
    if s == target_s:
        break
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx and nx < n and 0 <= ny and ny < n:
            # 아직 방문하지 않은 위치라면, 그 위치에 바이러스 넣기
            if graph[nx][ny] == 0:
                graph[nx][ny] = virus
                que.append((virus, s + 1, nx, ny))

print(graph[target_x -1][target_y - 1])
        

        