n=int(input())
c=[]
a=[]
k=list(map(int,input().split()))
for i in range(len(k)):
    if(k[i]%2==0):
        c.append(k[i])
    else:
        a.append(k[i])
print(*(a+c))