n=int(input())
a=list(map(int,input().split()))
s,sa=0,0
for i in range(0,n//2):
    s+=a[i]
for i in range(n//2,n):
    sa+=a[i]
print(s)
print(sa)