n=int(input())
l=list(map(int,input().split()))
a,b=map(int,input().split())
big=max(a,b)
small=min(a,b)
s=0
for i in range(len(l)):
    if l[i]<small or l[i]>big:
        s=s+l[i]
print(s)