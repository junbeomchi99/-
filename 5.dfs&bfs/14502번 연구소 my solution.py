from collections import deque
import copy
n, m = map(int, input().split())
graph = []
result = 0
for i in range(n):
    graph.append(list(map(int,input().split())))
dx = [-1,0,1,0]
dy = [0,-1,0,1]
que = deque()

#1 3개의 벽을 둔다, 벽이 3개일시 바이러스 전파를 실행함
def wall(x):
    if x == 3:
        bfs()
        return
    # 3개의 벽을 둘수 있는 모든 combinations에 한에서 반복한다
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                graph[i][j] = 1
                #여기서 만약에 wall이 3개가 된 경우 bfs가 실행되어서 
                #현재 조합에서 0 갯수가 몇개인지 파악을 하고 
                #제일 마지막에 넣었던 벽을 다시 0값으로 대체하고 다음 x,y 좌표부터 wall 실행 
                wall(x+1)
                graph[i][j] = 0


#2 바이러스를 전파 시킨다, 이것은 각 combinations마다 반복하며 최고 count 값을 result에 저장한다 
def bfs():
    temp = copy.deepcopy(graph)
    for i in range(n):
        for j in range(m):
            if temp[i][j] == 2:
                que.append((i,j))
    while que:
        x, y = que.popleft()            
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= 0 and nx < n and ny >= 0 and ny < m:
                if temp[nx][ny] == 0:
                    temp[nx][ny] = 2
                    que.append((nx,ny))
    #3 빈 공간에 값을 구한다 (바이러스 전파된 후 0의 갯수를 세는데 쓰임)
    cnt = 0
    for i in temp:
        cnt += i.count(0)
    global result
    result = max(result,cnt)


wall(0)
print(result)
