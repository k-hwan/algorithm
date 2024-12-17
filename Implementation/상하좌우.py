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