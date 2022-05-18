n=int(input())
t=n
s=n*n
k=0
c=0
v=0
while n!=0:
    r=n%10
    k=k*10+r
    n=n//10
w=k*k
while w!=0:
    r=w%10
    c=c*10+r
    w=w//10
if s==c:
    print("True")
else:
    print("False")
    
