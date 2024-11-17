# chose your own adventure game

name=input("Type your name: ")
print("Welcome",name,"to the adventure game")

answer=input("You are on a dirt road,it has come to an end and you can go left or right.Which way would you like to go?(left/right) ").lower()
#What would happen if user chose left
if answer=="left":
    answer=input("You come to a river.You can walk around it and swim across.Type walk to walk around and swim to swim across: ").lower()
    #If user chose swim then what would happen
    if answer=="swim":
        print("You swam across and were eaten by an alligator.")
    #If user chose walk then what would happen
    elif answer=="walk":
        print("You walked for many miles,ran out of water and you lost the game")
    else:
        print("Not a valid option.You lose.") 
        

#What would happen if user chose right
elif answer=="right":
    answer=input("You come to a bridge,it looks wobbly,do you want to cross it or head back(cross/back): ").lower()
    #If user chose cross then what would happen
    if answer=="cross":
        answer=input("You cross the bridge and meet a stranger.Do you talk to them?(yes/no): ").lower()
        # If user chose yes
        if answer=="yes":
            print("You talk to the stranger and they give you gold.You WIN!!")
        # If user chose no
        elif answer=="no":
            print("You ignore the stranger and they are offended and you lose.")
        else:
            print("You go back and lose.")
            
    #If user chose back then what would happen
    elif answer=="back":
        print("You go back and lose.")
    else:
         print("Not a valid option.You lose.")  

else:
    print("Not a valid option.You lose.")        