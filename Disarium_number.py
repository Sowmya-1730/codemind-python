n=int(input())
l=0
q=n
q1=n
while n!=0:
    r=n%10
    l=l+1
    n=n//10
s=0
while q!=0:
    r=q%10
    s+=pow(r,l)
    l=l-1
    q=q//10
if s==q1:
    print("True")
else:
    print("False")