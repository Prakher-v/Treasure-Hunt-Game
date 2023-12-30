def lets_play_again():
    print("\nDo you want to play again? (y or n)")
    answer = input(">").lower()
    if(answer == "y"):
        start()
    elif(answer == "n"):
        exit()

def game_over(reason):
    print("\n"+reason)
    print("Game Over!")
    lets_play_again()

def snake_room():
    print("\nThere is a snake here.")
    print("Behind the Snake in another door.")
    print("The snake is having eggs!")
    print("What would you do? (1 or 2)")
    print("1) . Take the eggs.")
    print("2) . Taunt the snake.")
    n = int(input('>'))
    if(n == 1):
        game_over("You want eggs not teasure !! Thats why the sanke killed you")
    elif(n == 2):
        print("Good, You Show Bravery")
        treasure_room()
    
def monster_room():
    print("\nNow you entered the room of a monster!")
    print("The monster is sleeping .\nBehind the monster, there is another door. What would you do? (1 or 2)")
    print("1). Go through the door silently.")
    print("2). Kill the monster and show your courage!")
    t = int(input('>'))
    if(t == 1):
        print("Good, Decision")
        treasure_room()
    elif(t == 2):
        game_over("The monster was hungry, he/it ate you")

def treasure_room():
    print("\nYou are now in a room filled with diamonds!")
    print("And there is a door too!")
    print("What would you do? (1 or 2)")
    print("1). Take some diamonds and go through the door.")
    print("2). Just go through the door.")
    w = int(input(">"))
    if(w == 1):
        print("\nCongratulaion")
        print("YAY !!! WIN")
        lets_play_again()
    elif(w == 2):
        game_over("Why you decided to leave the Diamonds Behind !!")
    
def start():
    print("\nYou are standing in a dark room.")
    print("There is a door to your left and right, which one do you take? (l or r)")
    ans = input(">").lower()
    if(ans == 'l'):
        snake_room()
    elif(ans == 'r'):
        monster_room()
    else:
        game_over("Please choose proper direction")
start()
            
        
