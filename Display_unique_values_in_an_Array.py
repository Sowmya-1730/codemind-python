n=int(input())
l=list(map(int,input().split()))
x=[]
for i in l:
    if i not in x:
        x.append(i)
    else:
        x.remove(i)
y=sorted(x)
for i in y:
    print(i,end=' ')
if len(x)==0:
    print("-1")