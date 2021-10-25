########################################################################
##
## CS 101 Lab
## Program #
## Alex Fonseca
## ajf8nd@umsystem.edu
##
## PROBLEM : We are tasked to use check digit in order to read a idnumber or card to decode which 
##
## ALGORITHM : 
##      1. Write out the algorithm
## 
## ERROR HANDLING:
##      Any Special Error handling to be noted.  Wager not less than 0. etc
##
## 
##
########################################################################
import string

def character_value(char : str) -> int:
  value = ord(char)-65
  return value
  ''' Returns 0 for A, 1 for B, etc. '''
    
def get_check_digit(idnumber : str) -> int:
  sum = 0
  for i in range(0,9):
    if idnumber[i].isdigit():
      sum += int(idnumber[i])*(i+1)
    else:
      sum += character_value(idnumber[i])*(i+1)
  return sum % 10      
  ''' Returns the check digit for the name and sid. '''

def verify_check_digit(idnumber : str) -> tuple:
  if len(idnumber) != 10:
    return False, "The length of the number given must be 10"
  for i in range(0,5):
    if idnumber[i].isalpha() == False:
      return False, ("The first 5 characters must be A-Z, the invalid character is at", i, " is ", idnumber[i])
  for i in range(6,10):
    if idnumber[i].isdigit() == False:
      return False, ("The last 3 characters must 0-9, the invalid character is at ", i, " is ", idnumber[i])
  if (idnumber[5] != '1') and (idnumber[5] != '2') and (idnumber[5] != '3'):
    return False, "The sixth character must be 1 2 or 3"
  if (idnumber[6] != '1') and (idnumber[6] != '2') and (idnumber[6] != '3')and (idnumber[6] != '4'):
    return False, "The seventh character must be 1 2 3 or 4" 
  if get_check_digit(idnumber) != int(idnumber[9]):
    return False, ("Check Digit " ,idnumber[9]," does not match calculated value ", get_check_digit(idnumber))
  return True, ""
  ''' returns True if the check digit is valid, False if not '''

def get_school(idnumber : str) -> str:
  school =['School of Computing and Engineering SCE','School of Law','College of Arts and Sciences','Invalid School','Invalid School']
  return school[int(idnumber[5])-1]
  ''' Returns the school the 5th index or 6th character is for. '''
  
def get_grade(idnumber : str) -> str:
  grade = ['Freshman','Sophomore','Junior','Senior','Invalid Grade','Invalid Grade']
  return grade[int(idnumber[6])-1]
  '''Returns the grade for index 6'''
   
if __name__ == "__main__":
    print("{:^60}".format("Linda Hall"))
    print("{:^60}".format("Library Card Check"))
    print("="*60)
    while True:
        print()
        card_num = input("Enter Libary Card.  Hit Enter to Exit ==> ").upper().strip()
        if card_num == "":
            break
        result, error = verify_check_digit(card_num)
        if result == True:
            print("Library card is valid.")
            print("The card belongs to a student in {}".format(get_school(card_num)))
            print("The card belongs to a {}".format(get_grade(card_num)))
        else:
            print("Libary card is invalid.")
            print(error)