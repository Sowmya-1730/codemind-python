n=int(input())
lst=list(map(int,input().split()))
s=set(lst)
if len(s)==1:
    print(0)
else:
    c=mc=0
    for i in range(n):
        c=0
        for j in range(i,n):
            if(lst[i]==lst[j]):
                c+=1
                if(mc<c):
                    mc=c
    print(mc)