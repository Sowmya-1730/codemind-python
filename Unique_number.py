n=int(input())
l=0
q=n
lst=[]
while n>0:
    r=n%10
    l+=1
    n=n//10
while q>0:
    r1=q%10
    if r1 not in lst:
        lst.append(r1)
    else:
        lst.remove(r1)
    q=q//10
if len(lst)==l:
    print('Unique Number')
else:
    print('Not Unique Number')