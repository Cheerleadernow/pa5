
#------------------------------------------------------------------------------
# Question.py
# Programming Assignment 5
# Reads a two positive integers n from user input, then guesses the number user is thining.
#------------------------------------------------------------------------------

import random

lowBound = int(input("Enter the n two integers giving the lower limits respectively:  "))
highBound = int(input("Enter the n two integers giving the lower and upper limits respectively:  "))
response = ''
Intuition = random.randint(lowBound,highBound)
Guessanswer = (lowBound + highBound)//2
mid = []

print("Low = {}".format(lowBound))
print("High = {}".format(highBound))
print ("Is your number Less than, Greater than, or Equal to {}?  ".format(Guessanswer))
response = ()
#print ("Type 'L', 'G' or 'E' ", end="")

#-- Search Functions

def binary_search(a, x, l=0, highBound=None):
    if highBound is None:
        highBound = len(a)
    while lowBound < highBound:
        mid = (lowBound+highBound)//2
        midval = a[mid]
        if midval < x:
            lowBound = mid+1
        elif midval > x: 
            highbound = mid
        else:
            return mid
			
#-----Main Program

while response != "e":
    print ("Is your number Less than, Greater than, or Equal to {}?  ".format(mid))
    response = input()
    if response == "g":
        lowBound = Intuition + 1   
        Intuition = random.randint(lowBound,highBound)
    elif response == "l":
        highBound = Intuition - 1
        Intuition = random.randint(lowBound,highBound)
    elif response == "e":
        print ("Woohooo, I'm so bitchin'")
        break
    else:
        print ('Huh? "higher", "lower", or "yes" are valid responses.')

print ()

