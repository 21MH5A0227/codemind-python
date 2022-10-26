a,b=map(int,input().split())
m=a*1
n=b*2
if(b%2==1 and a==0):
    print("NO")
elif((m+n)%2==0):
    print("YES")
else:
    print("NO")