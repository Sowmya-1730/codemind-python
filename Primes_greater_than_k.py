n=int(input())
lst=list(map(int,input().split()))
k=int(input())
g=0
for i in lst:
    c=0
    for j in range(1,i+1):
        if i%j==0:
            c+=1
    if c==2:
        if i>=k:
            g+=1
print(g)