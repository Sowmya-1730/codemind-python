def add(n):
    while n>=10:
        t=0
        while n>0:
            t+=n%10
            n=n//10
        n=t
    return n
n=int(input())
print(add(n))