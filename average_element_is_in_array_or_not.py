n=int(input())
s=0
a=list(map(int,input().split()))
for i in a:
    s+=i
d=s//n
if(d in a):
    print('True')
else:
    print('False')