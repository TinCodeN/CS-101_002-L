########################################################################
##
## CS 101 Lab
## Program Lab Week 6
## Name: Tin Nguyen
## Email: tdnng2@umsystem.edu
##
## PROBLEM : Strings
##
## ALGORITHM :
## 1. Write out the algorit
##
## ERROR HANDLING:
## Any Special Error handling to be noted. Wager not less than 0. etc
##
## 
##
#######################################################################
# import statement

# # functions

def get_school(library_card):
    if library_card[5] == '1':
        return "School of Computing and Engineering SCE"
    elif library_card[5] == '2':
        return "School of Law"
    elif library_card[5] == '3':
        return "College of Arts and Sciences"
    else:
        return "Invalid School"
  
def get_grade (library_card) :
    if library_card[6] == '1':
        return "Freshman"
    elif library_card[6] == '2':
        return "Sophomore"
    elif library_card[6] == '3':
        return "Junior"
    elif library_card[6] == '4':
        return "Senior"
    else:
        return "Invalid Grade"

def character_value (c):
    value = ord(c)
    if (value >= 48 and value<=57):
        return value - 48
    elif (value >= 65 and value<=90):
        return value - 65
  
def get_check_digit (library_card):
    sum = 0
    for i in range(len(library_card)):
        value = character_value(library_card[i])
        sum += value * (i+1)
    return sum % 10
  
def verify_check_digit (library_card):
    #check length of string
    if len(library_card) != 10:
        return (False,"The length of the number given must be 10")
  
    #check first five characters
    for i in range(5):
        if library_card[i] < 'A' or library_card[i] > 'Z':
            msg = "The first 5 characters must be A-Z, the invalid character is at index " \
            + str(i) +" is " + library_card[i]
            return (False, msg)
  
    #check charactersn at index 7-9
    for i in range(7,10):
        if library_card[i] < '0' or library_card[i] > '9':
            msg = "The last 3 characters must be 0-9, the invalid character is at index "\
                    + str(i) +" is " + library_card[i]
            return (False, msg)
  
    #check character at index 5
    if (library_card[5] != '1' and library_card[5] != '2' and library_card[5] != '3'):
            return (False, "The sixth character must be 1,2 or 3")
  
    #check character at index 6
    if (library_card[6] != '1' and library_card[6] != '2' \
        and library_card[6] != '3' and library_card[6] != '4'):
            return (False, "The seventh character must be 1,2,3 or 4")
  
    calculated_value = get_check_digit(library_card)
    given_value = int(library_card[9])
    if given_value != calculated_value:
        msg = "Check digit " + str(given_value) + " does not match calculated value " \
                + str(calculated_value)
        return (False,msg)
  
    return (True,"Library card is valid.")


def main():
    while(1):
        library_card = input("Enter Library Card. Hit Enter to Exit ==> ")
        (is_valid,msg) = verify_check_digit(library_card)
  
        if is_valid == True:
            print(msg)
            print("The card belongs to a student in " + get_school(library_card))
            print("The card belongs to a " + get_grade(library_card))
  
        else:
            print("Library card is invalid.")
            print(msg)
  
if __name__=="__main__":
    main()


