N=int(input())
x,y=1,1
plans=input().split()
dx=[-1,0,+1,0]
dy=[0,+1,0,-1]
move_tyles=['u','r','d','l']
for plan in plans:
    for i in range(4):
        if plan==move_tyles[i]:
            nx=x+dx[i]
            ny=y+dy[i]
    if nx<1 or ny<1 or nx>N or ny>N:
        continue

    x,y=nx,ny

print(f'{x} {y}')






# 상하좌우 (p.110)
# A는 N X N 크기의 정사각형 공간 위에 있다.
# 가장 왼쪽 위 좌표는 (1, 1)이고, 가장 오른쪽 아래 좌표는 (N, N)이다.
# A는 상(U), 하(D), 좌(L), 우(R) 방향으로 이동할 수 있다.
# 시작 좌표는 항상 (1, 1)이다.
# N X N 크기의 정사각형 공간을 벗어나는 움직임은 무시된다.
# 5 X 5 크기의 공간에서 R, R, R, U, D, D순으로 움직였을 때 좌표 ⇒ (3, 4)
