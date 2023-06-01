n=int(input())
while(len(str(n))!=1):
        s=0
        while(n):
                s+=(n%10)
                n//=10
        n=s
print(n)
