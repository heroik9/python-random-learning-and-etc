list = []
x = 1

while x < 100:

    if x % 3 == 0 and x % 5 == 0:
        list.append("fizzbuzz")
    elif x % 3 == 0:
        list.append("fizz")
    elif x % 5 == 0:
        list.append("buzz")
    else:
        list.append(x)

    x += 1

print(list)