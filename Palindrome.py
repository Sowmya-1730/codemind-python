n=int(input())
sm=0
q=n
while n!=0:
    r=n%10
    sm=sm*10+r
    n=n//10
if sm==q:
    print("True")
else:
    print("False")