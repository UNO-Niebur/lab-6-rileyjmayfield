#DiceRoll.py
#Name: Riley Mayfield
#Date: 2/24
#Assignment: Lab 6
#Purpose: Develop understanding of lists
import random

def main():
  print("2 dice 1000000 rolls\n")
  #Create an empty list with possible roll values
  rolls = [0] * 11
  for i in range(1000000):
    #Create two dice values ranging from 1 - 6 each
    die1 = random.randint(1,6)
    die2 = random.randint(1,6)

    #find the sum total of the two dice
    sum = die1 + die2
    rolls[sum-2] = rolls[sum-2] + 1

  
  r = 2
  #print statictics for dice rolls
  for roll in rolls:
    percent = round(roll/10000, 2)
    print(r , ":" , roll, ":", percent,"%")
    r = r + 1

if __name__ == '__main__':
  
  main()
