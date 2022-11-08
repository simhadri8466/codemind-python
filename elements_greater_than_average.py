n=int(input())
l=[int(i) for i in input().split()]
sum=0
count=0
for ele in l:
    sum=sum+ele
avg=sum//len(l)
for ele in l:
    if ele>=avg:
        count+=1
print(count)