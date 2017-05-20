
#Computer attempts to guess a number you choose between 1 and 100 in 10 tries
answer = 'yes'
print()
print ("Enter two numbers, low then high..")
LimitLow = int(input(" lower limit :  "))
LimitHigh = int(input(" upper limit:  "))
NumToGuess = [(LimitLow + LimitHigh)//2]
print("Low = {}".format(LimitLow))
print("High = {}".format(LimitHigh))
print ("Think of a number in the range {} to {}. " .format(LimitLow, LimitHigh ))
print ("Is your number Less than, Greater than, or Equal to {}?  ".format(NumToGuess))
#response = input()

response = input(" Type 'L', 'G' or 'E': ")


def BinSearch(x, L):
   left = 0
   right = len(L)-1
   while left<=right:   # search space is not empty
      m = (left+right)//2
      if x == L[m]:
         return m
      elif x < L[m]:
         right = m-1
      else:  #  L[m] < x 
         left = m+1
			

while answer == "yes":
    NumOfTry = 10
    NumToGuess = (LimitLow+LimitHigh)//2
    while NumOfTry != 0:
        try:
            print ("Is your number Less than, Greater than, or Equal to {}?  ".format(NumToGuess))
            print ("Please type: 'L', 'G' or 'E':")
         
            response  = int (input("So did I guess right?"))
            if 1 < response > 3:
                print ("Please enter a valid answer. 1, 2 and 3 are the valid choice")
                NumOfTry = NumOfTry + 1
            if response == 1:
                LimitHigh = NumToGuess
                print ("Hmm, so your number is between ",LimitLow, "and ", LimitHigh)
                NumOfTry = NumOfTry - 1
                print (NumOfTry, "attempts left")
                NumToGuess = int (((LimitHigh - LimitLow)/2) + LimitLow)
                if NumToGuess <= LimitLow:
                    NumToGuess = NumToGuess + 1
                if LimitHigh - LimitLow == 2:
                    NumToGuess = LimitLow + 1
            elif response == 2:
                LimitLow = NumToGuess
                print ("Hmm, so your number is between ",LimitLow, "and ", LimitHigh)
                NumOfTry = NumOfTry - 1
                print (NumOfTry, "attempts left")
                NumToGuess = int (((LimitHigh - LimitLow)/2) + LimitLow)
                if NumToGuess <= LimitLow:
                    NumToGuess = NumToGuess + 1
                if LimitHigh - LimitLow == 2:
                    NumToGuess = LimitLow + 1
            elif response == 3:
                print ("Woo hoo! I won")
                NumOfTry = 0
        except:
            break
    else:
        answer = input ('Do you want to play again? (yes/no)')

else:
    print ("Thank you for playing. Goodbye")