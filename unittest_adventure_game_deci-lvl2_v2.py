"""this is module for help to make a game like time make timeout when finishid look at another line"""
"""this is module for random choice i make it for list of enemy only"""
import time
import random

"""i made this variable inventory its Array to store any item i add to it"""
inventory = []

"""this variable for list of enemy"""
enemys = ["spider", "slime", "ghost"]


"""this variable health i make it for player for make it more funny"""
health = 100

"""this variable total score it's now 0 but in func it make deacrease and increase"""
total_score = 0



def print_and_sleep(text, delay):
    print(text)
    time.sleep(delay)






"""the leaderboard i name it only like this
 i make inside 
 the func global variable for all functions 
 know its total_score and i add parameter score so when i want call function i write what number the player take it """
def leaderboard(score):
    global total_score
    """here make it increase """
    total_score += score

def show_score():
    print(f"\nTotal score : {total_score}")




"""func for win or loss but i name it win"""
def win():
    """and return true i make under while true after he say you're score he return false for close the game"""
    if total_score >= 100:
        print_and_sleep("Congratulations! You've become a master adventurer!", 2)
        print_and_sleep("You found all the treasure and saved the kingdom.",2)
        print_and_sleep("Game Over - You Win!", 1)
        return True
    elif total_score >= 50:
        print_and_sleep("Well done! You've completed your quest.",2)
        print_and_sleep("but you should can make better end",2)
        print_and_sleep("Game Over - Good Ending!",1)
        return True
    elif total_score <= 0:
        print_and_sleep("Oh no! Your adventure has come to an early end.",2)
        print_and_sleep("You ran out of resources",2)
        print_and_sleep("Game Over - Try Again!",1)
        return True
    else:
        return False


"""i made this func for add items player a wait 1 second and system check if item not in inventory if not add itens
if item was in inventory system print you already have this item"""
def add_item(item):
    if item not in inventory:
        inventory.append(item)
        print_and_sleep(f"\n the 🎭'{item}'🎭 is added to bag",1) #if item wasn't in inventory added to
    else:
        print_and_sleep("you already have this item",1)


"""this func make use the item if item was in inventory and player use it inventory remove this item"""
def use_item(item):
    if item in inventory:
        print_and_sleep(f"\nThe {item} has been used",1)
        inventory.remove(item)


"""this func for damage player and i added also parameter when i call func i choose any number i want and i make global health
if health = 0 then func win() will be start and show her score"""
def damage_h(damage):
    global health #i make it global to all script now what is that
    health -= damage
    if health == 0:
        win()



"""this func show bag of player and health and total score i added for loop if item was 2 he print two times and any number"""
def show_inventory():
    print("\n  My bag🎒")
    print(f" Health:{health}")
    print(f"Total Score:{total_score}")
    print("=============")
    if not inventory:  #if inventory was empty print this
        print("you don't have any items :(")
    else:
        for item in inventory:
            print(f"--> {item} <--")
    print("=============")




#\n mean new line










def Room2():
    show_score()
    print_and_sleep("\n all the light-bulb are off",1)
    print_and_sleep("1-see you're bag",2)
    print_and_sleep("2-use tourch",2)
    print_and_sleep("3-return to bed room",1)
    print_and_sleep("4-go to the bathroom",1)


    choice = input("=> ")
    if choice == "1":
        show_inventory()
        Room2()
    elif choice == "2":
        use_item("old tourch 🔦")
        leaderboard(10)
        Room2()
    elif choice == "3":
        leaderboard(-1)
        bed_room()
    elif choice == "4":
        bathroom()


def door():
    show_score()
    """i made random enemy choice from list for make it more fun"""
    enemy = random.choice(enemys)
    damage_h(30)
    print_and_sleep(f"the {enemy} hit you",2)
    print_and_sleep(f"health: {health}",2)

    choice = input("\npress (E) to open the door!!!")
    if choice == "E" or "e" and "key gold🎁" in inventory:
        leaderboard(30)
        print("yay!!!!")
        time.sleep(2)
        show_inventory()
        win()
    else:
        leaderboard(-10)
        print("You don't have the key :(")
        time.sleep(2)
        show_inventory()
        win()




def living_room():
    show_score()
    print_and_sleep("\nThe key is here",1)
    print_and_sleep("\n1-see bag",1)
    print_and_sleep("2-take the key",1)
    print_and_sleep("3-go to the door",1)
    print_and_sleep("4-Cry",1)
    
    enemy = random.choice(enemys)
    choice = input("=> ")
    if choice == "1":
        show_inventory()
        time.sleep(1)
        living_room()
    elif choice == "2":
        add_item("key gold🎁")
        leaderboard(30)
        living_room()
    elif choice == "3":
        leaderboard(5)
        door()
    elif choice == "4":
        print(f"{enemy} loly boy cry i will eat you")
        leaderboard(-100)
        time.sleep(3)
        show_inventory()
        win()
    else:
        for i in range(1):
            print_and_sleep("please enter 1, or 2, or 3",2)
            living_room()





def bathroom():
    show_score()
    enemy = random.choice(enemys)
    print_and_sleep(f"\n the {enemy} hit you",2)
    damage_h(20)
    print(f"Health:{health}")
    time.sleep(1)
    print("\n1-escape from bathroom")
    print(f"2-fight the {enemy}")
    print("3-make the {enemy} friend and escape")

    choice = input("=> ")

    if choice == "1":
        living_room()
        leaderboard(20)
    elif choice == "2":
        leaderboard(-10)
        damage_h(80)
    elif choice == "3":
        (f"the {enemy} make you win :0")
        win()
    else:
        for i in range(1):
            print_and_sleep("please enter 1, or 2, or 3",1)
            bathroom()

    


def bed_room():
    show_score()
    """for start the story"""
    time.sleep(1)
    print("\n You were in the woods and then you found an abandoned house,")
    time.sleep(1)
    print("  you entered it and then you found yourself in a room")
    time.sleep(1)
    print("\n1-see you're bag")
    print("2-open-box")
    print("3-leave from room")

    choice = input("=> ")

    if choice == "1":
        show_inventory()
        bed_room()
    elif choice == "2":
        print("\n old tourch 🔦")
        add_item("old tourch 🔦")
        leaderboard(10)
        bed_room()
    elif choice == "3":
        Room2()
    else:
        for i in range(1):
            print("please enter 1, or 2, or 3")
            bed_room()


bed_room()






"""until true and win() func is called then end the game and return for player her score"""
while True:
    if win():
        break

print(f"Your final score: {total_score}")

"""todo : i will add more rooms and make it better and make story more long"""