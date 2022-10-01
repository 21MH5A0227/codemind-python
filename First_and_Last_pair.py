x=int(input())
l=list(map(int,input().split()))
if x%2!=0:
    l.insert((x//2)+1,0)
    x+=1
else:
    l=l
for i in range(x):
    if i!=x//2:
        print(l[i],l[(0-i+x-1)],end=' ')
    else:
        break