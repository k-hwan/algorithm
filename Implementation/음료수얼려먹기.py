n,m=map(int,input().split())
arr=[list(map(int,input())) for _ in range(m)]
dx=[-1,1,0,0]
dy=[0,0,-1,1]
x=0
y=0

def dfs(x,y):
    arr[x][y] = 1  # 현재 위치를 방문한 것으로 표시
    stack = [(x, y)]  # 스택을 사용하여 DFS 구현

    while stack:
        x, y = stack.pop()  # 스택에서 위치를 가져옴
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y

            if 0 <= nx < n and 0 <= ny < m and arr[nx][ny] == 0:
                arr[nx][ny] = 1  # 방문한 것으로 표시
                stack.append((nx, ny))  # 스택에 추가

result = 0
for i in range(n):
    for j in range(m):
        if arr[i][j] == 0:  # 얼음 틀이 비어있는 경우
            dfs(i, j)
            result += 1

print(result)
