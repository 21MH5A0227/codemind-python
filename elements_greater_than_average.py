num=int(input())
l=list(map(int,input().split()))
c=0
avg=sum(l)//num
for i in range(len(l)):
    if(l[i]>=avg):
        c+=1
print(c)