#Alex Fonseca
#program 6
#date 10/23/2021
#problem: We are tasked to encode a string then be able to decode it after by Caesar Cipher!

import string

def Encrypt(string_text, int_key):
  encrypted = ""
  for i in range(0, len(string_text)):
    if ord(string_text[i]) == 32:
      encrypted += chr(32)
    else:
      value = ord(string_text[i])+int_key
      encrypted += chr(value)
  return encrypted.upper()
  '''Caesar-encrypts string using specified key.''' 

def Decrypt(string_text, int_key):
  decrypted = ""
  for i in range(0, len(string_text)):
    if ord(string_text[i]) == 32:
      decrypted += chr(32)
    else:
      value = ord(string_text[i])-int_key
      decrypted += chr(value)
  return decrypted.upper()
  ''' Decrypts Caesar-encrypted string with specified key. ''' 
 
def Get_input():
  foo = True
  while foo:
    ask = input('Enter your selection ==> ')
    if ask == '1':
      return '1'
    elif ask == '2':
      return '2'
    elif ask == 'Q':
      return 3
    else:
      print("Try again")
    
    '''Interacts with user. Returns one of: '1', '2', '3', '4'.'''
 
def Print_menu():
  print('MAIN MENU:')
  print('1) Encode a string')
  print('2) decode a string')
  print('Q) Quit')
  '''Prints menu. No user interaction. '''
  
  
def main(): 
  Again = True 
  while Again: 
    Print_menu()
    Choice = Get_input() 
    if Choice == '1': 
      Plaintext = input("Enter (brief) text to encrypt: ").upper() 
      Key = int(input("Enter the number to shift letters by: "))
      Ciphertext = Encrypt(Plaintext, Key)
      print("Encrypted:", Ciphertext) 
    elif Choice == '2': 
      Ciphertext = input("Enter (brief) text to decrypt: ").upper() 
      Key = int(input("Enter the number to shift letters by: "))
      Plaintext = Decrypt(Ciphertext, Key)
      print("Decrypted:", Plaintext) 
   
    else: 
      print("Have an ordinary day.") 
      Again = False 
      
      
# our entire program: 
main() 