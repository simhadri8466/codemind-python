n=int(input())
a=list(map(int,input().split()))
b,c=map(int,input().split())
s=0
for i in a:
    if(i<b or i>c):
        s+=i
print(s)