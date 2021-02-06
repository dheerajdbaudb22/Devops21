import random


names_string = input("give me everybody's names, Sperated by a comma.\n ")
names = names_string.split(", ")
num_items = len(names)
random_choice = random.randint(0, num_items - 1)
person_to_pay = names[random_choice]
print(person_to_pay + "  is going to pay bill for today. ")
prrint(person_to_pay)

