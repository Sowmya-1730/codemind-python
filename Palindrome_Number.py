n=int(input())
for i in range(1,n+1):
    x=int(input())
    s=0
    q=x
    while x!=0:
        r=x%10
        s=s*10+r
        x=x//10
    if s==q:
        print("True")
    else:
        print("False")
