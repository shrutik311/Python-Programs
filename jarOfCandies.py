N = 10
quantity = int(input())

if quantity > N:
    print("INVALID INPUT")
else:
    print("Number of Candies Sold:",quantity)
    N = N - quantity
    print("Number of Candies available:",N)