n=int(input())
sm=0
pr=1
while n>0:
    r=n%10
    sm+=r
    pr*=r
    n=n//10
if sm==pr:
    print("Spy Number")
else:
    print("Not Spy Number")