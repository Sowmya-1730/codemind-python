n=int(input())
a=n**2
sm=0
while a>0:
    r=a%10
    sm+=r
    a=a//10
if sm==n:
    print("Neon Number")
else:
    print("Not Neon Number")