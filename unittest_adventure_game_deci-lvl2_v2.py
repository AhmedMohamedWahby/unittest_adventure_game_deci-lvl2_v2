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





"""the leaderboard i name it only like this
 i make inside 
 the func global variable for all functions 
 know its total_score and i add parameter score so when i want call function i write what number the player take it """
def leaderboard(score):
    global total_score
    """here make it increase """
    total_score += score






"""func for win or loss but i name it win"""
def Win():
    """and return true i make under while true after he say you're score he return false for close the game"""
    if total_score >= 100:
        print("Congratulations! You've become a master adventurer!")
        print("You found all the treasure and saved the kingdom.")
        print("Game Over - You Win!")
        return True
    elif total_score >= 50:
        print("Well done! You've completed your quest.")
        print("but you should can make better end")
        print("Game Over - Good Ending!")
        return True
    elif total_score <= 0:
        print("Oh no! Your adventure has come to an early end.")
        print("You ran out of resources")
        print("Game Over - Try Again!")
        return True
    else:
        return False


"""i made this func for add items player a wait 1 second and system check if item not in inventory if not add itens
if item was in inventory system print you already have this item"""
def add_item(item):
    time.sleep(1)
    if item not in inventory:
        inventory.append(item)
        print(f"\n the 🎭'{item}'🎭 is added to bag") #if item wasn't in inventory added to
    else:
        print("you already have this item")


"""this func make use the item if item was in inventory and player use it inventory remove this item"""
def use_item(item):
    time.sleep(1)
    if item in inventory:
        print(f"\nThe {item} has been used")
        inventory.remove(item)


"""this func for damage player and i added also parameter when i call func i choose any number i want and i make global health
if health = 0 then func win() will be start and show her score"""
def damage_h(damage):
    global health #i make it global to all script now what is that
    health -= damage
    if health == 0:
        Win()



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
    print("\n all the light-bulb are off")
    print("1-see you're bag")
    print("2-use tourch")
    print("3-return to bed room")
    print("4-go to the bathroom")


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
    """i made random enemy choice from list for make it more fun"""
    enemy = random.choice(enemys)
    damage_h(30)
    print(f"the {enemy} hit you")
    print(f"health: {health}")

    choice = input("\npress (E) to open the door!!!")
    if choice == "E" or "e" and "key gold🎁" in inventory:
        leaderboard(30)
        print("yay!!!!")
        time.sleep(2)
        show_inventory()
        Win()
    else:
        leaderboard(-10)
        print("You don't have the key :(")
        time.sleep(2)
        show_inventory()
        Win()




def living_room():
    print("\nThe key is here")
    print("\n1-see bag")
    print("2-take the key")
    print("3-go to the door")
    print("4-Cry")
    
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
        Win()
    else:
        for i in range(1):
            print("please enter 1, or 2, or 3")
            living_room()





def bathroom():
    enemy = random.choice(enemys)
    print(f"\n the {enemy} hit you")
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
        time.sleep(2)
        Win()
    else:
        for i in range(1):
            print("please enter 1, or 2, or 3")
            bathroom()

    


def bed_room():
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
    if Win():
        break

print(f"Your final score: {total_score}")

"""todo : i will add more rooms and make it better and make story more long"""