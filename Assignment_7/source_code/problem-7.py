#Alex Fonseca
#assignment 7
#problem: We are tasked to ask the user to enter a mpg, then asked to insert the file they are using. Once that happens they will be asked where they want it to be outputed and then it will do it.
#date: 10/23/2021



def open_file(prompt,mode="r"):
  while True:
    try:
      filename = input(prompt)
      file = open(filename, mode)
      return file
    except FileNotFoundError:
      print("Could not open file", filename)
    except IOError:
      print("There is an IO error", filename)

def output_file(prompt,mode="w"):
  while True:
    try:
      filename = input(prompt)
      file = open(filename, mode)
      return file
    except IOError:
      print("There is an IO error", filename)

def get_min_mpg():
  while True:
    try:
      mpg = float(input("Enter the minimum mpg ==>"))
      if mpg <= 0:
        print('Fuel economy given must be greater than 0')
      elif mpg > 100:
        print('Fuel economy must be less than 100')
      else:
        return mpg
    except ValueError:
      print("you must enter a number for the fuel economy")

mpg = get_min_mpg()
print()
file = open_file("Enter the name of the input vehicle file ==> ")
file.readline()

print()
output_file = open_file("Enter the name of the file to output to ==> ", "w")
for line in file:
  values = line.split("\t")
  try:
    combined = float(values[7])
    if combined >= mpg:
      output_str = "{:<5}{:<20}{:<40}{:>10.3f}".format(values[0], values[1], values[2], combined)
      print(output_str, file=output_file)
  except ValueError:
    print("Could not convert value", values[7] , "for vehicle", values[0], values[1], values[2])
    pass
  
