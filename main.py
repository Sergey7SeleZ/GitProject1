
print("Hello git!")

def f2(x):
    return x ** 2

print(f2(4))

def f3(x):
    return x ** 3

def f4(x):
    x += 1
    print(x ** 2 + x * 2)
    x -= 3
    print (x ** 3)

def f4(x):
    x += 1
    print(x ** 2 + x * 2)

f4(12)
f4(f3(5))