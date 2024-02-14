import time
l = [0,1]
cnt = 1
def count(f):
    def wrapper(n):
        global cnt
        r = f(n)
        print(f"{cnt}")
        cnt+=1
        return r

    return wrapper


@count
def fibo(n):

    for _ in range(n-1):
        l.append(l[len(l)-1] + l[len(l)-2])
    return l[n]

@count
def fibo_r(n):
    if n==0:
        return 0
    elif n==1:
        return 1

    return fibo_r(n-1) + fibo_r(n-2)


print(fibo_r(2))
