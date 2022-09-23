# Nicholas Patrick Suyat M2Lab2 Assignment

# Print a welcome messages and ask their name
print("Congratulations! you have won a vacation with all the airfare and all the hotel expenses paid")
name = input("What is your name?")
print("Congratulations " + name)

# Ask the user “where do you want to go for vacation? Display the location on screen.
Question = input("Where would you like to go on your vacation? ")
if Question == ("Japan"):
    print("Japan is a really good choice!")
elif Question == ("Philippines"):
    print("Philippines is a really good choice!")

num_days4 = ("4")
num_days7 = ("7")

# Calculate the cost by multiplying the number of days by 100.
Question2 = input("How many days are you planning to stay?")
if Question2 == num_days4:
    answer = int(num_days4)*100
    print("The cost will be $" + str(answer))
elif Question2 == num_days7:
    answer2 = int(num_days7)*100
    print("The cost will be $" + str(answer2))