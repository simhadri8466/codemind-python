n=int(input())
a=list(map(int,input().split()))
for i in a:
    x=str(i)
    p=len(x)
    if(i<0):
        p-=1
    print(p,end=' ')