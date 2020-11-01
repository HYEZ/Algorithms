
# 재귀 (탑다운방식-하향식)
d = [0] * 100

def fibo(a):
    if a == 1 or a == 2:
        return 1

    if d[a] != 0:
        return d[a]
    
    d[a] = fibo(a-1) + fibo(a-2)
    return d[a]

print(fibo(99))

# 반복 (보텀업방식-상향식)
d = [0] * 100

d[1] = 1
d[2] = 1
n = 99

for i in range(3, n+1):
    d[i] = d[i-1] + d[i-2]

print(d[n])