p=input()
j=input()
k=0
for i in range(0,len(p)):
    if p[i]==j:
        k=1
        print("True")
        print(i)
        break
if k==0:
    print("False")