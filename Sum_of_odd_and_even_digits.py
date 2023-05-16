n=int(input())
l=list(map(int,input().split()))
s=0
s1=0
for i in range(0,len(l)):
    if i%2==0:
        s+=l[i]
    else:
        s1+=l[i]
if abs(s1-s)==0:
    print("YES")
else:
    print("NO")