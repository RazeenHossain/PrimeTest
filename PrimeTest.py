test = input("Enter any integer greater than 1: ")

# checks if user entered an integer
try:
    test = int(test)
except TypeError:
    print("Error: user did not enter an integer")
    exit()
except ValueError:
    print("Error: user did not enter an integer")
    exit()

# checks if user entered an integer greater than 1
if test < 2:
    print("Error: user did not enter an integer greater than 1")
    exit()

n = 2
while n < test:
    quotient = test / n
    if quotient == round(quotient):
        print(str(test) + " is not prime")
        exit()
    else:
        n += 1
print(str(test) + " is prime.")
exit()