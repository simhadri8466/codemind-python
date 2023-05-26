n = int(input())
lst = list(map(int, input().split()))
lst.insert(0, lst[-1])
lst.append(lst[1])
c = 0
for i in range(1, n+2-1):
    if lst[i-1]%2 == 0 and lst[i+1]%2 == 1 or lst[i-1]%2 == 1 and lst[i+1]%2 == 0:
        c = c+1
print(c)