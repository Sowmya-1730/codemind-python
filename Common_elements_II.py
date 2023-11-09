a,b=map(int,input().split())
l1=list(map(int,input().split()))
l2=list(map(int,input().split()))
res=[]
for i in range(a):
    if l1[i] not in l2 and l1.count(l1[i])==1:
        res.append(l1[i])
for j in range(b):
    if l2[j] not in l1 and l2.count(l2[j])==1:
        res.append(l2[j])
print(*res)