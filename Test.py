def StartAgain():
    while True:
        try:
            num = int(input("Enter a number: "))
            notprime = False
            factors = [1]
            count = 2
            break;
        except ValueError:
            print ("Invalid input")

    if num > 1:
        for n in range(2, num):
            if num % n == 0:
                notprime = True
                factors.append(n)
                count += 1
        factors.append(num)
        if notprime == True:
            print(num, "is not a prime number")
        else:
            print(num, "is a prime number")
        print("The factors are", factors)
        Sum = sum(factors)
        print("The sum of the factors are", Sum)
        print("The number of divisors are", count)

    else:
        print(num, "is not a prime number")

    check = input("Do you want to quit or start again, enter Y for Yes: ")
    if check.upper() == "Y":
        StartAgain()
    else:
        print("Bye...")
    exit()


StartAgain()


