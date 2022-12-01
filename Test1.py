num = int(input("Enter a number: "))
notprime = False
factors = [1]
count = 2

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
    print("The number of divisors are", count)
    print("The sum of the divisors are", Sum)

else:
    print(num, "is not a prime number")


