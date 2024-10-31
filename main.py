import time

cat_attributes = {
    "intelligence": 15,
    "energy": 50,
    "weight": 30,
}

print("Welcome to my cat game!")

# Take the user inputs for name and colour:
name = input("Enter name:")
colour=input("Enter a colour: ")
# ...

# start the while loop
while True:
    # Finish the string below
    option = input("What would you like to do? 1. Play with your cat 2. Train your cat 3. show stats ")

    if option == '1':
        cat_attributes["energy"]=(cat_attributes["energy"])-5
        print(cat_attributes["energy"])
        pass
    elif option == '2':
        cat_attributes["intelligence"]=(cat_attributes["intelligence"])+5
        cat_attributes["energy"]=(cat_attributes["energy"])-5
        pass
    elif option == "3":
        print(cat_attributes)
    else:
        pass

    # finish off the if statements below
    if cat_attributes['energy'] < 0:
        
        print("Your cat has collapsed!")
        print("Energy: " +str(cat_attributes["energy"]))

        for i in range (5):
            print(".")
            time.sleep(1)

        print("Your cat has woken up.")

        cat_attributes["energy"]=cat_attributes["energy"]+10
        cat_attributes["weight"]=cat_attributes["weight"]-10

        print("+10 Energy -10 Weight")
        pass
    # elif ...
