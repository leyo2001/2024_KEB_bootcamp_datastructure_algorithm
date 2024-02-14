def fibo(n):
    l = [0,1]

    for _ in range(n-1):
        l.append(l[len(l)-1] + l[len(l)-2])
    return l[n]

def fibo_r(n):
    if n==0:
        return 0
    elif n==1:
        return 1

    return fibo_r(n-1) + fibo_r(n-2)

for i in range(40):
    print(i)
    print(fibo(i))

    print(i)
    print(fibo_r(i))


