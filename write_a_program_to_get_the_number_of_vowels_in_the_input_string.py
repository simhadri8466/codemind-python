k=input()
a="aeiouAEIOU"
z=0
for i in range(0,len(k)):
    if k[i] in a:
        z+=1
print(z)