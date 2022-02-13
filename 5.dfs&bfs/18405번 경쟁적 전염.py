#실패... bfs를 이용해야됨으로 deque 이용해보기 !
n,k = map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(map(int,input().split())))

s,finalx,finaly = map(int, input().split())

#바이러스 타입 다 찾기
viruses = []
for i in range(n):
    for j in range(n):
        if graph[i][j] != 0 and graph[i][j] not in viruses:
            viruses.append(graph[i][j])
viruses.sort()


def infect(x,y, virus):
    # n x n 맵 안에 없다면 종료
    if x <= -1 or x >= n or y <= -1 or y>=n:
        return         
    if graph[x][y] == 0:
        graph[x][y] = virus
    

# 시간별로 바이러스 투입
while s > 0:
    for virus in viruses:
        coordinates = []
        for x in range(n):
            for y in range(n):
                if graph[x][y] == virus:
                    coordinates.append([x,y])
        for pair in coordinates:
            x = pair[0]
            y = pair[1]
            infect(x-1,y,virus)
            infect(x+1,y,virus)
            infect(x,y-1,virus)
            infect(x,y+1,virus)
    s = s - 1
print(graph[finalx-1][finaly-1])
