import random

# adjective1 = input("Adjective 1: ")
# adjective2 = input("Adjective 2: ")
# verb1 = input("Verb 1: ")
# verb2 = input("Verb 2: ")
#
# phrase = f"This cat is so {adjective1}. I would like to {verb1} it and {verb2} it. I'm very {adjective2}."
# phrase2 = f"I'm totally in love with this {adjective1} baby. It is so {adjective2}. Don't you want to {verb2}? Or do you want to {verb1} it."
# print (phrase)
# print (phrase2)

male_list = ['Petko',
             'Mike',
             'Grisa',
             'Niki',
             'Kiko',
             'Luigi'
             ]

female_list = ['Sarah',
             'Luiza',
             'Eliza',
             ]

all_list = male_list + female_list

A = {random.choice(all_list)}
F = {random.choice(female_list)}
M = {random.choice(male_list)}

phrase3 = f"{A} told me that {A} is in love with {A}."
phrase4 = f"Another day, I've heard in the corridor that {A} really likes {A}."
phrase5 = f"I saw {A} kiss {A}, another day {A} kissed {A}, and that is why {A} slapped {A}."
phrase6 = f"{M} is in love with {F}. I also think, that she is awesome."

print(phrase3)
print(phrase4)
print(phrase5)
print(phrase6)
