flowers = ['lillies', 'tulips', 'marigolds']
for flowers in flowers:
    print(flowers)
    print(flowers.title() + " are beautiful flowers.")
    print("I can't wait to pick " + flowers + " again.")

print("I look forward to seeing these flowers next Spring.")
pizza = ['pepperoni', 'supreme', 'veggie']
for pizza in pizza:
    print(pizza)
    print(" I really like " + pizza + " pizza")
print("I never tire of pizza\n")
for value in range(1,6):
    print(value)
numbers = list(range(1,6))
print(numbers)
even_numbers = list(range(2,11,2))
print(even_numbers)

squares = []
for value in range(1,11):
    square = value**2
    squares.append(square)
print(squares)
squares = []
for value in range(1,11):
    squares.append(value**2)
print(squares)
print(min(numbers))
print(max(numbers))
print(sum(numbers))
squares = [value**2 for value in range(1,11)]
print(squares)
squares = [value+2 for value in range(1,11)]
print(squares)

for value in range(1,20):
    print(value)
numbers_stats = list(range(1,3000))
print(numbers_stats)
print(sum(numbers_stats))
print(list(range(1,3000,2)))
print(list(range(2,3000,2)))
print(list(range(1,3000,3)))
cubes = [value**2 for value in range(1,3000)]
print(cubes)

games = ['soccer', 'baseball', 'basketball']
print(games[0:3])

print("Here are my favorite games")
for games in games[:2]:
    print(games.title())

insects = ['ladybug', 'butterfly', 'dragonfly', 'centipede']
print(insects)
insects.append('beetle')
print(insects)
print(insects[0:3])
print("The insects in the middle of the list:")
for insects in insects[1:3]:
    print(insects)

flowers = ['lillies', 'buttercups', 'tulips']
my_flowers = flowers
print(my_flowers)
my_friends = flowers[:]
print(my_friends)
my_flowers.append('poppies')
print(my_flowers)
my_friends.insert(2,'roses')
print(my_friends)
print("My favorite flowers:")
for mylist in my_flowers:
    print(mylist)

print("\nMy friend's favorite flowers:")
for friendslist in my_friends:
    print(friendslist)

dimensions = (20, 40)
print("Original Dimensions:")
for dimension in dimensions:
    print(dimension)
print('')
dimensions = (30, 40)
print("New Dimensions:")
for dimension in dimensions:
    print(dimension)

Menu = ('ice cream', 'steak', 'salad', 'soup')
print("The original menu:")
for menus in Menu:
    print(menus)
print('')
Menu = ('pudding', 'pasta', 'salad', 'soup')
print("Updated Menu:")
for menus in Menu:
    print(menus)
Menu.append('chicken')