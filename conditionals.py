# conditionals 

# compiler : changes the code so the CPU can understand

# Boolean expressions & conditions

# you need to be age > 18
# you also need to have parental approval
# it costs $15 to get the game

# Return function
# store it
age = input("How old are you?") # returns a string
actual_age = int(age) # convert to number

approval = input("Do you have parental approval (Y / N)?") 

money = input("How much money do you have?")
actual_money = int(money)

# if actual_age <= 18:
#     print("Can't play")
# elif approval == 'N':
#     print("Can't play")
# elif actual_money < 15:
#     print("Can't play")
# else:
#     print("Can play")

# if actual_age > 18 and approval == 'Y' and actual_money >= 15:
#     print("Can play")
# else:
#     print("Can't play")


# if actual_age <= 18 or approval == 'N' or actual_money < 15:
#     print("Can't play")
# else:
#     print("Can play")
