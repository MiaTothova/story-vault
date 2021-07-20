import time 


def welcome():
    # Greets the user and starts the game.
    print("Welcome to Story Vault \n")
    time.sleep(2)
    user = input("Please enter your name : \n")
    print(f"Hello {user} ! Let's pick a story. \n \n")
    time.sleep(2)


def main():
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

        if choice == "1":
            # if a user typed "1" start taco_story()
            taco_story()
        elif choice == "2":
            # else if user entered "2" start pizza_party()
            pizza_party()
        elif choice == "3":
            # else if user entered "3" start about_me()
            about_me() 
        elif choice == "4":
            # else if user entered "4" start butterflies()
            butterflies()
        elif choice == "5":
            break
        else:
            print("Please enter a valid option")
    

def input_properties():
    adjective = input("Insert a Adjective (describtive word)....\n")
    verb = input("Insert a Verb (action word)....\n")
    noun = input("Insert a Noun (name of a person/ place/ thing)....\n")
    animal = input("Insert an Animal....\n ")
    vehicle = input("Insert something you ride in....\n ")
    color = input("Insert a colour ....\n ")
    foods = input("Insert Foods (plural) ....\n")
    person = input("Insert Person's Name ....\n ")
    phrase = input("Insert a Phrase ....\n ")

    return (adjective, verb, noun, animal, vehicle, color, foods, person,
            phrase)


def taco_story():
    (adjective, verb, noun, animal, vehicle, color, foods, person,
     phrase) = input_properties()
    time.sleep(2)
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
    adjective = input("Insert a Adjective (describtive word)....\n")
    song = input("Insert a Song name....\n ")
    thing = input("Insert something or funny word...\n ")
    color = input("Insert a colour ....\n ")
    foods = input("Insert Foods (plural) ....\n")
    person = input("Insert Person's Name ....\n ")
    feeling = input("Insert a Feeling....\n ")
    celebrity = input("Insert Celebrities's Name ....\n ")
    place = input("Insert a Place....\n ")


    print(f"\n\n I just got back from a pizza party with {person}.")
    print(f"Can you believe we got to eat {adjective} pizza in A {place}?!")
    print("Everyone got to choose their own toppings. ")
    print(f"I made '{foods} and {thing}'s pizza, which is my favorite!")
    print(f"They even stuffed the crust with {thing}'s. How {feeling}! ")
    print(f"If that wasn't good enough already, A {celebrity} was there ")
    print(f"singing {song} I was so inspired by the music. \n\n")
    


def about_me():
    verb = input("Insert a Verb (action word)....\n")
    job = input("Insert a Job name....\n")
    animal = input("Insert an Animal...\n ")
    thing = input("Insert something or funny word....\n ")
    color = input("Insert a colour ....\n ")
    celebrity = input("Insert Celebrities's Name ....\n ")
    phrase = input("Insert a Phrase ....\n ")
    place = input("Insert a Place....\n ")

    print(f"\n\n Hi my name is {celebrity}, ")
    print(f"but my friends call me {thing}")
    print(f"My favorite color is the {color} of {thing}'s and my favorite ")
    print(f"thing to do is {verb}. My parents were a {animal} and {job},")
    print(f"which is why we lived in {place}. You probably know me from")
    print(f"my TV commercial for {thing}. ")
    print(f"I'm the one who says, '{phrase}' at the very end!\n\n ")


def butterflies():
    adjective = input("Insert a Adjective (describtive word)....\n")
    verb = input("Insert a Verb (action word)....\n")
    place = input("Insert a Place....\n ")
    thing = input("Insert something or funny word....\n ")
    color = input("Insert a colour ....\n ")
    food = input("Insert Foods (plural) ....\n")
    person = input("Insert Person's Name ....\n ")
    phrase = input("Insert a Phrase ....\n ")
    print(f"\n\n Last night I dreamed I was a {adjective} butterfly")
    print(f"with {color} splotches that looked like {thing}'s.")
    print(f"I flew to {place} with my best friend, {person}, ")
    print(f"who was a {adjective} INSECT. We ate some {food} when")
    print(f"we got there and then decided to {verb}. The dream")
    print(f"ended when I said, '{phrase}.' \n\n")
    

main()
