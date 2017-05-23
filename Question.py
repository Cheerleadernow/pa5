
#------------------------------------------------------------------------------
# Question.py
#Programming Assignment 5
#Computer attempts to guess a number you choose between given integers,Reads a two positive integers n from user input, then #guesses the number user is thinking.
#------------------------------------------------------------------------------

## Parameters 

answer = 'yes'
print()
print ("Enter two numbers, low then high.")
LimitLow = int(input(" low =  "))
LimitHigh = int(input(" high =  "))
NumToGuess = [(LimitLow + LimitHigh)//2]

print ()

print ("Think of a number in the range {} to {}. " .format(LimitLow, LimitHigh ))
print ()

NumOfTry = 0	
while LimitLow <= LimitHigh:
    NumOfTry += 1
    NumToGuess = (LimitLow+LimitHigh)//2
	
    print("Is your number Less than, Greater than, or Equal to {}? \n " .format(NumToGuess))
response = input ("Type 'G', 'L' or 'E': ").upper()		
while response != "E" and response != "G" and response != "L":
	    response = input ("Please type 'G', 'L' or 'E': ").upper()
if response == "L":
		LimitHigh = NumToGuess - 1
	 
elif response == "G":
		LimitLow = NumToGuess + 1
	   
elif response == "E":
	break

if high < low:
    print ('Your answers have not been consistent.')

else :
        if response == "E":
	        print('I found your number in  {}'.format(NumToTry))	
                
			elif :
    print('Your number is {}. I found it in {} guesses.' .format( NumToGuess, NumOfTry))