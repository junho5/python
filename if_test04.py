N = 120
i = 1
cnt = 0
while i<=N:
    if N % i == 0:
        cnt += 1
        print(i)
    i += 1
print("{}의 약수는 총 {}개입니다.".format(N,cnt))