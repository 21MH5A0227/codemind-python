import math
def fun(x):
    if x==1:
        return False
    for i in range(2,int(math.sqrt(x))+1):
        if x%i==0:
            return False
    return True
n=int(input())
l=[]
for i in range(1,n+1):
    if fun(i):
        continue
    else:
        if n%i==0:
            l.append(i)
print(len(l))