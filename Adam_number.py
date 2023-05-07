n=int(input())
ns=n*n
s=0
s1=0
while n!=0:
    r=n%10
    s=s*10+r
    n=n//10
rs=s*s
while rs!=0:
    r=rs%10
    s1=s1*10+r
    rs=rs//10
if ns==s1:
    print("True")
else:
    print("False")
    