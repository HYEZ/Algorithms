# https://www.hackerrank.com/challenges/bigger-is-greater/problem
# 풀이) 구현



def biggerIsGreater(w):
    w = list(w)

    i = len(w) - 1
    while i > 0 and w[i-1] >= w[i]: # 가장 뒤부터 맨 처음 순서가 바뀐 곳 찾기
        i-=1

    print(i)

    if i <= 0: # 
        return 'no answer'
    
    j = len(w) - 1
    while w[j] <= w[i-1]: # w[i-1] 보다 큰거 찾기
        j -= 1

    w[i-1], w[j] = w[j], w[i-1] # 바꾸기

    w[i:] = w[len(w)-1:i-1:-1] # 바꿔준거부터는 다시 정렬!
    return ''.join(w)
    
    

w = 'dkhc'
# w = 'dcba'
# w = 'dhkc'
print(biggerIsGreater(w))