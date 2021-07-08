# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV134DPqAA8CFAYh&categoryId=AV134DPqAA8CFAYh&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=&pageSize=10&pageIndex=1
# 삼성 SW 역량 테스트
# 풀이) 그리디


T = 10
for test_case in range(1, T + 1):
    n = int(input())
    arr = list(map(int, input().split()))
    cnt = 0
    for i in range(2, len(arr)-2):
        a = arr[i] - arr[i-1] 
        b = arr[i] - arr[i-2] 
        c = arr[i] - arr[i+1] 
        d = arr[i] - arr[i+2] 

        if a > 0 and b > 0 and c > 0 and d > 0:
            cnt += min(a, b, c, d)
            
    print(f'#{test_case}', cnt)