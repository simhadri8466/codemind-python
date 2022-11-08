a,b,c=map(int,input().split())
C=2*a*b*c*512
k=C//1024
print(k,end='KB')