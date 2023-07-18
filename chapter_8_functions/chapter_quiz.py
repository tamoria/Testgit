def rafiki(lion):
    print(lion + " " + "Oh yes, the past can hurt. \
          But the way I see it, \
          you can either run from it or learn from it")
    
rafiki("simba")

def dory(fish, minutes_since_last_talked):
    if minutes_since_last_talked > 10:
        print("Who are you?", end="")
    else:
        if fish == "Nemo":
            print("Just keep swimming", end="")
        else:
            print("I don't know you.", end="")
        
print(dory("Nemo", 90))

def emperor(word_a, word_b):
    my_string=("The {word_b} that blooms" + 
               "in adversity is the most" + 
               "rare and {word_a} of all.")
    return my_string

print(emperor('flower', 'beautiful'))



def emperor(word_a, word_b):
    my_string=("The "+word_b+" that blooms" + 
               "in adversity is the most" + 
               "rare and "+word_a+" of all.")
    return my_string

word_1 = 'flower'
word_2 = 'beautiful'

print(emperor(word_b=word_1, word_a=word_2))

def see_character(name, age, species="human"):
    print(name, age, species)

see_character('Ariel', 16,'mermaid')



x = 5
def some_func(x):
    print(x, end="")

print(x, end="")
some_func(1)
x = x - 1
print(x, end="")
some_func(1)

print('')

def fun_a(number):
    return number + 5

def fun_b(number):
    return number * 2

print(fun_a(fun_b(5)))


def do_something(a_list):
    my_string=""
    for element in a_list:
        my_string += element[0]
    return my_string
aladdin_characters = ['Jasmine', 'Aladdin', 'Fazahl', 'Abu', 'Razoul']
print(do_something(aladdin_characters))
                  
