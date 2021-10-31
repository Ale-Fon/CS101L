#Alex Fonseca
#Assignment_8
#problem: must make a program for Weighted Grades!
#due 10/30/21 at 11:59

from statistics import mean
import math

#firstly I will make the main menu of the program
def Print_menu():
  print('            Grade Menu')
  print('1 - Add Test')
  print('2 - Remove Test')
  print('3 - Clear Test')
  print('4 - Add Assigment')
  print('5 - Remove Assignment')
  print('6 - Clear Assignment')
  print('D - Display Scores')
  print('Q - Quit')

def get_input():
  foo = True
  while foo:
    ask = input('==> ')
    if ask == '1':
      return '1'
    if ask == '2':
      return '2'
    if ask == '3':
      return '3'
    if ask == '4':
      return '4'
    if ask == '5':
      return '5'
    if ask == '6':
      return '6'
    if ask == 'D' or ask == 'd':
      return 'D'
    if ask == 'Q' or ask == 'q':
      return 'Q'

def Add_T(scores):
  foo = True
  while foo:
    score = int(input("Enter the new Test score 0-100 ==>"))
    if score < 0:
      print ("Cannot input score under 0, try again\n")
    else:
      foo = False
  scores.append(score)
  
def Remove_T(scores):
  foo = True
  while foo:
    s = int(input(("Enter the Test to remove 0-100 ==>")))
    if s < 0:
      print ("Cannot input score under 0, try again\n")
    else:
      foo = False
  if s in scores:
    scores.remove(s)
  else:
    print ("Could not find that score to remove\n")

def Clear_T(scores):
  scores.clear()
  print("Test scores cleared")

def Add_A(scores):
  foo = True
  while foo:
    score = int(input(("Enter the new Assignment score 0-100 ==>")))
    if score < 0:
      print ("Cannot input score under 0, try again\n")
    else:
      foo = False
  scores.append(score)

def Remove_A(scores):
  foo = True
  while foo:
    s = int(input(("Enter the Assignment to remove 0-100 ==>")))
    if s < 0:
      print ("Cannot input score under 0, try again\n")
    else:
      foo = False
  if s in scores:
    scores.remove(s)
  else:
    print ("Could not find that score to remove\n")

def Clear_A(scores):
  scores.clear()
  print("Assignment scores cleared")

def std(scores):
  s_mean = mean(scores)
  num = 0
  for i in scores:
    num += ((i - s_mean)**2)
  dev = math.sqrt((num/len(scores)))
  return dev

def Display_S(tcount,pcount,tscores,pscores):
  print('Type               #       min       max       avg       std\n============================================================\nTests             ',tcount, end ="")
  if tcount == 0:
    print('       n/a       n/a       n/a       n/a', end ="")
  else:
    print('       ',min(tscores), end ="")
    print('       ',max(tscores), end ="")
    print('       ',mean(tscores), end ="")
    print('       ',str(round(std(tscores),2)), end ="")
  print('\nPrograms          ',pcount, end ="")
  if pcount == 0:
    print('       n/a       n/a       n/a       n/a')
  else:
    print('       ',min(pscores), end ="")
    print('       ',max(pscores), end ="")
    print('       ',mean(pscores), end ="")
    print('       ',str(round(std(pscores),2)))
    
  if tcount == 0 and pcount == 0:
    weighted = 0
  elif tcount == 0:
    weighted = (mean(pscores) * 0.4)
  elif pcount == 0:
    weighted = (mean(tscores) * 0.6)
  else:
    weighted = (mean(tscores) * 0.6)+(mean(pscores) * 0.4)

  print("The weighted score is   ",weighted)


def main():
  tscores = []
  pscores = []
  tcount = 0
  pcount = 0
  Again = True
  while Again:
    Print_menu()
    choice = get_input()
    if choice == '1':
      Add_T(tscores)
      tcount += 1
    if choice == '2':
      Remove_T(tscores)
      tcount -= 1
    if choice == '3':
      Clear_T(tscores)
      tcount = 0
    if choice == '4':
      Add_A(pscores)
      pcount += 1
    if choice == '5':
      Remove_A(pscores)
      pcount -= 1
    if choice == '6':
      Clear_A(pscores)
      pcount = 0
    if choice == 'D':
      Display_S(tcount, pcount, tscores, pscores)
    if choice == 'Q':
      Again = False

main()