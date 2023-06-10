import random
import time
#import datetime
#from timeit import default_timer as timer


#symbols = '!@#$%^&*()_+{}|:"<>?1234567890-=[]\;\',./~   '
#letters = 'qwertyuioplkjhgfdsazxcvbnmQAZWSXEDCRFVTGBYHNUJMIKQAZWSXEDCRFVTGBYHNUJMIK    '
#RHsymbols = '()_+=-"\':;{}['
#numSym = '12345678!@#$%^&* '
lowLetters = 'abcdefghijklmnopqrstuvwxyz '
#allLetters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ '
allChar = 'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ !@#$%^&*()_+{}|:"<>?1234567890-=[]\;\',./~              '
#capLH = 'QAZWSXEDCRFVTGBYHNUJMIK '
#cap1LH = 'UIJKNM '

#Specify input chars, number of characters, and speed goal
charInput = lowLetters
speedOfTypePerMin = 60
numOfChars = 10

print('Welcome to the typing game.\n')
print('Ignore the "-" at the end of each bit of text. Type the rest.')
print('Mistypes = streak cleared. Slow types = -1 to streak value.')
print('Streak of 10 to pass, at ' + str(speedOfTypePerMin) + ' characters per min.')
      

streak = 0

while streak < 10:
    randText = ''
    for i in range(numOfChars):
        randomValPos = random.randint(0, len(charInput) - 1)        
        randText = randText + charInput[randomValPos]
        
    while randText[numOfChars-1] == " ":
        randText = randText[0:numOfChars-1]
        randText += charInput[random.randint(0, len(charInput)-1)]       
        
    
    print("\n3")
    t = time.sleep(1.0)
    print("2")
    t = time.sleep(1.0)
    print("1")
    t = time.sleep(1.0)
    print("Go!\n")

    print(randText + "-")
    print("-----------------------------------------------------")
    
    firstTime = True
    userTyped = ''
    while userTyped != randText:
        start = time.monotonic()
        userTyped = input("")
        if userTyped == randText:
            end = time.monotonic()
            result = end - start
            print("\nCorrect\n")
            if firstTime == True and result < (speedOfTypePerMin / numOfChars):    
                streak += 1
            elif streak >= 1:
                streak -= 1
        else:
            print("\nTry again.\n")
            print(randText + "-")
            print("-----------------------------------------------------")
            start = time.monotonic()            
            streak = 0
            firstTime = False
        

    
    print("Your time was:", result)
    print("Current streak:", streak)

    
    
        
