adjList = [
    [1, 2],     # 0
    [0, 3, 4],  # 1
    [0, 4],     # 2
    [1, 5],     # 3
    [1, 2, 5],  # 4
    [3, 4, 6],  # 5
    [5]]        # 6

def dfs(v, N):
    visited = [0] * N                   # visited 생성
    stack = [0] * N                     # stack 생성
    top = -1    
    print(v)

    visited[v] = 1                      # 시작점 방문 표시
    while True:
        for w in adjList[v]:            # if (v의 인접 정점 중 방문 안 한 정점 w가 있으면)
            if visited[w] == 0:         # push(v), v <- w, 
                top += 1
                stack[top] = v
                v = w
                print(v)                # 방문
                visited[w] = 1          # visited[w] <- true;
                break
        else:                           # w가 없으면
            if top != -1:               # 스택이 비어있지 않은 경우
                v = stack[top]
                top -= 1
            else:                       # 스택이 비어 있으면
                break                   # while

V, E = map(int, input().split())
N = V + 1
adjList = [[] for _ in range(N)]
for _ in range(E):
    a, b = map(int, input().split())
    adjList[a].append(b)
    adjList[b].append(a)

visited = [0] * N
stack = [0] * N
dfs(1, N)
print()