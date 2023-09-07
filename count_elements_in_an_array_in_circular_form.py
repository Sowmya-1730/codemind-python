n=int(input())
l = list(map(int,input().split()))
c=0
for i in range(len(l)):
    if(i==0):
        if((l[i+1]%2==0 and l[n-1]%2!=0) or (l[i+1]%2!=0 and l[n-1]%2==0)):
            c+=1
    elif(i==n-1):
        if((l[i-1]%2==0 and l[0]%2!=0) or(l[i-1]%2!=0 and l[0]%2==0)):
            c+=1
    else:
        if((l[i+1]%2==0 and l[i-1]%2!=0) or (l[i+1]%2!=0 and l[i-1]%2==0)):
            c+=1
print(c)
    