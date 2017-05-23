print ("Please think of a number between 0 and 100!")


low = int(input("Enter the n two integers giving the lower limits respectively:  "))
high = int(input("Enter the n two integers giving the upper limits respectively:  "))
Responses = ''
Bounds = random.randint(low,high)
guess =  Bounds

while response != "c":
    
     Guesses = []
     i = 0
     response = input()

while (len(Guesses) < n):
    
	if (isPrime(i, Guesses)):
            Guesses.append(i)
            i += 1
    
	return (Guesses)
	
	print ("Is it ", Bounds, " ?")

	if response == "h":
			lowBound = Bounds + 1   
			Bounds = random.randint(lowBound,highBound)
			elif response == "l":
			highBound = Bounds - 1
			Bounds = random.randint(lowBound,highBound)
		    elif response == "c":
			print ("Your number is. I found it in 3 guesses. '")
			break
		    else:
			print ('Huh? "h", "l", or "c" are valid responses.')
			print (Guesses)

if response == "c":

        print ("Your number is + str(Guesses). I found it in str(Guesses[0]) guesses. ")    
       
	   while True:
    print ("Is your secret number " + str(guess) + "?")
    Responses = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")
    if (Responses == 'c'):
        print ("Game over. Your secret number was: " + str(guess),)
        break;
    elif (Responses == 'l'):
        low = guess
    elif (Responses == 'h'):
        high = guess
    else:
        print ("Sorry, I did not understand your input.")
        continue
guess = (low + high)/2