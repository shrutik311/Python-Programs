# Find the factorial of given number

def fact(num):
    if num == 1:
        return 1
    else:
        return num * fact(num-1)

num = int(input())

# fact = 1
# for i in range(1,num+1):
#     fact = fact * i

# print(fact)

result = fact(num)
print(result)


