from tkinter.messagebox import YES


name = input("Hey pretty girl! What is your name?")
print( str(name) + " is such a beautiful name" + "!" + "\n")

Question = input("do you want to be my valentines date?")
if Question == ("yes"):
    print ("yey")
elif Question == ("no"):
    print ("sad")

food = input("can we go out?")
if food == ("yes"):
    print("where do you want to eat?")
elif food == ("no"):
        print(":(")