a = input ("Enter a:")
b = input("Enter b:")
b = int(b)
a = int(a)

while a <= b:
    if a % 2 == 0:
        print(str(a) + " is odd")
    else:
        print(str(a) + " is even")

    a = a + 1
