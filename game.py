
#Variable declaration 
game_running = False
menu_opened = False
opened_file = False
key_found = False



def main_room():
    print('''describe main room and acessible keys
            'menu' to open the menu 
            'left' to go to the bedroom
            'right' to go to the kitchen
            'front' to knock on the princess' room ''')
    reponses = input().lower()
    if reponses == 'menu':
        print("Menu opening...")



print("")
print('''Welcome dear user unto 'the art of a hero'! \n
    You are the hero, your role is to rescue the princess who's stuck in her room,
    or at least that's what everybody says... \n
    will you acheive this ? \n
    choose the options below: 
    'exit' -> quit the game
    'enter' -> start the game
    'menu' -> open the menu
    ''')
reponse = input().lower()
if reponse == 'exit':
    print('I guess someone else will acheive this task...')
    pass
elif reponse == 'enter':
    print("We have a real hero! \n")
    game_running = True
    main_room()
elif reponse == 'menu':
    print("menu opening...")    
else:
    raise print("make sure to type 'exit' 'enter' or 'menu'") 


