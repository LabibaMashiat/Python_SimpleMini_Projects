import random
options=["rock","paper","scissor"]
your_winning_times=0
computer_winning_times=0
while True:
    computer_pick=options[random.randint(0,2)]
    # 0="rock" , 1="paper" , 2="scissor"
    user_input=input("Type rock/paper/scissor or Q to quit = ").lower()
    print("Computer pick= "+computer_pick)
    if user_input=="q":
        break
# Game Start   
    elif user_input in options:
        if user_input=="rock" and computer_pick=="scissor":
            print("You won")
            your_winning_times+=1
            continue

        elif user_input=="paper" and computer_pick=="rock":
            print("You won")
            your_winning_times+=1
            continue
        elif user_input=="scissor" and computer_pick=="paper":
            print("You won")
            your_winning_times+=1
            continue
        elif user_input==computer_pick:
            print("Draw!")
            continue
        else:
            print("Computer Won.")
            computer_winning_times+=1
            continue
#Game ends
    else:
        print("Please enter rock/paper/scissor correctly.")
        continue

# result    
print("You won",your_winning_times,"times")    
print("Computer won",computer_winning_times,"times")    

if(your_winning_times>computer_winning_times):
    print("Congratulations!!You are the winner!")
elif your_winning_times<computer_winning_times:
    print("Oops! Computer is the winner! Best of luck for the next time!")
else:
    print("Its a draw!!")        

