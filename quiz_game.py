print("Welcome to my computer quiz!")

playing=input("Do you want to play? ")
if playing!="yes":
    quit()
else:
    print("Okay! Let's play :) ")  
score=0      
answer=input("What does CPU stand for?").lower()
if answer=="central processing key":
    print("Correct!")   
    score+-1
else:
    print("Incorrect!")   
