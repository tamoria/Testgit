'''age = input("What is your age? ")
age= int(age)

while age > 10:
    age -= 1
    print(age, end="")'''

print("Hello")

while False:
    print("My", end="")
    print("Name", end="")
    continue
    print("is", end="")
    break
    print ("chika-chika", end="")
    print("Slim Shady", end="")

age = 13

while age > 10:
    print("You are too old!", end="")
    if age == 13:
        break
    age += 1

print('')

age = 1

while age < 10:
    if age % 2 == 1:
        if age == 3:
            print("ding", end="")
        elif age == 4:
            print("dong", end="")
        elif age == 5:
            print("the", end="")
        print("which", end="")
    age += 1

print("is dead", end="")

print("")

num = 1
new_num = 0

while num < 10:
    for i in range(3):
        new_num += 1
    num += 2
print(new_num)

x = 10
my_list = ['Yaba', 'Daba', 'Doo']

while x < 13:
    for remark in my_list:
        print(remark, end="")
        x += 1

print('')

i = 6
while i <= 10:
    for j in range(3):
        i*=j+2
        print(j, end="")
        break
