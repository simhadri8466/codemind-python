n,m=map(int,input().split())
mat=[]
for i in range(n):
    ls=list(map(int,input().split()))
    mat.append(ls)
mx=0
for i in mat:
    mx=max(mx,sum(i))
k=[[0 for i in range(n)] for j in range(m)]
for i in range(n):
    for j in range(m):
        k[j][i]=mat[i][j]
for i in k:
    mx=max(mx,sum(i))
print(mx)    