def prime(n):
    if n==1:
        return 0
    elif n==2:
        return 1
    for i in range(2,int(n*0.5)+2):
        if n%i==0:
            return 0
    return 1
a=int(input())
b=int(input())
for i in range(a,b+1):
    if prime(i):
        print(i)
