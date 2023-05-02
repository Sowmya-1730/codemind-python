a,b=map(int,input().split())
for j in range(1,b+1):
    if j%2!=0:
        print("%d x %d = %d"%(a,j,a*j))