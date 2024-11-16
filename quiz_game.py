print("Welcome to my computer quiz!")

playing=input("Do you want to play? ")
if playing!="yes":
    quit()
else:
    print("Okay! Let's play :) ")  
"""
There are four questions....The questions start from here
"""    
score=0  #intially score is zero
#Question1    
answer=input("What does CPU stand for? ").lower()
if answer=="central processing unit":
    print("Correct!")   
    score+=1 #If correct then score will be updated adding plus one 
else:
    print("Incorrect!") 

#Qustion 2
answer=input("What does GPU stand for? ").lower()
if answer=="graphic processing unit":
    print("Correct!")   
    score+=1
else:
    print("Incorrect!")  

#Qustion 3     
answer=input("What does RAM stand for? ").lower()
if answer=="random access memory":
    print("Correct!")   
    score+=1
else:
    print("Incorrect!") 

#Qustion 4      
answer=input("What does PSU stand for? ").lower()
if answer=="power supply":
    print("Correct!")   
    score+=1
else:
    print("Incorrect!") 
#Result      
print("You have  got "+ str(score )+" questions correct.")  
print("You have got "+ str((score/4)*100) +" % "+"in the quiz.")    

