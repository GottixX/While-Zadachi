a = input ("Enter a:")
b = input("Enter b:")
b = int(b)
a = int(a)

if a <= b:
    while a <= b:
        print(a)
        a = a + 1

else:
    while b <= a:
        print(b)
        b = b + 1
