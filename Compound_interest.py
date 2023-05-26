p,r,t=map(int,input().split())
amnt=(p*(1+(r/100))**t)
print("%.2f" %amnt)