n=int(input())
l=list(map(int,input().split()))
e=0
o=0
for i in range (n):
    
    e+=l[i]
   
print(abs(e))