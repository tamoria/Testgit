deck = ["1", "mew", "3", "4"]
print(deck[1])
my_card = deck[-1]
print(my_card)
del deck[1]
print(deck)
deck = ["1", "mew", "3", "4"]
deck[3] = "charmander"
print(deck)
print(deck.reverse())
del deck[1]
print(len(deck))
deck = ["pikachu", "mew", "mewtwo", "charzard"]
print(deck)
deck.sort(reverse=True)
print(deck)
sorted(deck)
print(deck)
deck = ["pikachu", "mew", "mewtwo", "charzard"]
print(deck)
sorted(deck)
print(deck)
deck.append(2)
print(deck)
deck.pop()
print(deck)

my_list = ["It's", "peanut butter", "jelly", "time"]
for index in range(3):
    print(my_list[index], end='')

my_list = [1, 3.0, ["a", "b", ["A", "B", "C"], "d"], "John"]
print(my_list[2][2][0])
    