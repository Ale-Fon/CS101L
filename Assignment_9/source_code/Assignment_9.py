#Alex Fonseca
#program 9
#problem:
#created: 11/6/2021
#due: 11/7/2021 at 11:59pm

import csv

MONTHS = {1: 'January',2: 'February', 3: 'March', 4: 'April', 5: 'May', 6: 'June', 7: 'July', 8: 'August', 9: 'September', 10: 'October', 11: 'November', 12: 'December'}

def month_from_number(month: int) -> str:

  if month not in range(1, 13):
    raise ValueError("Month must be 1-12")
  return MONTHS[month]

def read_in_file(filename: str) -> list:
  file = open(filename, encoding='utf-8')
  csv_file = csv.reader(file)
  lst = list(csv_file)
  file.close()
  return lst



def create_reported_date_dict(file_lst: list) -> dict:
  da = {}

  for line in file_lst[1:]:
    date = line[1].strip()
    da[date] = da.get(date, 0) + 1
  return da


def create_reported_month_dict(file_lst: list) -> dict:

  mon = {}

  for line in file_lst[1:]:
    month = int(line[1].split("/")[0].strip())
    mon[month] = mon.get(month, 0) + 1
  return mon

def create_offense_dict(file_lst: list) -> dict:
  off = {}

  for line in file_lst[1:]:
    offense = line[7].strip()
    off[offense] = off.get(offense, 0) + 1
    
  return off

def create_offense_by_zip(file_lst: list) -> dict:
  zipc = {}
  
  for line in file_lst[1:]:
    offense = line[7].strip()
    zip_code = line[13].strip()
    if offense not in zipc:
      zipc[offense] = {}
    zipc[offense][zip_code] = zipc[offense].get(zip_code, 0) + 1
  return zipc

def get_top_ten_key_values(list):
  top = sorted(list.items(), key=lambda x: x[1], reverse=True)
  
  return top[:10]

if __name__ == "__main__":
  
  invalid_file = True
  while invalid_file:
    try:
      file_name = input("Enter the name of the crime data file ==> ")
      lst = read_in_file(file_name)
      invalid_file = False
    except FileNotFoundError:
      print('could not find the file specified. {} not found'.format(file_name))
  
  print()
  months = create_reported_month_dict(lst)
  top_10_months = get_top_ten_key_values(months)
  print("The month with the highest # of crimes is {} with {} offenses".format(month_from_number(top_10_months[0][0]), top_10_months[0][1]))

  offenses = create_offense_dict(lst)
  top_10_offenses = get_top_ten_key_values(offenses)
  print("The month with the highest # of crimes is {} with {} offenses".format(top_10_offenses[0][0], top_10_offenses[0][1]))

  offense_by_zip = create_offense_by_zip(lst)

  print()
  invalid_key = True
  while invalid_key:
    offense_key = input("Enter an offense ==> ")
    if offense_key in offense_by_zip:
      invalid_key = False
    else:
      print("Not a valid offense found, please try again")

  print()
  print('{} offenses by Zip Code'.format(offense_key))
  print("{:20}{:10}".format("zip code", "# offenses"))
  print("="*30)
  for key, value in offense_by_zip[offense_key].items():
    print("{:<20}{:>10}".format(key, value))