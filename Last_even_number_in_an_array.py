n=int(input())
l=list(map(int,input().split()))
lst=[]
for i in l:
    if i%2==0:
        lst.append(i)
print(lst[-1])       