# #### Practice if/else statements

# #####Loyalty Card
# loyalty = input("Do you have a loyalty card? Y/N: ")
# if loyalty =="Y":
#   print("Please scan")
# #elif loyalty == "N":
#   #print("Do you want one?")
# else:
#   print("Do you want one? Y/N: ")

# #########################
# ##Payment


# #At register, asks if paying with card, cash or coupon
# #if paying with cash - print insert cash
# #if paying with card - print insert card
# #if paying with coupon - print insert coupon
# payment = input("Card, cash or coupon")
# if payment == "card":
#   print("insert card")
# elif payment == "cash":
#   print("insert cash")

#######################################
####Program to see if someone can get a driver's license
#Ask the user their age - make sure it's a number
# If they're 17 or over (>=), display a messge telling them they're eligible
#Or else they see a message saying that they aren't eligible

############################
# age = int(input("What age are you? "))
# if age >= 17:
#   print("You are eligible!")
# # elif age < 17:
# #   print("Not eligible")
# else:
#   print("not eligible")
##################################
#Print an introductory message saying welcome to the ticket machine
#Let the user enter A, B or C
#if they choose A, they get a message saying that they get a free ticket to Dundrum
#if they choose B, free ticket to the Square
#If they choose C, free ticket to Broombridge
#if they choose something else, they get a message telling them there's an error

####################################
## While loops
## A while loop keeps repeating while the condition is true and stops when it is false. A while loop could keep going forever.

## create a variable called counter and initialise it - give it a starting value
# counter = 0

# ## set the condition for the loop, while this is true the indented part runs
# while counter < 7:
#    ## while the counter value is less than 7
#   print(counter)  ## print the value of the counter variable
#   counter +=1     ## +=1 lets the counter variable increase by 1 each time the loop runs. It will run while the value of counter is less than 7
# print("The loop is finished!") ##when the value gets above 6, this will happen. This is the point the where the condition is not TRUE anymore.

## Create a loop to display the numbers from 1 - 100

# counter = 0
# while counter < 101:
#   print(counter)
#   counter +=1
# print("ta da!")
#################################
## Create a loop to display the numbers from 100 down to 1

# counter = 100
# while counter > 0:
#   print(counter)
#   counter -= 1
# print("Ta da!")

## To set a permanent loop - often used in games
## set the condition to True - this means the loop will continuously run 
# while True:
#   print("Looping forever")

## We can use loops to check for errors. Before, our code broke or ignored a problem if the input was incorrect or of the wrong type. Eg. the user enters a word when we want a number. We need a loop if someone enters the wrong password - it lets them try to enter their password correctly
#################################
## Example - entering grades

# ##create variable to let user enter their grade
# percentage = float(input("Enter your grade mark between 0 and 100: "))
# ## create a while loop to fix the issue of the user entering the wrong thing
# while percentage < 0 or percentage > 100:
#   print("Error, mark outside the accepted range")
#   percentage = float(input("Enter your grade again: "))
# ## while the value is in the accepted range print the following message
# print("You entered", percentage,"%")
# # ## add a condition that if the mark is below 50% a message displays telling them to study more, otherwise the message saya well done.
# if percentage < 50:
#   print("You need to study more")
# else:
#   print("Well done!")
# # #####################
# ## Ending a loop with a condition - used in menus a lot - if the user presses a certain value (sentinel value) the loop stops 

# ## Create a program where the user enters a list of numbers to be added together. If they press 0 the loop ends and the total is displayed. Here 0 is the sentinel value 
##########################
# # ## Create a varibale so the user can enter a number
# num = int(input("Enter a number. To end press 0: "))
# # ## create a variable that will add the numbers entered together
# total = num

# # ##create the condition of the loop -- if the user doesn't press 0, it asks the user to enter a number and it adds that number to the total, until they press 0. 
# while num != 0:
#   num = int(input("Enter a number. To end press 0: "))
#   total += num
# ## if they press 0 this message is displayed and the numbers that have been added together are displayed
# print("The total is", total)

#######################

#######################################
# ## Write a program to add up the numbers to 1000 inclusive. Use a while loop.

# counter = 0
# total = counter
# while counter < 1001:
#   counter +=1
#   total += counter
# print(total)

# ###Add the numbers between 1000 and 1500
# counter = 1000
# total = counter
# while counter < 1501:
#   counter += 1
#   total += counter
# print(total)
################################
