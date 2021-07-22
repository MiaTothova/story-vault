# All code writen by: Marketa Mia Tothova 5P

import time 

words = {
    'adjective': ['red', 'blue'],
    'animal': ['fox', 'lion'],
    'vehicle': ['car', 'van'],
    'verb': ['sleeping', 'drinking'],
    'noun': ['dog', 'cat'],
    'foods': ['rice', 'beens'],
    'person': ['dad', 'son', 'mum'],
    'phrase': ['do it'],
    'color': ['red', 'blue', 'green', 'black']
}

def welcome():
    # Greets the user and starts the game.
    print("    __          __  _                            _         ")   
    print("    \ \        / / | |                          | |        ")
    print("     \ \  /\  / /__| | ___ ___  _ __ ___   ___  | |_ ___   ")
    print("      \ \/  \/ / _ \ |/ __/ _ \| '_ ` _ \ / _ \ | __/ _ \  ")
    print("       \  /\  /  __/ | (_| (_) | | | | | |  __/ | || (_) | ")
    print("      __\/_ \/ \___|_|\___\___/|_|_|_| |_|\___|  \__\___/  ")
    print("     / ____| |                   \ \    / /        | | |   ")
    print("    | (___ | |_ ___  _ __ _   _   \ \  / /_ _ _   _| | |_  ")
    print("     \___ \| __/ _ \| '__| | | |   \ \/ / _` | | | | | __| ")
    print("     ____) | || (_) | |  | |_| |    \  / (_| | |_| | | |_  ")
    print("    |_____/ \__\___/|_|   \__, |     \/ \__,_|\__,_|_|\__| ")
    print("                           __/ |                           ")
    print("                          |___/                            ")
    time.sleep(2)
    user = input("Please enter your name : \n")
    print(f"Hello {user} ! Let's pick a story. \n \n")
    time.sleep(2)


def selectItem(key):
    # get the array of items. e.g: adjetive, animal
    items = words[key]
    # tranverse the array with index that is why range is being used
    for i in range(len(items)):
        # Print the index and the value in the menu
        print("{}.- {}".format(i + 1, items[i]))

    # Initialize selection in -1 as no selection
    selection = -1

    # Make validInput false at the beggining.
    # This variable controls the input validation
    validInput = False

    # item is the final value that the user selected from the menu
    item = None

    # This loop is going to be repeated until the user has selected
    # a valid option from the menu.
    while not validInput:
        # ask the user to enter a number asociated to a value in the menu
        # rendered above.
        input_value = input("Select a '{}' form the list above: [1..{}]\n"
                            .format(key, len(items)))
        # Enclose in a try-except the intructions that could thrown
        # an exception to validate the user input.
        # If the entered value is not an integer the ValueError exception is
        # thrown.
        # If the integer value selected is not in the range of the values then
        # the IndexError is thrown when retrieving the items[selection-1] .
        try:
            selection = int(input_value)
            item = items[selection-1]
            validInput = True
        except (ValueError, IndexError):
            validInput = False
    return item


def main():
    # prints a list of available stories and allows for a choice to take place
    welcome()
    while True:
        print("I have 4 stories in my vault. \n")
        print("1. Taco Story")
        print("2. Pizza Party")
        print("3. About Me")
        print("4. Buterflies \n")
        print("5. To Exit \n")
        time.sleep(2)
        print("Which will you choose? (1, 2, 3,4) ?\n")
        choice = input()
        # Calls a story function based on choices
        if choice == "1":
            taco_story()
        elif choice == "2":
            pizza_party()
        elif choice == "3":
            about_me() 
        elif choice == "4":
            butterflies()
        elif choice == "5":
            # Breaks the loop to exit game on entering 5
            print("\n\n See you next time!")
            print("\n press : RUN PROGRAM to play again")
            print("        _____                 _ _                  ")
            print("       / ____|               | | |                 ")
            print("       | |  __  ___   ___   __| | |__  _   _  ___  ")
            print("       | | |_ |/ _ \ / _ \ / _` | '_ \| | | |/ _ \ ")
            print("       | |__| | (_) | (_) | (_| | |_) | |_| |  __/ ")
            print("        \_____|\___/ \___/ \__,_|_.__/ \__, |\___| ")
            print("                                          | |      ")
            print("                                        __/ |      ")
            print("                                       |___/       ")
            time.sleep(2)
            break
        else:
            print("Please enter a valid option! \n\n")
    

