n,m=map(int,input().split())
mat=[]
for i in range(n):
    ls=list(map(int,input().split()))
    mat.append(ls)
a,b=0,0    
for i in range(len(mat)):
    if i%2:
        a+=sum(mat[i])
    else:
        b+=sum(mat[i])
print(b,a)    