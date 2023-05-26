r,c=map(int,input().split())
mat,mx,s=[],0,0
for i in range(r):mat.append(list(map(int,input().split())))
for i in mat:
    s+=sum(i)
print(s)    