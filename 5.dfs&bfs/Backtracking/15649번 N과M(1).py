#https://www.acmicpc.net/problem/15649
#python3 으로 돌려야 돌아감
#back tracking에 기초 
#permutations 개념이랑 같음
#https://blog.encrypted.gg/945

n, m = map(int, input().split())

comb = []
visited = [False] * (n)

def search(x):
    if x == m:
        print(*comb)
        return
    for i in range(n):
        if visited[i] == False:
            visited[i] = True
            comb.append(i+1)
            search(x+1)
            visited[i] = False
            comb.pop()
search(0)