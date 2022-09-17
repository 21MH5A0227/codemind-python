n=int(input())
m=list(map(int,input().split()))
c=0
s=0
for i in range(len(m)):
    if(i%2==0):
        c+=m[i]
    else:
        s+=m[i]
if c-s==0:
    print("YES")
else:
    print("NO")