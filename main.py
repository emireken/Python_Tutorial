# # Getting Input From Users
# user_name = input("Enter Your Name: ")
# user_age = input("Enter Your Age: ")
# print("Hi " + user_name + "!")
# print("You are " + user_age + "!")

# # Building a Basic Calculator
# var1 = float(input("Enter Number 1: "))
# var2 = float(input("Enter Number 2: "))
# result = var1 +var2
# print("Sum is " + str(result))

# # Lists
# lucky_numbers = [4, 8, 9, 15, 34, 35]
# friends = ["Alex", "Zebra", "Helen", "Kevin"]

# # List Functions
# friends.extend(lucky_numbers) #List Merge
# friends.append("Emir")  # Add Value to end of the list
# friends.insert(2,"Emir")  # Add Value to certain place
# friends.remove("Helen")  # Removes One Value from list
# friends.clear() # Clears the list
# friends.pop() # Removes Last Value from list
# friends.sort() # Sorts alphabetical or numerically
# friends2 = (friends.copy())
# friends2.reverse()
# print(friends)
# print(friends2)
# print(lucky_numbers)

# # Tuples
# coordinates = (4, 5)
# # coordinates[1] = 10
# print(coordinates)

# # Return Statement
# def sayHi(X):
#     print("Hello User")
#     print(X)
#     return X
#
# Y= sayHi(6)
# print(Y)

# # If Statements
# X = 6
# isTrue = True
#
# if(X==6 and X=="Six"):
#     print("6 or Six")
# elif (isTrue and X==6):
#     print(X)
# else:
#     print("Not Six")

# X = 5
# Y = 6
#
# if(X>Y):
#     print("X>Y")
# elif (X<Y):
#     print("X<Y")
# else:
#     print("X=Y")

# # If Statements & Comparisons
# def maxNum(X, Y, Z):
#     if X>=Y and X>=Z:
#         return X
#     elif Y>=X and Y>=Z:
#         return Y
#     else:
#         return Z
# input3 = (1,2,3,4)
# print(max(input3))
# print(maxNum(input3[0],input3[1],input3[2]))

# # Building a better Calculator
# num1 = float(input("Enter First Number:"))
# op = input("Enter Operator:")
# num2 = float(input("Enter Second Number"))
#
# if op=="-":
#     print(num1-num2)
# elif op=="+":
#     print(num1+num2)
# elif op=="/":
#     print(num1/num2)
# elif op=="*":
#     print(num1*num2)
# else:
#     print("Operator is invalid!")

# # Dictionaries
# monthConversions = dict(Jan="January", Feb="February", Mar="March", Apr="April", May="May", Jun="June", Jul="July",
#                         Aug="August", Sep="September", Oct="October", Nov="November", Dec="December")
# print(monthConversions['Apr'])
# print(monthConversions.get("Dec","Not Found!"))
# print(monthConversions.get("Emr","Not Found!"))

# # While Loop
# i=1
# while i<=10:
#     print(i)
#     i += 1
# print("Done with loop!")

# # Building a Guessing Game
# secretWord = "Emir"
# userWord= ""
# while userWord != secretWord:
#     userWord = input("Enter a Word: ")
#
# print("You Win!")


# Building a Guessing Game#2
import random
secretNumber = random.randint(1, 10)
userNumber = 0
userLive = 3
print("Pick a Number Between 1 and 10")
print(secretNumber)
while userNumber != secretNumber and (userLive > 0):
    userNumber = int(input("Enter a Number: "))
    if (userLive > 1) and (userNumber != secretNumber):
        userLive -= 1
        print("Try Again! " + str(userLive) + " Lives Remaining")
    elif (userLive >= 0) and (userNumber == secretNumber):
        print("You Win!")
    else:
        print("You Failed!")
        break
