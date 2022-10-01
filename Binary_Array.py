num=int(input())
l=list(map(int,input().split()))
a=max(l)
if(a==0 or a==1):
    print(True)
else:
    print(False)