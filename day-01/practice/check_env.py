# Get the environment variable and print it out

env = input("Enter the environment you want to deploy  ")


# Conditional statemrnt
if (env == "prod"):
    print("Don`t deploy to production on friday")
elif env == "staging":
    print("Take to backup && Test well")
else: 
    print("Safe to deploy any day except friday")

# a = int(input("Enter your first number: "))
# b = int(input("Enter your second number: "))

# print(type(a))
# print(type(b))

# print("The sum of the two numbers is: ", a + b)
# print("The difference of the two numbers is: ", a - b)
# print("The product of the two numbers is: ", a * b)
# print("The division of the two numbers is: ", a / b)