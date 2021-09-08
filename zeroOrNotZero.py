n,m = map(int,input().split())

for i in range(n,m+1):
    if m >= 10 and m < 100:
        print("{:02d}".format(i),end=" ")
    elif m >= 100:
        print("{:03d}".format(i),end=" ")
    else:
        print(i,end=" ")