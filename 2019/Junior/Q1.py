apples = 0
bananas = 0

for x in reversed(range(1, 7)):
    if x > 3:
        apples += int(input())*(x-3)
    else:
        bananas += int(input())*x

if apples > bananas:
    print("A")
elif bananas > apples:
    print("B")
else:
    print("T")
