n=int(input())
x=list(map(int,input().split()))
d=x[::-1]
for i in d:
    if i%2==0:
        print(i)
        break