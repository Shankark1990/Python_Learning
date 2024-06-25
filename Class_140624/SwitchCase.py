for a in range(0, 10):
    print(a)
    if a == 5:
        break

print("Outside of for loop..")

for b in reversed(range(0, 10)):
    print(b)

for c in range(10):
    if c == 5:
        pass
    else:
        print(c)

for i in range(10):
    if i % 3 == 0:
        print(i)
