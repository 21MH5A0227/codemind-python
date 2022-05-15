n=int(input())
es=0
os=0
x=list(map(int,input().split()))
for i in range(len(x)):
    if (x[i]%2==0):
        es=es+x[i]
    else:
        os=os+x[i]
big=max(es,os)
small=min(es,os)
print(abs(big-small))
