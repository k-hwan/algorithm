n='d4'
arr=list(n)
count=1
alphas=['a','b','c','d','e','f','g','h']
for alpha in alphas:
    if arr[0]==alpha:
        break
    else : 
        count=count+1
arr[0]=count
array=list(map(int,arr))
cnt=0
x,y=array[0],array[1]

dx=[-2,-2,-1,1,2,2,1,-1]
dy=[-1,1,2,2,1,-1,-2,-2]
for i in range(8):
    nx=x+dx[i]
    ny=y+dy[i]
    if nx<1 or ny<1 or nx>8 or ny>8:
        continue
    else:
        cnt=cnt+1
print(cnt)




# 왕실의 나이트 (p.115)
# 왕실 정원은 8 X 8 좌표 평면이다
# 왕실 정원의 특정한 한 칸에는 나이트가 서 있다. 나이트는 아래처럼 2가지 경우로 이동할 수 있다.
# 수평으로 두 칸 이동한 뒤에 수직으로 한 칸 이동하기
# 수직으로 두 칸 이동한 뒤에 수평으로 한 칸 이동하기
# 왕실 정원의 행 위치는 1부터 8로 표현하고, 열 위치는 a부터 h로 표현한다
# 만약 나이트가 좌표 평면을 벗어나게 되면 이동할 수 없다
# 이동할 수 있는 경우의 수를 출력
# a1에 위치한 나이트가 이동할 수 있는 경우의 수 ⇒ 2

# ============================================================================

# 내가 짠 코드는 길고 가독성이 안좋다.

# input_data = input()
# row = int(input_data[1])
# column = int(ord(input_data[0])) - int(ord('a')) + 1              # 아스키 코드를 활용할 수도

# steps = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1,2 ), (-2, 1)]
# rows = ["1", "2", "3", "4", "5", "6", "7", "8"]
# columns = ["a", "b", "c", "d", "e", "f", "g", "h"]
# loc = list(n)
# loc_r = rows.index(loc[1]) + 1
# loc_c = columns.index(loc[0]) + 1
# count = 0                                       # 인덱스함수를 활용해도됨
