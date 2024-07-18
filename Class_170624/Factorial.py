fact = int(input("Enter number:"))
factorial = 1
for i in range(1, fact + 1):
    factorial = factorial * i

print("Using for loop:", factorial)

factNumber = 1
while fact > 0:
    factNumber = factNumber * fact
    fact = fact - 1

print("Using while loop:", factorial)
