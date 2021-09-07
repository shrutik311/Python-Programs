# Check whether String contains Duplicate elements or not

string = str(input())

newString = set(string)
print(newString)


if len(string) == len(newString):
    print("No Duplicate")
else:
    print("Duplicate")