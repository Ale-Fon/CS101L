########################################################################
##
## CS 101 Lab
## Program #4
## Alex Fonseca
## ajf8nd@umsystem.edu
##
## PROBLEM : We have to make a slot machine, and ask the user how much chips will they like to start off with and how much will they wager each spin.
##
## ALGORITHM : 
##      1. Write out the algorithm
## 
## ERROR HANDLING:
##      Any Special Error handling to be noted.  Wager not less than 0. etc
##
## OTHER COMMENTS:
##      Any special comments
##
########################################################################

def play_again() -> bool:

    playing = input('Would you like to play again? :')
    if playing == 'N' or playing == 'NO':
      return False
    elif playing == 'Y' or playing == 'Yes':
      return True


    ''' Asks the user if they want to play again, returns False if N or NO, and True if Y or YES.  Keeps asking until they respond yes '''
     
def get_wager(bank : int) -> int:
  while get_wager:
    wager = int(input('How many chips would you like to wager?'))
    if wager <= 0:
      print('The wager amount must be greater than 0. Please enter again.')
      continue
    elif wager > bank:
      print('The wager amount cannot be greater than how much you have.',bank)
      continue

    ''' Asks the user for a wager chip amount.  Continues to ask if they result is <= 0 or greater than the amount they have '''

    return wager            

def get_slot_results() -> tuple:
  import random
  reela = random.randint(1,10)
  reelb = random.randint(1,10)
  reelc = random.randint(1,10)

  ''' Returns the result of the slot pull '''

  return reela, reelb, reelc

def get_matches(reela, reelb, reelc) -> int:
  match = 0
  if reela == reelb:
    match += 1
  if reela == reelc:
    match += 1
  if reelb == reelc:
    match += 1
  if match == 1:
    match += 1
  elif match == 2:
    match += 1
    ''' Returns 3 for all 3 match, 2 for 2 alike, and 0 for none alike. '''

  return match

def get_bank() -> int:
  while get_bank:
    chips = int(input('How many chips do you want to start with?'))
    if chips >= 101:
      print('Too high a value, you can only choose 1 - 100 chips')
      continue
    elif chips <= 0:
      print('Too low a value, you can only choose 1 -100 chips')
      continue
    else:
      return chips
    ''' Returns how many chips the user wants to play with.  Loops until a value greater than 0 and less than 101 '''

    return 0

def get_payout(wager, matches):
  payout = 0
  if matches == 3:
    payout = wager * 10
  elif matches == 2:
    payout = wager * 3
  elif matches == 0:
    payout = wager * -1
    ''' Returns how much the payout is.. 10 times the wager if 3 matched, 3 times the wager if 2 match, and negative wager if 0 match '''
  return payout    


if __name__ == "__main__":

    playing = True
    while playing:

        bank = get_bank()
        initial = bank
        count = 0
        highest = 0

        while bank>0:  # Replace with condition for if they still have money.
            
            wager = get_wager(bank)

            reel1, reel2, reel3 = get_slot_results()

            matches = get_matches(reel1, reel2, reel3)
            payout = get_payout(wager, matches)
            bank = bank + payout
            if bank > highest:
              highest = bank


            print("Your spin", reel1, reel2, reel3)
            print("You matched", matches, "reels")
            print("You won/lost", payout)
            print("Current bank", bank)
            print()
            count += 1
           
        print("You lost all", initial, "in", count, "spins")
        print("The most chips you had was", highest)
        playing = play_again()
