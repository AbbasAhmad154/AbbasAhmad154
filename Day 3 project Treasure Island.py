print("Assalamualikum") 
print("Welcome to Treasure Island. ")
print("Your mission is to find the treasure.")
choice1 = input('You\'re at a crossroad, where do you want to go? Type "left" or "right".').lower( )

if choice1 == "right" :
   choice2 =  input(f'You\'ve come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across. ').lower( )
   if choice2 == "wait":
    choice3 = input("You arrived to the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose? ").lower( )
    if choice3 == "red":
        print("It's a room full of fire. Game over.")
    elif choice3 == "yellow":
        print("You found the treasure! You Win! ")
    elif choice3 =="blue":
                print("You enter a room of beasts. Game over")
    else:
           print("You choose a door that doesn't exist. Game over.")     
   else:
        print("You got attacked by an angry tout. Game over.")
    
else:
    print("You fell into a hole, Game over.")
    

    
