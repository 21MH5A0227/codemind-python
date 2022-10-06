a,b=map(int,input().split())
l=[]
for i in range(a):
    l1=list(map(int,input().split()))
    l.append(l1)
s=0
for i in range(b):
    for j in range(a):
        if i==j or i+j==b-1:
            s=s+l[i][j]
print(s)