from math import sqrt
running = True
while running:
    test = input("Enter any integer greater than 1 (enter exit to stop): ")
    if test == "exit":
        break
    checking = True
    while checking:
        # checks if user entered an integer
        try:
            test = int(test)
        except TypeError:
            print("Error: User did not enter an integer")
            break
        except ValueError:
            print("Error: User did not enter an integer")
            break

        # checks if user entered an integer greater than 1
        if test < 2:
            print("Error: User did not enter an integer greater than 1")
            break

        testing = True
        isPrime = True
        while testing:
            n = 2
            while n <= sqrt(test):
                if test % n == 0:
                    isPrime = False
                    testing = False
                    break
                else:
                    n += 1
            break
        if isPrime:
            print(str(test) + " is prime.")
            break
        else:
            print(str(test) + " is not prime.")
            break
