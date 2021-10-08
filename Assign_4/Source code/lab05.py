########################################################################
##
## CS 101 Lab
## Program Lab Week 5
## Name: Tin Nguyen
## Email: tdnng2@umsystem.edu
##
## PROBLEM : Functions
##
## ALGORITHM :
## 1. Write out the algorit
##
## ERROR HANDLING:
## Any Special Error handling to be noted. Wager not less than 0. etc
##
## 
##
########################################################################

#import modules needed
import random
#Ask the user if they want to play again
def play_again() -> bool: #play again function
  user_val = 1
  while user_val == 1:
    play_again = input('Do you want to play again? ==> ') 
    if play_again == "NO" or play_again == "N":
      user_val = 0
      return False
    elif play_again == "YES" or play_again == "Y":
        user_val = 0
        return True
    else:
        print("You must enter Y/YES/N/NO to continue. Please try again")


#Input the function
def get_wager (bank: int) -> int: #get wager function
  user_val = 1
  while user_val == 1:
    wager1 = int(input("How many chips do you want to wager? ==> "))
    if wager1 <= 0:
        print("The wager amount must be greater than 0. Please enter again.")
    elif wager1 > bank:
        print("The wager amount cannot be greater than how much you have.",
bank)
    else:
        user_val = 0
        return wager1

# Get random reels to play
def get_slot_results() -> tuple: #get slot function
  ''' Returns the result of the slot pull ''' 
  slot1 = random.randint(1,10) #import random 
  slot2 = random.randint(1,10) #import random 
  slot3 = random.randint(1,10) #import random 
  return slot1, slot2, slot3


def get_matches(reela, reelb, reelc) -> int:
  result = 0
  if slot1 == slot2 == slot3:
    result = 3
  elif slot1 == slot2 and slot1 != slot3:
    result = 2
  elif slot1 == slot3 and slot1 != slot2:
    result = 2
  elif slot2 == slot3 and slot2 != slot1:
    result = 2
  else:
    result = 0
  return result

#Ask the user for how many chips they want to start with def get_bank() -> int: #get bank function
def get_bank () -> int : #get bank function
  user_val = 1
  while user_val == 1:
    bank1 = int(input("How many chips do you want to start with? ==> "))
    if bank1 <= 0:
      print("Too low a value, you can only choose 1 - 100 chips")
    elif bank1 > 100:
      print("Too high a value, you can only choose 1 - 100 chips")
    else:
      user_val = 0
      return bank1

def get_payout (wager, matches): # get payout function
    if matches == 3:
      result = wager*10 - wager
      return result
    elif matches == 2:
      result = wager*3 - wager
      return result
    else:
      result = wager*-1
      return result

if __name__ == "__main__":
   
    playing = True
    while playing:
      
      bank = get_bank() 
      first_bank = bank
      spin = 0
      chip_list = [] 
      chip_list.append(first_bank)

      while bank > 0:
        wager = get_wager(bank)
        slot1, slot2, slot3 = get_slot_results()
        
        matches = get_matches(slot1, slot2, slot3)
        payout = get_payout(wager, matches)
        bank = bank+payout
        print("Your spin", slot1, slot2, slot3)
        print("You matched", matches, "reels")
        print("You won/lost", payout)
        print("Current bank", bank)
        print()
        spin += 1
        chip_list.append(bank)
    print("You lost all", first_bank, "in", spin, "spins")
    print("The most chips you had was", max(chip_list))
    playing = play_again()