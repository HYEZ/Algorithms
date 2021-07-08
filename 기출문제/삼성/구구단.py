# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&contestProbId=AXkcWgFa8sADFAS8&categoryId=AXkcWgFa8sADFAS8&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=3&pageSize=10&pageIndex=1
# 삼성 SW 역량 테스트
# 풀이) 그리디

T = int(input())
for test_case in range(1, T + 1):
    n = int(input())

    chk = 'No'
    for i in range(1, 10):
        if n % i == 0 and i * n//i == n and 1 <= n//i <= 9:
            chk = 'Yes'
            break
    
    print(f'#{test_case}', chk)

