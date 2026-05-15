class Character:
    def __init__(self, name, animal):
        self.name = name
        self.animal = animal.lower()

def left_path():
    print(f"\n{player.name}, you walk around the forest, lost and confused. You've lost your way home, and can't figure out how to get back. You come across a rushing river.")
    print("1. Try to swim across the river")
    print("2. Look for a bridge to go across")

    choice = input("> ")

    if choice == "1":
        if player.animal == "penguin":
            print("\nBeing a Penguin, you dive in and glide through the water with ease! You swim swiftly and gracefully across the river. You reach the other side and find your way home. You win!")
        else:
            print("\nThe current is too strong. You were never taught to swim. You are swept away. Game over.")
    elif choice == "2":
        bridge()
    else:
        print("That's not an option, buckaroo.")
        left_path()

def right_path():
    print("\nYou find a super duper ooky spooky cave.")
    print("1. Enter the super duper ooky spooky cave")
    print("2. Go past the cave and keep walking")

    choice = input("> ")

    if choice == "1":
        print("\nA maroon troll named Hargleswet appears. 'Hi, Imma eat you now.'")
        print("1. Try to run away")
        print("2. Accept your fate")
        
        action = input("> ")
        if action == "1" and player.animal == "rat":
            print("\nYou're a tiny rat! You scurry between his legs, dodging all of his moves and escape into the woods. You're safe and make it home!")
        else:
            print("\nHe catches you easily. He just picks you up and eats ya. Game over.")
            
    elif choice == "2":
        print("\nYou find a sign, but can't read. You call an animal taxi on your animal phone that now magically convienently has power... You win!")
    else:
        print("Nuh uh, invaly daly teehee.")
        right_path()

def shack_path():
    print("\nYou find a creepy abandoned shack. Literally. It has a sign above the door that says 'Creepy Abandoned Shack'. The door is creaking in the wind.")
    print("1. Knock on the door")
    print("2. Peek through the window")
    print("3. Sneak around to the backyard")

    choice = input("> ")

    if choice == "1":
        print("\nA ghost opens the door! His name is Gohn. He's actually very lonely and makes you tea. You spend the rest of your days as roommates, drinking tea and discussing literature. Neutral Ending.")
    elif choice == "2":
        print("\nYou see a pile of gold! But as you lean in, the window shatters as a troll from under the bridge bursts in and beats you to death with his bat. For some reaosn hes chanting 'BLUE PAINT! BLUE PAINT!' as you bleed out. Game over.")
    elif choice == "3":
        if player.animal == "dog":
            print("\nYour dog nose picks up a scent in the backyard! You follow it, and find out it led you back to your neighborhood. You win!")
        else:
            print("\nYou trip over a rusty lawnmower and make so much noise that you instantly explode from Lawnmover-itis. Game over.")
    else:
        print("The shack doesn't understand that command.")
        shack_path()

def bridge():
    print("\nHentroid the Troll (Hen Dawg) blocks your path.")
    print("1. Fight Hen Dawg")
    print("2. Answer one of his famous riddles")

    choice = input("> ")

    if choice == "1":
        if player.animal == "cow":
            print("\nYou're a massive, and I mean MASSIVE cow! You simply tip Hen Dawg over. He's too embarrassed to move, you destroyed his aura. You walk past. You win!")
        else:
            print("\nHen Dawg's aura is too cool. You pass away instantly. Game over.")
    elif choice == "2":
        riddle()
    else:
        print("Hen Dawg didn't like your invalid answer.")
        bridge()

def riddle():
    print("\nHentroid asks: 'Whats blue and smells like red paint?'")
    answer = input("> ").lower()

    if "blue paint" in answer:
        print("\nCorrect! You and Hen Dawg high-five. You go home. You win!")
    else:
        print("\nWrong. You are now the secret ingredient in Hen Dawg's Signature Soup. Game over.")

def mountain_path():
    print("\nYou face a towering, jagged mountain. The path up is narrow, and looks rather dangerous. However, if you get to the top, you might be able to see where your neighborhood is.")
    print("1. Scale the steep cliff face to save time")
    print("2. Take the long, winding stairs")

    choice = input("> ")

    if choice == "1":
        if player.animal == "cat":
            print("\nWith your feline agility, you leap from rock to rock effortlessly. You reach the summit and see your house! You win!")
        else:
            print("\nYou lose your footing and slide all the way back down. You're too tired to continue. You just take a nap and pass away for some reason. Game over.")
    elif choice == "2":
        print("\nYou walk for hours. You meet a mountain goat who gives you a granola bar. You never leave. You are a goat now, you spend the rest of your days eating grass and granola bars. Neutral Ending.")
    else:
        print("The mountain echoes your confusion. Try again.")
        mountain_path()

def meadow_path():
    print("\nYou enter a beautiful sunlit meadow. There is a picnic blanket laid out.")
    print("1. Eat the mysterious glowing sandwich in the basket")
    print("2. Nap in the tall grass")

    choice = input("> ")

    if choice == "1":
        print("\nIt was a magical sandwich! You grow wings and fly home, dodging the confused ducks in the air. You win!")
    elif choice == "2":
        print("\nYou fall into a deep sleep. A group of butterflies carries you to a faraway land. You're not lost anymore, but you're definitely not home. Neutral ending.")
    else:
        print("The grass tickles you until you pick a real option.")
        meadow_path()

def sky_path():
    print("\nYou look up and see a giant Eagle circling overhead. It lands and offers you a ride, but it looks a bit shaky. The eagle might be a little sick, but you would easily be able to se your house up high if it goes well.")
    print("1. Hop on its back and fly toward the horizon")
    print("2. Ask the Eagle to just drop you off at the nearest cliff")
    choice = input("> ")

    if choice == "1":
        if player.animal == "eagle":
            print("\nYou're an Eagle too! You don't need a ride. You both race home, and you win by the end of your beak. You win!")
        else:
            print("\nYou fly high up into the sky and the Eagle gets distracted by a shiny nickel on the ground and accidentally flips upside down. You fall off. Game over.")
    elif choice == "2":
        print("\nThe Eagle drops you off at a high cliff. It's a long way down.")
        print("1. Do a 'Trust Fall' off the edge")
        print("2. Wait for a different bird")
        
        action = input("> ")
        if action == "1":
            if player.animal == "cat":
                print("\nYou land perfectly on your feet after a 500-foot drop. Your house is right there. Physics doesn't apply to cats. You win!")
            else:
                print("\nGravity is something you forgot about. You didn't bounce. Game over.")
        else:
            print("\nYou wait so long you became friends with all of the animals in that area and got adopted into their comunity. Neutral ending.")
    else:
        print("The Eagle screeches in confusion.")
        sky_path()

user_name = input("Hello user! Please pick a name: ")
user_animal = input("Please pick an animal (rat, cat, dog, cow, eagle, or penguin): ")

player = Character(user_name, user_animal)

print(f"\nWelcome, {player.name} the {player.animal}!")
print("You're in a dark forest. You've lost your way home and don't know where to go. Where do you go?")
print("1. Left (The River)")
print("2. Right (The Cave)")
print("3. Middle (The Shack)")
print("4. Up (The Mountain)")
print("5. Down into the valley (The Meadow)")
print("6. Look up (The Sky)")

choice = input("> ")

if choice == "1":
    left_path()
elif choice == "2":
    right_path()
elif choice == "3":
    shack_path()
elif choice == "4":
    mountain_path()
elif choice == "5":
    meadow_path()
elif choice == "6":
    sky_path()
else:
    print("You stood still for too long and turned into a tree. Invalid choice.")