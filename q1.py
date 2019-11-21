n,m,q=map(int,input("PLEASE ENTER N,M,Q : ").split())
gc=[0]*n
for i in range(0,m):
    x,y=map(int,input("PLEASE ENTER X,Y : ").split())
    ma=max(x,y)
    if(x>=y):
        gc[ma]+=1
    else:
        gc[ma-1]+=1
for i in range(1,n):
    gc[i]+=gc[i-1]
for i in range(q):
    t=int(input("ENTER SECONDS: "))
    if t>n:
        res=(2*t)**2-m
    else:
        res=(2*t)**2-gc[t-1]
    print(res)
