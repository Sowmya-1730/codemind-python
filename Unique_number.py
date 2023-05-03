n=int(input())
lst=[]
sm=0
while n>0:
    r=n%10
    sm+=1
    if r in lst:
        print("Not Unique Number")
        break
    lst.append(r)
    n=n//10
if len(lst)==sm:
    print("Unique Number")