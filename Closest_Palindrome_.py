def pal(x):
    a=x
    s=0
    while x>0:
        r=x%10
        s=s*10+r
        x=x//10
    if a==s:
        return 1
    else:
        return 0
def npal(x):
    while pal(x)==0:
        x=x+1
    return x
def ppal(x):
    while pal(x)==0:
        x=x-1
    return x
x=int(input())
a=ppal(x)
b=npal(x)
if pal(x)==1:
    print(ppal(x-1),npal(x+1))
elif x-a<b-x:
    print(a)
elif x-a>b-x:
    print(b)
elif x-a==b-x:
    print(a,b)
