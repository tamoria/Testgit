# Modulo, %, provides the remainder of a division problem

#print(4 % 3)
#clear
#print(8 % 4)

# Tell whether a number is even

# number = input("Enter a number, and I'll tell you if it's even or odd: ")
# number = int(number)

# if number % 2 == 0:
    #print("\nThe number " + str(number) + " is even.")
# else:
    # print("\nThe number " + str(number) + " is odd.")

# Try it yourself

#car = input("What kind of rental car would you like? ")

#print("I can find a " + str(car) + " for you.")

#people = input("How many people are sitting at your table? ")
#people = int(people)

#if people < 8:
    #print("Your table is ready.")
#else:
    #print("Sorry, due to the size of your party, there is a 10 minute wait.")

number = input("Pick a number, any number: ")
number = int(number)

if number%10 == 0:
    print("Your number is a multiple of 10.")
else:
    print("Your number is not a multiple of 10.")