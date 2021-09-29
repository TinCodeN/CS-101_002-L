##
## CS 101 Lab
## Program: Loopandcondition.py
## Name: Tin Nguyen
## Email: tdnng2@umsystem.edu
## Date: Fall 2021
##
## PROBLEM : In this code help us output the number we think in our head after we put the right remainder
##
##
## ALGORITHM : The indencation for this loop need to at the line and order otherwise the loop is not understand
##      
##    
##
##  
##
##
##
#printing welcome Message
print("Welcome to Flarsheim Guesser!")
# a variable to store user choice
choice='y'

# a while loop run until the user is N or n
while(choice == 'Y' or choice == 'y'):
    #Asking user to imagine a number
    print("\nPlease think of a number between and including 1 and 100.")
  
    #variables to remainder of number with 3,5,7
    Three_Remainder=0
    Five_Remainder=0
    Seven_Remainder=0
  
    #reading remainder when the number is divided by 3
    Three_Remainder = int(input("\nWhat is the remainder when your number is divided by 3 ?"))
    # a while loop to ask input continuously until user enter correct input
    while(Three_Remainder < 0 or Three_Remainder >= 3):
        #if the entered remainder is negative
        if Three_Remainder < 0 :
            #printing error message
            print("The value entered must be 0 or greater")
        #if the entered number is greater than or equal to 3
        elif Three_Remainder >= 3 :
            #printing the error message
            print("The value entered must be less than 3")
  
        #reading remainder from user again
        Three_Remainder = int(input("What is the remainder when your number is divided by 3 ?"))
  
    #reading remainder when the number is divided by 5
    Five_Remainder = int(input("\nWhat is the remainder when your number is divided by 5 ?"))
    # a while loop to ask input continuously until user enter correct input
    while(Five_Remainder < 0 or Five_Remainder >= 5):
        #if the entered remainder is negative
        if Five_Remainder < 0 :
            #printing error message
            print("The value entered must be 0 or greater")
        #if the entered number is greater than or equal to 5
        elif Five_Remainder >= 5 :
            #printing the error message
            print("The value entered must be less than 5")
  
        #reading remainder from user again
        Five_Remainder = int(input("What is the remainder when your number is divided by 5 ?"))
  
    #reading remainder when the number is divided by 7
    Seven_Remainder = int(input("\nWhat is the remainder when your number is divided by 7 ?"))
    # a while loop to ask input continuously until user enter correct input
    while(Seven_Remainder < 0 or Seven_Remainder >= 7 ):
        #if the entered remainder is negative
        if Seven_Remainder < 0 :
            #printing error message
            print("The value entered must be 0 or greater")
        #if the entered number is greater than 7
        elif Seven_Remainder >= 7 :
            #printing the error message
            print("The value entered must be less than 7")
  
        #reading remainder from user again
        Seven_Remainder = int(input("What is the remainder when your number is divided by 7 ?"))
  
  
    for i in range(1,101):
        if(i%3 == Three_Remainder and i%5 == Five_Remainder and i%7 == Seven_Remainder):
            print("Your number was",i)
            print("How amazing is that?\n")
  
  
    choice=input("Do you want to play again? Y to continue,N to quit ==>")
    while(choice != 'Y' and choice != 'N' and choice != 'y' and choice != 'n' ):
        choice=input("Do you want to play again? Y to continue,N to quit ==>")
