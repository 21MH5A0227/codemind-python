import math
def fun(x):
    if x==1:
        return False
    for i in range(2,int(math.sqrt(x))+1):
        if x%i==0:
            return False
    return True
n=int(input())
m=int(input())
c=n+m
t=c
while True:
    c=c+1
    if fun(c):
        break
print(c-t)