s=input()
c=0
for i in s:
    if i not in ' abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ':
        c+=1
print(c)