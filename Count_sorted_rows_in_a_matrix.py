a,b=map(int,input().split())
c=0
for i in range(a):
    arr=list(map(int,input().split()))
    x=sorted(arr)
    y=x[::-1]
    if arr==x or arr==y:
        c+=1
print(c)