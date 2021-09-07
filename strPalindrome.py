# Check whether string is palidrome or not

string = str(input())

newString = string[::-1]

if string == newString:
    print("String is Palindrome...")
else:
    print("String is Not Palindrome...")