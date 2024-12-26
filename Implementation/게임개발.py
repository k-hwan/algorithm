# N, M을 공백으로 구분하여 입력받기
n, m = map(int, input().split())

# 현재 캐릭터의 X좌표, Y좌표, 방향을 입력받기
x, y, direction = map(int, input().split())

# 전체 맵 정보를 입력받기
array = [list(map(int, input().split())) for _ in range(n)]

# 현재 위치 방문 처리 (2로 표시)
array[x][y] = 2

# 방향에 따른 이동 정의 (북, 동, 남, 서)
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 왼쪽으로 회전
def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3

# 시뮬레이션 시작
count = 1
turn_time = 0

while True:
    # 왼쪽으로 회전
    turn_left()
    nx = x + dx[direction]
    ny = y + dy[direction]
    
    # 정면에 가보지 않은 칸이 존재하는 경우 이동
    if 0 <= nx < n and 0 <= ny < m and array[nx][ny] == 0:
        array[nx][ny] = 2  # 방문 처리
        x, y = nx, ny
        count += 1
        turn_time = 0
        continue
    else:
        turn_time += 1
    
    # 네 방향 모두 갈 수 없는 경우
    if turn_time == 4:
        nx = x - dx[direction]
        ny = y - dy[direction]
        
        # 뒤로 갈 수 있다면 이동 (방문했거나 육지일 경우만 가능)
        if 0 <= nx < n and 0 <= ny < m and array[nx][ny] != 1:
            x, y = nx, ny
        else:
            # 뒤가 바다이거나 맵 경계를 벗어나면 종료
            break
        turn_time = 0

# 최종적으로 방문한 칸의 개수 출력
print(count)



