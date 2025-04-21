import time
import random

inventory = [] #Array for store any item
enemys = ["spider", "slime", "ghost"]

health = 100

def Game_Over():
    time.sleep(0.5)
    print("\n Game Over...")
    time.sleep(1)
    retry = input("\ndo you want play agian? (Y or N)")
    if retry == "Y" or "y":
        bed_room()
    elif retry == "N" or "n":
        print("\nThe Game is End :0")
        print("\n\nThe Game Made By: Ahmed Mohamed Wahbi")

def Win():
    print("\n\nOh, the player won sorry i miss you're name")
    user = input("\nYou're name please sir : ")
    time.sleep(2)
    print(f"\nthe {user} won :)")
    print("\n\nThe Game Made By: Ahmed Mohamed Wahbi")


def add_item(item):
    time.sleep(1)
    if item not in inventory:
        inventory.append(item)
        print(f"\n the 🎭'{item}'🎭 is added to bag") #if item wasn't in inventory added to
    else:
        print("you already have this item")


def use_item(item):
    time.sleep(1)
    if item in inventory:
        print(f"\nThe {item} has been used")
        inventory.remove(item)

def damage_h(damage):
    global health #i make it global to all script now what is that
    health -= damage
    if health == 0:
        Game_Over()


def show_inventory():
    print("\n  My bag🎒")
    print(f" Health:{health}")
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
        Room2()
    elif choice == "3":
        bed_room()
    elif choice == "4":
        bathroom()


def door():
    enemy = random.choice(enemys)
    damage_h(30)
    print(f"the {enemy} hit you")
    print(f"health: {health}")

    choice = input("\npress (E) to open the door!!!")
    if choice == "E" or "e" and "key gold🎁" in inventory:
        print("yay!!!!")
        time.sleep(2)
        Win()
    else:
        print("You don't have the key :(")
        time.sleep(2)
        Game_Over()




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
        living_room()
    elif choice == "3":
        door()
    elif choice == "4":
        print(f"{enemy} loly boy cry i will eat you")
        time.sleep(3)
        Game_Over()





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
    elif choice == "2":
        damage_h(80)
    elif choice == "3":
        (f"the {enemy} make you win :0")
        time.sleep(2)
        Win()

    


def bed_room():
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
        bed_room()
    elif choice == "3":
        Room2()
    else:
        print("\n you have 3 choice only 1 and 2 and 3 only!!")


bed_room()