import caesar_cypher as c
import sys

#Variable declaration 
game_running = False
menu_opened = False
opened_file = False
key_found = False
state = "None"

def menu():
    print("Menu opening ... \n")
    menu_opened = True
    while menu_opened:

        print('''Main keys to keep in mind:
    !only usable in the menu! \n
        'Quit' -> Close the game
        'Close' -> Close the menu
        'catalog' -> Your items
        'story' -> To get a slice of the story \n''')
        reponse_menu = input(" >> ").lower()

        match reponse_menu:

            case "quit":
                print("Thank you for playing, but I guess someone else will achieve this task...\n")
                sys.exit()
                
            case "close":
                print("menu closing... \n")
                menu_opened = False

            case "catalog":
                if key_found:
                    print("Items: Key for the princess' room \n")
                else:
                    print("Items: None \n")
                
            case "story":
                print("The story ")

            case _:
                print("We cant seem to find this commend\n")

def princess_room():
    
    print('''\nyou knock, but nobody seem to answer... 
    The door is locked. \n''')

    while True:    
        if key_found:
            print('''You do own the key now, what do you do ?
                        'enter' -> enter the room
                        'back' -> go back to the main room''')
            reponses = input(">> ").lower()

            match reponses:
                case "enter":
                    princess()

                case 'back':
                    main_room()

                case _:
                    print("We cant seem to find this commend.\n")   
        else:
            main_room()
            
def pc():
    print('''\n You get closer to the laptop to read "18" as the name of the user
     must be useful in the future you thought...
     On the screen, two applications sit open: one labeled 
     "Caesar Cypher" 
     the other a locked file that demands a "decrypted sentence" as its password...
     What do you do? \n''')
    casear = True

    while casear:
        global opened_file
        print('''Choose one of the options below:
                'menu' to open the menu 
                'Caesar' to Caesar cypher
                'file' to input a code in the locked file
                'back' to go back to the bedroom''')
        reponses = input(">> ").lower()

        match reponses:
            case "menu":
                menu()
        
            case 'caesar':
                c.caesar()
        
            case 'file':
                password = input('''\n Insert the password : ''').lower()
                if password == "i am free":
                    print("\n Access allowed \n\n instructions \n")
                    opened_file = True


                else:
                    print("\n Access denied \n ")

            case 'back':
                bedroom()

            case _:
                print("We cant seem to find this commend.")   
        
def bedroom():
    print('''\nThe room is dark except for the pale glow of a laptop screen,
    casting long shadows across an unmade bed and scattered papers. What do you do ?\n''')

    while True:
        print('''Choose one of the options below:
                'menu' to open the menu 
                'PC' to lanch the pc
                'back' to go to main room''')
        reponses = input(">> ").lower()

        match reponses:
            case "menu":
                menu()
        
            case 'pc':
                pc()
        
            case 'back':
                main_room()

            case _:
                print("We cant seem to find this commend.")        

def kitchen():
    print("\n Describe the kitchen, What do you do?\n ")

    while True:
        global key_found
        print('''Choose one of the options below:
                'menu' to open the menu 
                'inspect' to inspect the walls
                'back' to go to main room''')

        reponses = input(">> ").lower()

        match reponses:
            case "menu":
                menu()
        
            case 'inspect':
                print("\n When you look closer you find this writing on the wall: \n A SE XJWW \n I wonder what it could stand for...\n")
                if opened_file:
                    print('''\nfound an opening in the wall and got a key out of it, 
                    it looks like the princess' room locket key...\n''')
                    key_found = True
        
            case 'back':
                print("Going back to the main room...")
                main_room()

            case _:
                print("We cant seem to find this commend.\n")               

def main_room():
    print('''\n describe main room and purpose \n''')

    while game_running:
        print('''Choose one of the options below:
                'menu' to open the menu 
                'left' to go to the bedroom
                'right' to go to the kitchen
                'front' to go to the princess' room ''')
                
        reponses = input(" >> ").lower()

        match reponses:
            case "menu":
                menu()
        
            case 'left':
                bedroom()
        
            case 'right':
                kitchen()
        
            case 'front':
                princess_room()

            case _:
                print(" \n We cant seem to find this commend. \n")

def main_game():
    global game_running

    print("")
    print('''Welcome dear user unto 'the art of a hero'! \n
            You are the hero, your role is to rescue the princess who's stuck in her room,
            or at least that's what everybody says... \n
            will you acheive this ? \n''')

    while not game_running:   
        print('''
            choose the options below: 
            'exit' -> quit the game
            'enter' -> start the game
            'menu' -> open the menu
            ''')
            
        reponse = input(" >>").lower()
        match reponse:
            case 'exit':
                print('Thank you for playing, but I guess someone else will achieve this task...\n')
                return
            case 'enter':
                print(" \n We have a true hero! \n")
                game_running = True
                main_room()
                
            case 'menu':
                menu()
                
            case _:
                print("We cant seem to find this commend.\n")


main_game()