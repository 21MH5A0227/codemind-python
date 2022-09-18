n=int(input())
for i in range(n):
    a=int(input())
    t=a
    s=0
    while (a!=0):
        r=a%10
        s=s*10+r
        a=a//10
    if s==t:
        print(True)
    else:
        print(False)