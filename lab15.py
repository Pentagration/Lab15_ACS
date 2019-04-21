# Lab 15 Python Standard Library
# Adam Houser, Colin Reed, Sergio Quiroz
#-------------------------------------

import random
import time

#---------------------------------------


def diceRoll(): # dice are rolled and value is stored
  dice1 = die()
  dice2 = die()
  sum = dice1 + dice2

  print("Total roll was " + str(sum))

  return sum

def die(): # the dice are shuffled

  return random.randint(1,6)
  time.sleep(1)


def roll(): #players first roll
  sum = diceRoll()

  if( sum == 7 or sum == 11):

    print("Congratulations you WIN! you rolled a " + str(sum))
    return 0

  elif (sum == 2 or sum == 3 or sum == 12):

    print("Sorry you lose you rolled a " + str(sum))


  elif  (sum != 2 or sum != 3 or sum != 12 or sum != 7 or sum != 11):
    print ("the point is for this game is " + str(sum))
    point = sum
    return point


def secondRoll(point): #player's second roll and so on
  point = point
  secondRoll = 1

  while secondRoll !=0 :

    diceRoll()
    if diceRoll() == point:
      print "The sum on the new roll matches the point YOU WIN!"

      break

    elif diceRoll() == 7:
      print("You rolled a 7, you lose play thanks for playing!! ")
      secondRoll = 0


def craps(): #run to play game

  point = roll()
  time.sleep(1)
  if point != 0:
     print("------------------------")
     time.sleep(1)
     secondRoll(point)
     print("-------------------------")


# ------------------------- lab part 2 ------------------------------


import calendar
import datetime

def month(): # asks user for the month and displays the month

  month = input("Enter the number of month you were born ")
  year = input("Enter the year you were born ")
  print (calendar.month(year,month))

def birthday(): # this will calculate the day until your next birthday

  month = input("\nEnter the number of month you were born ")
  day = input("Enter the number of day you were born ")

  currentDay = datetime.datetime.now()
  birthday = datetime.datetime(currentDay.year, month, day) #only works when it has two datetime

  print("Lets calculate how many more days until your birthday!")
  time.sleep(2)
  print("\ncalculating...")
  time.sleep(3)

  birthday2 = datetime.datetime(1 + currentDay.year, month, day)

  if currentDay > birthday:
      ppp = (birthday2 - currentDay).days + 1
  else:
      ppp = (birthday - currentDay).days + 1

  print ("Looks like your birthday will be in " + str(ppp) + " days!")



def declaration():

  import datetime
  import calendar
  #Monday July 4th, 1776)
  #x = datetime.datetime(1900, 7, 4, 12)

  #print(x.strftime("Monday "+ "%B %dth, %Y"))   #for some reason strftime wont go before the year 1900

  print ("Write out the full name of a day.")
  month = input("Input a month (the number): ")
  day = input("Input a day (the number): ")
  year = input("Input a year: ")
  wDay = calendar.weekday(year, month, day)
  wDay = calendar.day_name[wDay]
  wMonth = calendar.month_name[month]
  print str(wDay) + " " + str(wMonth) + " " + str(day) + ", " + str(year)
