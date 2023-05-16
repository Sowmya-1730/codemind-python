l=list(map(int,input().split(',')))
x=[]
for i in range(len(l)):
    s=0
    for j in range(1,(l[i]+1)):
        if l[i]%j==0:
            s+=j
    if s in l:
        x.append(l[i])
y=sorted(x)
for i in y:
    print(i,end=' ')
if len(y)==0:
    print('-1')