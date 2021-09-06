# Find the Fibbonaice Series

num = int(input())

num1 = 0
num2 = 1
print(num1,end=" ")
for i in range(0,num-1):
    res = num1 + num2
    num1 = num2
    num2 = res

    print(res,end=" ")
    