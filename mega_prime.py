def is_prime(n):
    fc=0
    for i in range(1,n+1):
        if n%i==0:
            fc=fc+1
    if fc==2:
        return True
    else:
        return False
a=int(input())
mega_prime=True
if is_prime(a)==True:
    while a>0:
        r=a%10
        if is_prime(r)==False:
            mega_prime=False
            break
        a=a//10
    if mega_prime==True:
        print("Mega Prime")
    else:
        print("Not Mega Prime")
else:
    print("Not Mega Prime")
        