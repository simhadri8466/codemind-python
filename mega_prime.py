n=int(input())
c=0
x=0
a=0
for i in range (1,n+1,1):
    if(n%i==0):
        c+=1
if(c==2):
    while(n!=0):
        d=n%10
        n=n//10
        s=0
        for j in range (1,d+1,1):
            if(d%j==0):
                s+=1
        if(s==2):
            x+=1
        a+=1
if(x==a and c==2):
    print('Mega Prime')
elif(c>2 or x!=a):
    print('Not Mega Prime')