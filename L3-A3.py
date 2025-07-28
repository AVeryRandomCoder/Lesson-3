num = int(input("Enter number to check: "))

if num>50:
    print("Number is bigger then 50")
    if num%2==0:
        print("And it is even too")
    else:
        print("And it is odd too")
else:
    print("Number is smaller then 50")
    if num % 3 == 0:
        print("And it is divisible by 3")
    else:
        print("It can't be divided by 3")
    if num < 0:
        Pos = -num
        print("And it is even now: ", Pos)