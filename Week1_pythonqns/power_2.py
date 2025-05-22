n = int(input("Enter a number: "))
if n<= 0:
    print(n, "is NOT a power of 2")
else:
    while n%2==0:
        n= n//2
    if n== 1:
        print("It is a power of 2")
    else:
        print("It is not a power of 2")
