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

# # checks if user actually entered an integer greater than 1
# # doesn't check if user entered an integer
#
# if test < 2:
#     print("Learn to read directions first.")
#     exit()

# n = 2
# while n < test:
#     quotient = test / int(n)
#     if isinstance(quotient, int):
#         print(str(test) + " is not prime.")
#         exit()
#     else:
#         n += 1
# print(str(test) + " is prime.")
# exit()
