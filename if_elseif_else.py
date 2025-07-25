#id elif else statement 
#show ticket pricing 

#1 to 3 (free)
#4 to 10 (150)
#11 to 60 (250)
#above 60 (200)

age = input("enter your age")
age = int (age)

if 0<=age<=3:
 print("Ticket is free")
 
elif 3<age<10: 
    print("Ticket price is : 150")
    
elif 10<age<=60:
    print ("Ticket price is : 250")

else :
    print ("Ticket price is : 200")

