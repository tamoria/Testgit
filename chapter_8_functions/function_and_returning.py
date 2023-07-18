def greet_user():
    print("Hello!")

greet_user


def greet_user(username):
    print("Hello, " + username.title() + "!")

greet_user('jesse')
greet_user('sarah')

def display_message():
    print("I am learning about functions.")

display_message()

def favorite_book(title):
    print("One of my favorite books is " + title.title() + ".")

favorite_book("fermat's enigma")

def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print("\nI have a " + animal_type + ".")
    print("\nMy " + animal_type + "'s name is " + pet_name.title() + ".")

describe_pet('hamster', 'harry')
describe_pet('dog', 'willie')

# You can also make each parameter equal a specific arguement.

def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print("\nI have a " + animal_type + ".")
    print("\nMy " + animal_type + "'s name is " + pet_name.title() + ".")

describe_pet(animal_type = 'hamster', pet_name = 'harry')

# Setting a default value
# Here, we set a default value for animal type. Note, default value was entered in last when describing the function.
# Animal type will be replace if another animal type is provided during the function call. 

def describe_pet(pet_name, animal_type = 'dog'):
    """Display information about a pet."""
    print("\nI have a " + animal_type + ".")
    print("\nMy " + animal_type + "'s name is " + pet_name.title() + ".")

describe_pet(pet_name = 'willie')
describe_pet('harry', 'hamster')


def make_shirt(shirt_message, shirt_size = 'large'):
    print("\nYou requested a t-shirt with the following message: " + shirt_message + ".")
    print("The shirt will be made in size, " + shirt_size)

make_shirt("Forever Young", 'medium')
make_shirt('I love trees')

# Returning a Simple Value
# When you call a function that returns a value, you need to provide a variable where the return is stored. Ex. musician

def get_formatted_name(first_name, last_name):
    '''Return a full name, neatly formatted.'''
    full_name = first_name + " " + last_name
    return full_name.title()

musician = get_formatted_name('jimi', 'hendrix')
print(musician)



def get_formatted_name(first_name, middle_name, last_name):
    '''Return a full name, neatly formatted.'''
    full_name = first_name + " " + middle_name + " " + last_name
    return full_name.title()

musician = get_formatted_name('john', 'lee', 'hooker')
print(musician)

# Making an arguement optional
# Example below, middle name. Set middle name to a blank default.

def get_formatted_name(first_name, last_name, middle_name = ''):
    '''Return a full name, neatly formatted.'''
    if middle_name:
        full_name = first_name + " " + middle_name + " " + last_name
    else:
        full_name = first_name + " " + last_name
    
    return full_name.title()

musician = get_formatted_name('john', 'hooker')
print(musician)

musician = get_formatted_name('john', 'hooker', 'lee')
print(musician)

# Returning a Dictionary

def build_person(first_name, last_name):
    '''Return a dicionary of information about a person'''
    person = {'first' : first_name, ' last' : last_name}
    return person

musician = build_person('jimi', 'hendrix')
print(musician)

def build_person(first_name, last_name, age = ''):
    '''Return a dicionary of information about a person'''
    person = {'first' : first_name, ' last' : last_name}
    if age:
        person['age'] = age
    return person

musician = build_person('jimi', 'hendrix', 27)
print(musician)

# Using a function with a While loop

def get_formatted_name(first_name, last_name):
    '''Return a full name, neatly formatted.'''
    full_name = first_name + " " + last_name
    return full_name.title()

'''while True:
    print("\n Please tell me your name: ")
    print("\nEnter 'q' at any time to quit.")

    f_name = input("First name: ")
    if f_name == 'q':
        break

    l_name = input("Last name: ")
    if l_name == 'q':
        break

    formatted_name = get_formatted_name(f_name, l_name)
    print("\nHello, " + formatted_name + "!")
'''

def city_country(city, country):
    print(city.title() + ", " + country.title())

city_country('paris', 'france')



def make_album(artist_name, album_name, track_number = ''):
    if track_number:
        album = {'artist' : artist_name.title(), 'album' : album_name.title(), 'number of tracks' : track_number}
    else:
        album = {'artist' : artist_name.title(), 'album' : album_name.title()}
    return album

album_1 = make_album('Lauryn Hill', 'miseducated', 10)
print(album_1)

album_2 = make_album('dermont kennedy', 'sonder')
print(album_2)



def make_album(artist_name, album_name):
    album = {'artist' : artist_name.title(), 'album' : album_name.title()}
    return album

'''while True:
    print("\nPlease enter an artist and their album.")

    musician = input("Artist name: ")

    a_name = input("Album name: ")
    
    another_input = input("Would you like to enter another artist and album? (yes/no) ")
    if another_input == 'no':
        break

print("The artist you entered is, " + musician.title() + ". They recorded the album: " + a_name.title() + ".")'''


# Passing a list

def greet_users(names):
    for name in names:
        msg = "Hello, " + name.title() +  "!"
        print(msg)

usernames = ['hannah', 'ty', 'suraya']
greet_users(usernames)

# Modifying a List in a Function

unprinted_designs = ['iphone case', 'robot pendant', 'hexagon']
completed_models = []

while unprinted_designs:
    current_design = unprinted_designs.pop()    
    print("Printing model: " + current_design)
    completed_models.append(current_design)           # Moves each design to completed_models after printing

# Display all completed models
print("\nThe following models have been printed: ")
for completed_model in completed_models:
    print(completed_model)


# Preventing a Function from Modifying a list.
# Passing the function a copy of the list, not the original.

# Example: function_name(list_name[:])

# The slice notation [:] makes a copy of the list to send to the function.

def show_magicians(names):
    for name in names:
        msg = "Hello, " + name.title() + "!"
        print(msg)

magicians = ['david', 'eric', 'finley']
show_magicians(magicians[:])


# Passing an Arbitrary Number of Arguements
# use *

def make_pizza(*toppings):
    print(toppings)

make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')

# Adding a loop

def make_pizza(*toppings):
    print("\nMaking a pizza with the following toppings: ")
    for topping in toppings:
        print("- " + topping)

make_pizza('pepperoni')
print('')
make_pizza('mushrooms', 'green peppers', 'extra cheese')

# Mixing positional and arbitrary arguements

def make_pizza(size, *toppings):
    print("\nMaking a " + str(size) + "-inch pizza with the following toppings: ")
    for topping in toppings:
        print("- " + topping)

make_pizza(16, 'pepperoni')
print('')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')


# Using Arbitrary Keyword Arguements

def build_profile(first, last, **user_info):        # ** causes Python to create and empty dictionary called user_info
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile

user_profile = build_profile('albert', 'einstein', location = 'princeton', field = 'physics')

print(user_profile)

def sandwich_filling(*fillings):
    print("\nThe sandwich you ordered has the following fillings: ")
    for filling in fillings:
        print("\n- " + filling)

sandwich_filling('tomato', 'cheese', 'bacon')
sandwich_filling('spinach', 'cheese', 'portabella', 'tomato')


def make_car(model, year, **car_info):
    profile = {}
    profile['model_name'] = model
    profile['year built'] = year
    for key, value in car_info.items():
        profile[key] = value
    return profile

car_profile = make_car('volt', 2023, color = 'blue', electric = 'yes')
print(car_profile)