# def input_properties():
#     adjective = input("Insert a Adjective (describtive word)....\n")
#     verb = input("Insert a Verb (action word)....\n")
#     noun = input("Insert a Noun (name of a person/ place/ thing)....\n")
#     animal = input("Insert an Animal....\n ")
#     vehicle = input("Insert something you ride in....\n ")
#     color = input("Insert a colour ....\n ")
#     foods = input("Insert Foods (plural) ....\n")
#     person = input("Insert Person's Name ....\n ")
#     phrase = input("Insert a Phrase ....\n ")
#     song = input("Insert a Song name....\n ")
#     thing = input("Insert something or funny word...\n ")
#     feeling = input("Insert a Feeling....\n ")
#     celebrity = input("Insert Celebrities's Name ....\n ")
#     place = input("Insert a Place....\n ")
#     job = input("Insert a Job name....\n")

#     return (adjective, verb, noun, animal, vehicle, color, foods, person,
#             phrase, song, thing, feeling, celebrity, place, job)


def taco_story():
    # (adjective, verb, noun, animal, vehicle, color, foods, person,
    #  phrase,_) = input_properties()
    # adjective = input("Insert a Adjective (describtive word)....\n")
    # verb = input("Insert a Verb (action word)....\n")
    # noun = input("Insert a Noun (name of a person/ place/ thing)....\n")
    # vehicle = input("Insert something you ride in....\n ")
    # color = input("Insert a colour ....\n ")
    # foods = input("Insert Foods (plural) ....\n")
    # person = input("Insert Person's Name ....\n ")
    # phrase = input("Insert a Phrase ....\n ")
    # animal = input("Insert an Animal....\n ")

    adjective = selectItem('adjective')
    animal = selectItem('animal')
    vehicle = selectItem('vehicle')
    verb = selectItem('verb')
    color = selectItem('color')
    noun = selectItem('noun')
    foods = selectItem('foods')
    person = selectItem('person')
    phrase = selectItem('phrase')

    print("\n.-~-.-~-.-~.-~-.-~-.-~ LOADING STORY... .-~-.-~-.-~.-~-.-~-.-~\n\n")
    time.sleep(2)
    print("    >>------>  [ THE TACO STORY ] <------<< ")
    print("                      ___          /|       ")
    print("         ||||     .-"     "-.     } |  __   ")
    print("    |||| ||||   .'  .-'`'-.  '.   } | /  \  ")
    print("    |||| \  /  /  .'       '.  \  } | ;();  ")
    print("    \  /  ||  /  ;           ;  \  \| \  /  ")
    print("     ||   ||  | ;             ; |  ||  ||   ")
    print("     %%   %%  | ;             ; |  %%  %%   ")
    print("     %%   %%  \  ;           ;  /  %%  %%   ")
    print("     %%   %%   \  '.       .'  /   %%  %%   ")
    print("     %%   %%    '.  `-.,.-'  .'    %%  %%   ")
    print("     %%   %%      '-.,___,.-'      %%  %%   ")
    print("\n\nToday I went to my favorite Taco Stand called ") 
    print(f"the {adjective} {animal}. Unlike most food stands,")
    print(f" they cook and prepare the food in a {vehicle}") 
    print(f"while you {verb}. The best thing on the menu is ")
    print(f"the {color} {noun}. Instead of ground beef they ")
    print(f"fill the taco with {foods}, cheese, and top it off")
    print(f"  with a salsa made from {foods}.") 
    print("If that doesn't make your mouth water, ")
    print(f"then it' just like {person} always says: {phrase}! \n\n",)


