import random
#Take user input
top_of_range=input("Type a number: ")
if top_of_range.isdigit():
    top_of_range=int(top_of_range)
    if top_of_range<=0:
        print("Please Type a number greater than zero.")
        quit()
else:
    print("Please type a valid digit next time.")
    quit()         
generate_number=random.randint(0,top_of_range)
#print(generate_number)
   
# random.randrange(11) generate random number from 0 to 10
# random.randrange(0,11) 0 included but not 11..
#To include 11 we have to use random.randint(0,11)
guesses=0
while(True):
        guesses+=1
        user_guess=int(input("Make a guess: "))
            
        if user_guess==generate_number:
            print("Correct!!You got it")
            break
        else:
            print("Incorrect!Try again")
            continue
print("You got it in",guesses,"guesses.")  
      