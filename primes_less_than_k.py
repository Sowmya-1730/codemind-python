n=int(input())
lst=list(map(int,input().split()))
k=int(input())
l=0
for i in lst:
    c=0
    for j in range(2,i+1):
        if i%j==0:
            c+=1
    if c==1:
        if i<=k:
            l+=1
print(l)