def pizza_party():
    (adjective, person, foods, place, celebrity, feeling, 
     thing, song) = input_properties()
    # adjective = input("Insert a Adjective (describtive word)....\n")
    # person = input("Insert Person's Name ....\n ")
    # foods = input("Insert Foods (plural) ....\n")
    # celebrity = input("Insert Celebrities's Name ....\n ")
    # feeling = input("Insert a Feeling....\n ")
    # thing = input("Insert something or funny word...\n ")
    # song = input("Insert a Song name....\n ")
    # place = input("Insert a Place....\n ")
    print("\n.-~-.-~-.-~.-~-.-~-.-~ LOADING STORY... .-~-.-~-.-~.-~-.-~-.-~\n\n")
    time.sleep(2)
    print("     >>------>  [ THE PIZZA PARTY ] <------<<  ")
    print("⠀⠀⠀⠀⠀   ⠀⠀⠀⠀⠀⠀   ⠀⠀⣠⣤⣶⣶⣦⣄⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀   ")
    print("⠀⠀⠀⠀⠀⠀   ⠀⠀⠀⠀⠀⠀⠀⠀⢰⣿⣿⣿⣿⣿⣿⣿⣷⣦⡀⠀⠀⠀⠀⠀⠀   ")
    print("⠀⠀⠀⠀⠀⠀⠀⠀⠀   ⠀⠀⠀⠀⢠⣷⣤⠀⠈⠙⢿⣿⣿⣿⣿⣿⣦⡀⠀⠀⠀     ")
    print("⠀⠀⠀⠀⠀⠀⠀   ⠀⠀⠀⠀⣠⣿⣿⣿⠆⠰⠶⠀⠘⢿⣿⣿⣿⣿⣿⣆⠀⠀⠀    ")
    print("⠀⠀⠀⠀   ⠀⠀⠀⠀⠀⠀⢀⣼⣿⣿⣿⠏⠀⢀⣠⣤⣤⣀⠙⣿⣿⣿⣿⣿⣷⡀⠀  ")
    print("⠀⠀⠀   ⠀⠀⠀⠀⠀⠀⢠⠋⢈⣉⠉⣡⣤⢰⣿⣿⣿⣿⣿⣷⡈⢿⣿⣿⣿⣿⣷⡀   ")
    print("⠀⠀⠀   ⠀⠀⠀⠀⠀⡴⢡⣾⣿⣿⣷⠋⠁⣿⣿⣿⣿⣿⣿⣿⠃⠀⡻⣿⣿⣿⣿⡇  ")
    print("⠀⠀   ⠀⠀⠀⠀⢀⠜⠁⠸⣿⣿⣿⠟⠀⠀⠘⠿⣿⣿⣿⡿⠋⠰⠖⠱⣽⠟⠋⠉⡇  ")
    print("⠀⠀   ⠀⠀⠀⡰⠉⠖⣀⠀⠀⢁⣀⠀⣴⣶⣦⠀⢴⡆⠀⠀⢀⣀⣀⣉⡽⠷⠶⠋⠀   ")
    print("⠀⠀   ⠀⠀⡰⢡⣾⣿⣿⣿⡄⠛⠋⠘⣿⣿⡿⠀⠀⣐⣲⣤⣯⠞⠉⠁⠀⠀⠀⠀⠀   ")
    print("⠀⠀   ⢀⠔⠁⣿⣿⣿⣿⣿⡟⠀⠀⠀⢀⣄⣀⡞⠉⠉⠉⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀   ")
    print("   ⠀⠀⡜⠀⠀⠻⣿⣿⠿⣻⣥⣀⡀⢠⡟⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀    ")
    print("   ⠀⢰⠁⠀⡤⠖⠺⢶⡾⠃⠀⠈⠙⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀    ")
    print("   ⠀⠈⠓⠾⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀     ")
    print(f"\n\n I just got back from a pizza party with {person}.")
    print(f"Can you believe we got to eat {adjective} pizza in A {place}?!")
    print("Everyone got to choose their own toppings. ")
    print(f"I made '{foods} and {thing}'s pizza, which is my favorite!")
    print(f"They even stuffed the crust with {thing}'s. How {feeling}! ")
    print(f"If that wasn't good enough already, A {celebrity} was there ")
    print(f"singing {song} I was so inspired by the music. \n\n")
    

