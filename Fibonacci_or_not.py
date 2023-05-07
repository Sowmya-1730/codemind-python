n=int(input())
a=0
b=1
lst=[]
for i in range(1,n+1):
    lst.append(a)
    c=a+b
    a=b
    b=c
if n in lst:
    print("True")
else:
    print("False")