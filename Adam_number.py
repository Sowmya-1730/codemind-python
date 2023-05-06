n=int(input())
ns=n*n
s=0
s1=0
while n!=0:
    r=n%10
    s=s*10+r
    n=n//10
nr=s*s
nrs=nr
while nr!=0:
    r=nr%10
    s1=s1*10+r
    nr=nr//10
if ns==s1:
    print("True")
else:
    print("False")