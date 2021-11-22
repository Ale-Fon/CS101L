#Alex Fonseca
#program 11
#created: 11/21, due: 11/21 at 11:59 pm
#problem: We are tasked to make a clock with the class method.

import time

class Clock(object):
  def __init__(self, hours, minutes, seconds):
    self.hour = hours
    self.minute = minutes
    self.second = seconds  
  
  def hour(self):
    return self.hour if self.milTime else ((self.hour-1) % 12)+1
    
  def hour(self, hour):
    self.hour = hours % 24

  def minute(self):
    return self.minute
  
  def minute(self, minutes):
    self.minute = minutes % 60
  
  def second(self):
    return self.second

  def second(self, seconds):
    self.second = seconds % 60

  def time(self):
    return self.hour, self.minute, self.second

  def time(self, t):
    self.hour, self.minute, self.second = t
  
  def tick(self):
    self.second = self.second + 1
    if self.second >= 60:
      self.second = 0
      self.minute += 1
    if self.minute >= 60:
      self.minute = 0
      self.hour += 1
    if self.hour >= 24:
      self.hour = 0 
  
  def __str__(self):
    ap = ("AM", "PM")[self.hour >= 12]
    return "{hr:>2}:{min:02}:{sec:02} {ap}".format(hr=self.hour, min=self.minute, sec=self.second, ap=ap)

if __name__ == "__main__":
  hours = int(input("What is the current hour ==> "))
  minutes = int(input("What is the current minute ==> "))
  seconds = int(input("What is the current second ==> "))

  clock = Clock(hours, minutes, seconds)

  while True:
    print(clock)
    clock.tick()
    time.sleep(1)