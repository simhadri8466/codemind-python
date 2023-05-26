r,c=map(int,input().split())
mat,mx,s=[],[],0
for i in range(r):mat.append(list(map(int,input().split())))
for i in mat:
    mx.append(sum(i))
print(*mx)    