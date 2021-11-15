#Alex Fonseca
#program 10
#created: 11/13, due: 11/13 at 11:59 pm
#problem: 

def get_words(words):
  word_list = words
  d = {}
  for word in word_list: 
    if len(word) > 3:
      d[word] = d.get(word, 0) + 1
  return d
  

def open_file():
  invalid_file = True
  while invalid_file:
    file = input("Enter the name of the file to open ")
    try:
      file = open(file, "r")
      filedata = file.read()
      change = '-.,!\n'
      for char in change:
        filedata = filedata.replace(char,' ')
      filedata = filedata.lower()
      word_list = filedata.split()
      invalid_file = False
      return word_list
    except FileNotFoundError:
      print("Could not open file", file)
    except IOError:
      print("There is an IO error", file)


def get_top_ten_key_values(list):
  top = sorted(list.items(), key=lambda x: x[1], reverse=True)
  
  return top[:10]


if __name__ == "__main__":
  
  word_list = open_file()
  words = get_words(word_list)
  top_10_words = get_top_ten_key_values(words)
  #print("The word with the highest count is {}, with {} counts".format(top_10_words[0][0], top_10_words[0][1]))
  
  
  print("{:10}{:15}{:10}".format("#", "Word", "Freq."))
  print("="*30)
  count=0
  for key, value in words.items():
    count += 1
    print("{:<10}{:15}{:<10}".format(count, key, value))

  count=0
  for key, value in words.items():
    if value == 1:
      count += 1 
  print('There are {} words that only occur once'.format(count))
  print('There are {} unique words in the document'.format(len(words)))
