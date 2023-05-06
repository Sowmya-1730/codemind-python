import math
n=int(input())
l=0
sm=0
nn=n
q=n
while n!=0:
    r=n%10
    l+=1
    n=n//10
while q!=0:
    r=q%10
    s=pow(r,l)
    sm+=s
    l=l-1
    q=q//10
if sm==nn:
    print("True")
else:
    print("False")