def about_me():
    (verb, animal, color, celebrity, thing, job, place,
     phrase) = input_properties()
    # verb = input("Insert a Verb (action word)....\n")
    # animal = input("Insert an Animal....\n ")
    # color = input("Insert a colour ....\n ")
    # celebrity = input("Insert Celebrities's Name ....\n ")
    # thing = input("Insert something or funny word...\n ")
    # place = input("Insert a Place....\n ")
    # job = input("Insert a Job name....\n")
    # phrase = input("Insert a Phrase ....\n ")
    print("\n.-~-.-~-.-~.-~-.-~-.-~ LOADING STORY... .-~-.-~-.-~.-~-.-~-.-~\n\n")
    time.sleep(2)
    print("    >>------>  [ ABOUT ME ] <------<<   ")
    print("                    ___   .--.     ")
    print("              .--.-"   "-' .- |       ")
    print("             / .-,`          .'          ")
    print("             \   `           \           ")
    print("              '.            ! \        ")
    print("                |     !  .--.  |       ")
    print("                \        '--'  /.____   ")
    print("               /`-.     \__,'.'      `\   ") 
    print("            __/   \`-.____.-' `\      /   ")
    print("            | `---`'-'._/-`     \----'    _    ")
    print("            |,-'`  /             |    _.-' `\   ")
    print("           .'     /              |--'`     / |   ")
    print("          /      /\              `         | |   ")
    print("          \    .\/  \      .--. __          \ |   ")
    print("           '-'      '._       /  `\         /   ")
    print("                       `\    '     |------'`    ")
    print("                         \  |      |         ")
    print("                          \        /        ")
    print("                           '._  _.'          ")
    print("                              ``            ")
    print(f"\n\n Hi my name is {celebrity}, ")
    print(f"but my friends call me {thing}")
    print(f"My favorite color is the {color} of {thing}'s and my favorite ")
    print(f"thing to do is {verb}. My parents were a {animal} and {job},")
    print(f"which is why we lived in {place}. You probably know me from")
    print(f"my TV commercial for {thing}. ")
    print(f"I'm the one who says, '{phrase}' at the very end!\n\n ")


def butterflies():
    (adjective, color, thing, place, person, foods, verb,
     phrase) = input_properties()
    # color = input("Insert a colour ....\n ")
    # adjective = input("Insert a Adjective (describtive word)....\n")
    # thing = input("Insert something or funny word...\n ")
    # place = input("Insert a Place....\n ")
    # person = input("Insert Person's Name ....\n ")
    # foods = input("Insert Foods (plural) ....\n")
    # verb = input("Insert a Verb (action word)....\n")
    # phrase = input("Insert a Phrase ....\n ")
    print("\n .-~-.-~-.-~.-~-.-~-.-~  LOADING STORY... .-~-.-~-.-~.-~-.-~-.-~\n\n")
    time.sleep(2)
    print("   >>------>  [ BUTTERLIES] <------<<   ")     
    print("    / `._                     _.' \     ") 
    print("    ( @ : `.                 .' : @ )   ") 
    print("     \  `.  `.  ._     _.  .'  .'  /    ") 
    print("      \;' `.  `.  \   /  .'  .' `;/     ") 
    print("       \`.  `.  \  \_/  /  .'  .'/      ") 
    print("        ) :-._`. \ (:) / .'_.-: (       ") 
    print("        (`.....,`.\/:\/.',.....')       ") 
    print("         >------._|:::|_.------<        ") 
    print("        / .'._>_.-|:::|-._<_.'. \        ") 
    print("        |o _.-'_.-^|:|^-._`-._ o|       ") 
    print("        |`'   ;_.-'|:|`-._;   `'|       ") 
    print("        '.o_.-' ;.'|:|'.; `-._o.'       ") 
    print("         ''.__.'   \:/   '.__.''         ") 
    print("                    ^                   ") 
    print(f"\n\n Last night I dreamed I was a {adjective} butterfly")
    print(f"with {color} splotches that looked like {thing}'s.")
    print(f"I flew to {place} with my best friend, {person}, ")
    print(f"who was a {adjective} INSECT. We ate some {foods} when")
    print(f"we got there and then decided to {verb}. The dream")
    print(f"ended when I said, '{phrase}.' \n\n")
    

main()
