n=int(input())
lst=list(map(int,input().split()))
a,b=map(int,input().split())
s=0
for i in lst:
    if i not in range(a,b+1):
        s+=i
print(s)