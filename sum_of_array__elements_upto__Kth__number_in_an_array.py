n=int(input())
l=list(map(int,input().split()))
k=int(input())
s=0
for i in range(n):
    if l[i]>k:
        break
    else:
        s=s+l[i]
print(s)