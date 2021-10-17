########################################################################
##
## CS 101 Lab
## Program Lab Week 7
## Date : Fall 2021
## Name: Tin Nguyen
## Email: tdnng2@umsystem.edu
##
## PROBLEM : The Caesar Cipher is an encryption/decryption method that shifts the alphabet.  
##           For instance, if you have a cipher that shifts by 1, A would become B, 
##           B would become C, Z would wrap and become A.
##           To decrypt that cipher you simply shift by -1.  
##           It is a very simple cipher that is easily broken
##
## ALGORITHM : 
## 1. We initilize a variable equal to one, which then run the while loop
## 2. Print menu function which show user option, we take input from the user 
## 3. Depending on user choice either function encrypt or decrypt call 
## 4. Step two to three will repeat until user enter 'q' which end the loop
##
## 
##
## 
##
#######################################################################

def encrypt(text,s): 
    result = "" 
    for i in range(len(text)): 
        char = text[i] 
  
        if (char.isupper()): 
            result += chr((ord(char) + s-65) % 26 + 65) 
  
        elif(char.islower()): 
            result += chr((ord(char) + s - 97) % 26 + 97) 
        else:
            result+= char
  
    return result 
    
def decrypt(text,s): 
    result = "" 
 
    for i in range(len(text)): 
        char = text[i] 
        if (char.isupper()): 
            result += chr((ord(char) - s-65) % 26 + 65) 
  
        elif(char.islower()): 
            result += chr((ord(char) - s - 97) % 26 + 97) 
        
        else:
            result+= char
            
    return result 
    
def printMenu():
    print("\nMain Menu")
    print("1). Encode a String")
    print("2). Decode a String")
    print("Q).Quit")
    print("Enter your selection ==>",end='')

choice = 1

while(choice !=3):
    printMenu()
    choice = input()
    if choice =='1':
        print("\nEnter brief text to encrypt : ",end='')
        text = input()
        print("\nEnter the number to shift letters by: ",end='')
        shift = int(input())
        ans = encrypt(text,shift)
        print("\nEncrypted : ",ans)
    elif choice == '2':
        print("\nEnter brief text to decrypt : ",end='')
        text = input()
        print("\nEnter the number to shift letters by: ",end='')
        shift = int(input())
        ans = decrypt(text,shift)
        print("\nDecrypted : ",ans)
    elif choice == 'Q':
        break
    else:
        print("\nWrong Input")