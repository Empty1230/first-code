'''import random
secret = random.randint(1, 100)
guess = 0
tries = 0
print("You need to guess the number from 1 to 100. You have 6 tries.")
while guess != secret and tries < 6:
    guess = int(input("What is your answer? "))
    if guess < secret:
        print("Too little!")
    elif guess > secret:
        print("Too much!")
    tries += 1
if guess == secret:
    print("You got it!")
else:
    print("No you are incorrect.")
'''



'''
grade = int(input("Write in your score 0-100"))
if grade >= 90 and grade <= 100:
    print("You got a 5🎉🎉🎉")
elif grade > 100:
    print("no stop lying")
elif grade >= 80:
    print("You got a 4😀😀😀")
elif grade >= 70:
    print("You got a 3😶😶😶")
else:
    print("You got a 2😡😡😡😡😡")
'''








'''
sale = int(input("How much does your items cost?"))
if sale <= 1000:
    print("your get a discount of 10%")
    sale = sale*0.9
else:
    print("you get a discount of 20%🎉🎉🎉")
    sale = sale*0.8
print("The cost of your shopping, ",sale)
'''



















'''
a = input("Who is it? ")
s = int(input("How old is... "))
if a == "female" and  s >= 10 and s <= 12:
    print("You are accepted into the team. ")
    print("😎😎😎😎😎😎")
else:
    print("Sorry we can't let you on the team. ")
    print("😡😡😡😡😡")
'''





'''
a = input("Gender")
if a == "female ":
    b = int(input("Age? "))
    if b >= 10 and b <= 12:
        print("You can be on the team! ")
    else:
        print("No you cant be on the team ")
else:
    print("You can't be on the team.😥😥😥 ")
'''











'''
a = int(input("What is your age? "))
if a < 18:
    print("Sorry you can't get this. ")
else:
    print("Ok im going to bring it ")
    w = float(input("How much money do you have? "))
    if w < 1.99:
        print("Sorry you need more money")
    else:
        print("Ok you can get it")
'''










'''
a = input("What material do u want us to use? ")
if a == "brick" or a == "concrete" or a == "cement":
    print("ok")
else:
    print("Sorry we don't have that right now ")
'''
























"""
import time
for i in range(10, 0, -1):
    print(i)
    time.sleep(1)
print("START!")
"""








'''
import time
import pygame
pygame.init()
pygame.mixer.music.load("START.mp3")
for i in range(0, 10, 1):
    print(i)
    time.sleep(1)
print("START!")
pygame.mixer.music.play()
'''







'''
a = int(input("What number do you need to multiply with? "))
for i in range(1,11):
    print(a, 'x' , i, '=' , a*i)
'''

'''
a = int(input("What number do you need to multiply with? "))
i = 1
while i < 11:
    print(a, 'x' , i, '=' , a*i)
    i = i + 1
'''





















'''
i = 1
a = int(input("What number do you need to multiply with? "))
b = int(input("until how much do you want it to multiply?"))
while i < b + 1:
    print(a, 'x' , i, '=' , a*i)
    i = i + 1
'''





'''
for multiplier in range(1, 11):
    for i in range(1, 11):
        print(i, 'x', multiplier, "=", i * multiplier)
    print()
'''




'''
for i in range(5):
    for j in range(3):
        print('* ', end=' ')
    print()
'''











'''
import time
a = int(input("Pick a number. "))
for i in range(a, 0, -1):
    print(i, end="" )
    for star in range(0, i):
        print('* ', end='')
    time.sleep(1)
    print()
print("START!")
'''







'''
k = 100
while k != 0:
    print(k)
    k = k - 1
'''























'''
answer = 1
cars = []
while answer != 0:
    print("""Choose An Option:
                1 - Add Car
                2 - Delete Car
                3 - A List Of All The Cars
                4 - Find a Car
                5 - Sort The Garage
                0 - Leave """)
    answer = int(input())
    if answer == 1:
        car = input("What Car Do You Want To Add *write the name of the car*")
        cars.append(car)
        print("The Car Has Been Added")
    elif answer == 2:
        car = input("What Car Do You Want To Delete?")
        cars.remove(car)
        print("The Car Has Been Removed")
    elif answer == 3:
        for x in cars:
            print(x)
            print("The List Has Been Shown")
    elif answer == 4:
        car = input("Which Car Are You Looking For?")
        if car in cars:
            print("This Car Is In The Garage.")
        else:
            print("The Car Your Looking For Isn't Here.")
    elif answer == 5:
        cars.sort()
        print("The Garage Has Been Sorted.")
'''







'''
numbers = [99, 100, 101, 102]
for n in numbers:
    print(n)
'''
















'''
def calculatetax(price, tax_rate):
    total = price + (price*tax_rate)
    return total
my_price = float(input("Write In The Price: "))
total_price = calculatetax(my_price, 0.2)
print("price = ", total_price, " Price Added Value")
'''








'''
def numbers(first, second):
    total = first + second
    return total
n = int(input("Which is the first number?: "))
b = int(input("Which is the second number?: "))
print(numbers(n, b))
'''



















'''
def apple(a):
    total = 0
    for x in a:
        total = total + x
    return total
b = [2 ,67, 38, 29, 9, 14, 20, 25, 98, 48, 68]
print(apple(b))
'''
















'''
def apple(a):
    max = 0
    for x in a:
        if max > x:
            max = x
    return max
b = [2455 ,2123, 223, 212, 2365, 212, 224, 2333, 222, 22, 21]
print(apple(b))
'''













'''
def give(president, line):
    total = president + line
    return total
print(give(5, 9))
'''








'''
cars = ["toyota", "folkswagen", "audi", "tesla" ]
car = input("What Car Do You Want To Add🙄🙄🙄")
def add_car(cars, car):
    cars.append(car)
    return cars
print(add_car(cars, car))
'''


'''
words = {"Anthon":"122"}
words["Hi"] = "123"
def change(phonebook):
    print("whos number do you want to change")
    save = input()
    if save in phonebook:
        answer = input("what do you want to change it into?")
        phonebook[save] = answer
def delete(phonebook):
    print("Whos number do you want to delete?")
    save = input()
    if save in phonebook:
        print("Are you sure? y/n")
        answer = input()
        answer = answer.lower()
        if answer == "y" or answer == "yes":
            del phonebook[save]
            print(save," Deleted")
        else:
            print("Delete has been cancelled.")
def find(phonebook):
    print("Whos number do you want to find?")
    save = input()
    if save in phonebook:
        print(phonebook[save])
    else:
        print("This phone number isn't saved.")
def menu():
    print()
    print("phonebook")
    print("1 - find the phone number")
    print("2 - add the phone number")
    print("3 - show the phone number")
    print("4 - delete the phone number")
    print("5 - Change the phone number")
    print("6 - leave")
    answer = int(input("write in the chosen: "))
    return answer
def add_phone(phonebook):
    name = input("whats the name: ")
    number = input("whats the number: ")
    if name in phonebook:
        print("this name is already in use")
    else:
        phonebook[name] = number
def show(phonebook):
     for key in sorted(phonebook.keys()):
         print(key,",",phonebook[key])
choice = 0
while choice != 6:
    choice = menu()
    if choice == 3:
        show(words)
    elif choice == 1:
        find(words)
    elif choice == 2:
        add_phone(words)
    elif choice == 4:
        delete(words)
    elif choice == 5:
        change(words)
'''














