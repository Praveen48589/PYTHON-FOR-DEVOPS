# num = int(input("Enter a number you want to create a table for : "))


#  String formatting by "f" :

# for i in range(1,11):
#     print(f" {num} * {i} = {num*i}")


choice = input("Enter the choice (press q to quit) : ")

while choice != "q":
    num = int(input("Enter a number you want to create a table for : "))
    for i in range(1,11):
        print(f" {num} * {i} = {num*i}")
    choice = input("Enter the choice (press q to quit) : ")