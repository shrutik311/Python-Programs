#Bubble Sort without using function

li = list(map(int,input().split()))
print(li)

for i in range(0,len(li)):
    for j in range(0,len(li)-i-1):
        if li[j] > li[j+1]:
            li[j],li[j+1] = li[j+1],li[j]

print(li)