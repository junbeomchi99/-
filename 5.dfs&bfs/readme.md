# DFS & BFs

참고: (나동빈님 이것이 취업을 위한 코딩 테스트다 with 파이썬 자료 참고)

https://www.youtube.com/watch?v=7C9RgOcvkvo&ab_channel=%EB%8F%99%EB%B9%88%EB%82%98
<br>
https://www.youtube.com/watch?v=1vLqC1rItM8&list=PLVsNizTWUw7H9_of5YCB0FmsSc-K44y81&index=18

# Stack 

선입후출 (First In Last Out) 구조 또는 후입선출 (Last in First Out) 구조라고 불림
- 박스 쌓기에 비유할수 있음
- stack.append()
- stack.pop()

# Que
선입설출 (First in First Out)
- 대기줄에 비유 가능 ('공정한' 자료구조라 비유됨)
- from collections import deque
- queue = deque()
- queue.append()
- queue.popleft()

# Recursive Function (재귀 함수)
자기 자신을 다시 호춣하는 함수
- 종료 조건 필수 (함수가 무한 호출 될수 있음)
- tmi: 컴퓨터 내부에서 재귀 함수의 수행은 스택 자료구조 이용. 함수를 계속 호출 했을때 가장 마지막에 호출한 함수가 먼저 수행을 끝내냐 그 앞의 함수 호출이 종료 되기 때문
- = 재귀 함수는 내부적으로 스택 자료구조와 동일하다
> 스택 자료구조를 활용해야 하는 상당수 알고리즘은 재귀 함수를 이용해서 간편 구현 가능 (e.g. DFS)

# 그래프 구조
![image](https://miro.medium.com/max/976/0*UgMHEDLriw2efXbx)

노드 (Node)와 간선 (Edge)으로 노드를 정점(Vertex)라고도 표현함. 

두 노드가 간선으로 연결되어 있다면 '두 노드는 인접하다 (Adjacent)'라고 표현 
- 노드 1 과 노드 3은 인접하다 (Node 1 is adjacent to Node 3)

프로그래밍에서 그래프 표현방식
1. 인접 행렬 (Adjacency Matrix): 2차원 배열로 그래프의 연결 관계를 표현하는 방식
- 연결 되어 있지 않은 노드끼리는 무한의 비용이라고 작성 (데이터를 초기화해줌)
e.g.
```python
INF = 999999999 #무한의 비용 선언
#2차원 리스트를 이용해 인접 행렬 (Adjacency Matrix) 표현
graph  [
    [0, 7 ,5],
    [7, 0 ,INF],
    [5, INF, 0]
]
#코드와 무관하며 print(graph)했을시 결과
[[0,7,5], [7,0, 999999999], [5, 999999999, 0]]
```
2. 인접 리스트(Adjacency List): 리스트로 그래프의 연결 관계를 표현하는 방식
- 연결 리스트 (LinkedList) 라는 자료구조를 이용해 구현
![image](https://images.velog.io/images/hyewonkkang/post/93699df9-1619-4594-b22d-887236f351ed/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA%202022-01-29%20%E1%84%8B%E1%85%A9%E1%84%8C%E1%85%A5%E1%86%AB%2012.12.05.png)

```python
# 행(row)이 3개인 2차원 리스트로 인접 리스트 표현
graph = [[] for _ in range(3)]

#노드 0에 연결된 노드 정보 저장(노드, 거리)
graph[0].append((1,7))
graph[0].append((2,5))
#노드 1에 연결된 노드 정보 저장(노드, 거리)
graph[1].append((-,7))
#노드 2에 연결된 노드 정보 저장(노드, 거리)
graph[2].append((0,5))

#코드와 무관하며 print(graph)했을시 결과
[[(1,7), (2,5)], [(0,7)], [(0,5)]]
```

# 인접 행렬 (adj. matrix) vs 인접 리스트 (adj. list)

메모리 측면:
- 인접 행렬 = 모든 관계를 저장, 노드 개수가 많을수록 메모리 낭비가 큼
- 인접 리스트 = 연결된 정보만 저장하기 떄문에 메모리 효율적 사용

속도 측면
- 인접 리스트: 두 노드가 연결되어 있는지에 대한 정보를 얻는 속도가 느림 
- 왜냐: 연결된 데이터를 하나씩 확인해야 하기 떄문. 

# DFS
Depth-First Search = 깊이 우선 탐색, 그래프에서 깊은 부분을 우선적으로 탐색하는 알고리즘

Stack (or recursive function) 자료구조 이용:
1. 탐색 시작 노드를 스택에 삽입하고 방문 처리
2. 스택의 최상단 노드에 방문하지 않은 인접 노그다 있으면 그 인접 노드를 스택에 넣고 방문 처리. (방문하지 않은 인접 노드가 없으면 스택에서 최상단 노드를 꺼냄)
3. 2번 과정을 더 이상 수행할 수 없을 때까지 반복한다. 

특징: 데이터 개수가 N개인 경우 O(N)의 시간이 소요됨

# BFS
breadth first search = 너비 우선 탐색
- 가까운 노드부터 탐색하는 알고리즘 (dfs의 반대)

que 자료구조 이용:
1. 탐색 시작 노드를 큐에 삽입하고 방문 처리를 한다
2. 큐에서 노드를 꺼내 해당 노드의 인접 노드 중에서 방문하지 않은 노드를 모두 큐에 삽입 하고 방문 처리를 한다
3. 2번의 과정을 더 이상 수행할 수 없을 때까지 반복한다. 
