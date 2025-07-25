#exercise chapter 3.1 
#number guessing number 

#make a variable like winning number and assign any number to it 
#ask user to guess a number 
#if user guessed correctly then print  'YOU WIN" 
#if user didnt guessed correctly then : 
# print too low or too high 

#gooogle "how to generate random number in  python : to generate random winning number 

#import random 
#num = (random.randint (1,20)) #to generate a random numnber 


num = 45

guessnum = (int(input("guess the number" )))
print(num)

if guessnum == num:
 print ("You win")
 
else: #nested if else 
    if guessnum > num: 
        print("Too high")
     
    else :
        print("Too low")









