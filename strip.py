name = "  Srishty  "
dots = "..........."

#lstrip () method 

print(name+dots)
print(name.lstrip() + dots) #to remove left space 
print(name.rstrip() + dots) #to remoce right and left space 
print(name.strip()+ dots) #to remove both left and right space 


space = ' Srish tea'
#strip method cannot remoce the space whihc is coming between the variable. 
#we need to use replace method for that 

print(space.replace(" " , "") + dots)
