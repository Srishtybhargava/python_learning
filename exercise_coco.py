#exercise coco 
#ask user's name and age 
#if user's name start with " a " and "A" and age is above 10 then 
#print ("you can watch movie coco")
#else print "sorry you cannnot watch coco 

name = input("enter your name ")
age = int (input ("enter your age"))
print (name, age)

if (name[0] == "A" or name[0] == "a" ) and age >= 10 :
    print("You can watch the movie coco")
    
else : 
     print ("Sorry, You cannot watch the movie coco")
    

