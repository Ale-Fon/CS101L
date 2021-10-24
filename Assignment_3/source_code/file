print('welcome to the flarsheim guesser!')
print()
playing = True
#firstly I make a variable and called it playing, then I set that to true. After that I made a while loop saying while playing is true to make the program go.
while playing is True: 
  print('please think of a number between and including 1 and 100. ')
  value = True
#here I made another while loop and also made another variable setting that to true. So while the value is true, i put if staments in it telling if the input is less than than 0 to print out that statement to repeat the code over until they gave a number between 0 or 2.
  while value is True:
    three = int(input('What is the remainder when your number is divided by 3 ?'))
    if three < 0:
      print('The value entered must be 0 or greater')
      continue
    elif three > 2:
      print('The value entered must be less than 3')
      continue
    elif three >= 0:
      break
  #here I did the same thing as the while loop for three, but changed up the variable and numbers conditions.
  while value is True:
    five = int(input('What is the remainder when your number is divided by 5 ?'))
    if five < 0:
      print('The value entered must be 0 or greater')
      continue
    elif five > 4:
      print('The value entered must be less than 5')
      value = False
    elif five >= 0:
      break
   #here I did the same thing as the while loop for three and five, but changed up the variable and numbers conditions.
  while value is True:
    seven = int(input('What is the remainder when your number is divided by 7 ?'))
    if seven < 0:
      print('The value entered must be 0 or greater')
      continue
    elif seven > 6:
      print('The value entered must be less than 7')
      value = False
    elif seven >= 0:
      break
  #I then take the input from each variable and then made a for loop of the number between 1, 100. I than took the variable from each input and took that remainder to maker sure that the number is the same as the one they guessed.
  for i in range(1, 101):
    if i % 3 == three and i % 5 == five and i % 7 == seven:
      print('your number is ', i)
      print('How amazing was that!')
      break

#and finally I made a variable asking they wanted to play again, and put if and elif statement for each condition such as If they put in Y or y then it will start the game over from the top. If they pressed N or n they it will stop the program completely.
  play = input('Do you want to play again? Y to continue, N to quit')

  if play == 'Y' or play == 'y':
    playing = True
    print()
  elif play == 'N' or play =='n':
    playing = False
    break

