a,b=map(int,input().split())
i=1
if(a,b):
    mini=a
else:
    mini=b
for i in range(1,mini+1):
    if(a%i==0 and b%i==0):
        hcf=i
print(hcf)