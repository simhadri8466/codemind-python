r,c=map(int,input().split())
mat,mx,s=[],0,0
for i in range(r):mat.append(list(map(int,input().split())))
for i in range(r):
    for j in range(c):
        if mat[i][j]%2:
            s+=mat[i][j]
        else:
            mx+=mat[i][j]
        
print(mx,s)    