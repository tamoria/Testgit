cars = ['audi', 'bmw', 'suburu', 'toyota']

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())
print(car)

car = 'bmw'

print(car =='bmw')

requested_topping = "mushrooms"

if requested_topping != "anchovies":
    print("Hold the anchovies!")

age = 19

print(age < 21)
print(age<=21)
print(age > 21)
print(age >= 21)

# checking multiple conditions:

age_0 = 18
age_1 = 21

print(age_0 >=21 and age_1 >= 21)
print(age_0 >= 21) and print(age_1 >=21) # a more readable way to code.

# Checking whether a value is in a list

requested_toppings = ['mushrooms', 'onion', 'pineapple']

print('mushrooms' in requested_toppings)
print('pepperonip' in requested_toppings)

# checking whether a value is not in a list

banned_users = ['andrew', 'tim', 'mike']
user = 'marie'

if user not in banned_users:
    print(user.title() + ", you can post a response if you wish.")

# Bolean tests - another name for a conditional test. It is either True or False.
game_active = True
can_edit = False

car = 'toyota'

print("Is car == 'toyota'? I predit it is True.")
print(car == 'toyota')
print("\nDoes car == 'audi'? I predict False")
print(car == 'audi')

a = 'love'

print(a.lower() == 'love')
print(a.upper() == 'love')

a = 7

print(a < 8)
print(a > 8)
print(a <= 8)
print(a < 8 or a == 8)
print(a < 8 and a == 8)

flowers = ['orchid', 'lilly', 'buttercup']
for flower in flowers:
    print(flower == 'orchid')
print('lilly' in flowers)
print('marigold' in flowers)
print('marigold' not in flowers)

# Conditionals and if-else statements

age = 19

if age >= 18:
    print("You are old enough to vote!")
    print("Have you registered yet?")
else: 
    print("Sorry, you are too young to vote.")
    print("Please register when you are 18.")

age = 17
if age >= 18:
    print("You are old enough to vote!")
    print("Have you registered yet?")
else: 
    print("Sorry, you are too young to vote.")
    print("Please register when you are 18.")

# if-elif-else chain (testing for 1 condition)

age = 12

if age < 4:
    print("Your admission cost is $0.")
elif age < 18:
    print("Your admission cost is $5")
else:
    print("Your admission cost is $10")

    # more efficient way to code...

age = 12

if age < 4:
    price = 0
elif age < 18:
    price = 5
else:
    price = 10

print("Your adimission cost is $" + str(price) + ".")

# Using multiple elif

age = 67

if age < 4:
    price = 0
elif age < 18:
    price = 5
elif age < 65:
    price = 10
elif age > 65:
    price = 5

print("Your adimission cost is $" + str(price) + ".")

# Testing multiple conditions

requested_toppings = ['mushrooms', 'peppers', 'olives']

if 'mushrooms' in requested_toppings:
    print("Adding mushrooms")
if 'peppers' in requested_toppings:
    print("Adding peppers")
if 'olives' in requested_toppings:
    print("Adding olives")

print("\nFinished making your pizza!")

alien_color = ['red', 'blue', 'green']

if 'red' in alien_color:
    print("You earned 5 points")
if 'blue' or 'green' in alien_color:
    print("You earned 10 points")

alien_color = 'blue'

if 'red' in alien_color:
    print("5 points")
else:
    print("10 points")

alien_color = 'yellow'

if 'red' in alien_color:
    print("You earned 5 points")
elif 'blue' in alien_color:
    print("You earned 10 points")
else:
    print("You earned 15 points")

age = 10

if age < 2:
    print("Baby")
elif age < 4:
    print("Toddler")
elif age < 13:
    print("Kid")
elif age < 20:
    print("teenager")
elif age < 65:
    print("Adult")
else:
    print("Elder")

# Checking for Special Items

requested_toppings = ['mushrooms', 'peppers', 'olives']

for requested_topping in requested_toppings:
    if requested_topping == 'peppers':
        print("Sorry, we are out of peppers today.")
    else:
        print("Adding " + requested_topping + ".")

print("\nFinished making your pizza")

# Checking if a list is empty

requested_toppings = []

if requested_toppings:
    print("Adding " + requested_toppings + ".")
else:
    print("Are you sure you want plain pizza?")

print("\nFinished making your pizza")

# Using multiple lists

available_toppings = ['mushrooms', 'peppers', 'olives', ',onions', 'garlic', 'tomato']
requested_toppings = ['mushrooms', 'extra cheese', 'garlic']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print("Adding " + requested_topping + ".")
    else:
        print("Sorry, we don't have " + requested_topping + ".")

# Try it yourself practice
print('')

users = ['Cooper', 'Bodin', 'Finley', 'admin']

for user in users:
    if user is 'admin':
        print("Hello " + user + ", would you like to see the status report?")
    else:
        print("Hello " + user + ", thank you for logging in.")

print('')

users = []

if users:
    print("Hello " + user + ", thank you for logging in.")
else:
    print("We need some users!")

print('')

current_users = ['Cooper', 'Bodin', 'Finley', 'Catherine', 'Karen']
new_users = ['Jessica', 'BODIN', 'Finley', 'Gavin', 'Rowan']

for new_user in new_users:
    if new_user.title() in current_users:
        print("You entered " + new_user + ". Sorry, this username is already in use.")
    else:
        print("You entered " + new_user + ". This username is available.")

print('')

numbers = [1,2,3,4,5,6,7,8,9]
print(numbers)

for number in numbers:
    if number == 1:
        print("1" + "st")
    elif number == 2:
        print("2" + "nd")
    elif number == 3:
        print("3" + "rd")
    else:
        print(str(number) + "th")