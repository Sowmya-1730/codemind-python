n=int(input())
lst=[]
while n!=0:
    r=n%10
    lst.append(r)
    n=n//10
print(max(lst))