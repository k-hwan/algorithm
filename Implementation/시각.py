def solution(n) :
    time = [0,0,0]
    answer = 0

    for i in range(n+1) :
        time = [i, 0, 0]
        for j in range(60) :
            time = [i, j, 0]
            for k in range(60) :
                time = [i, j, k]
                time_str = str(i) + str(j) + str(k)
                if '3' in list(time_str) :
                    answer = answer + 1

    return answer

n=int(input())
print(solution(n))


# 시각 (p.113)
# 정수 N이 입력되면 00시 00분 00초부터 N시 59분 59초까지의 모든 시각 중에서 3이 하나라도 포함되는 모든 경우의 수를 구하는 프로그램
# 5를 입력하면 00시 00분 00초부터 5시 59분 59초까지의 모든 시각 중에서 3이 하나라도 포함되는 경우의 수를 출력 ⇒ 11475
# ==========================================================================
# 3중 반복문 사용해야 함
# 굳이 list 안쓰고 해도됨
# ' ' 안에 있는 건 String이다!!
