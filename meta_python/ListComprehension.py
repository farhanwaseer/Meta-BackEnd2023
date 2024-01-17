"""
List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list.

Example:

Based on a list of fruits, you want a new list, containing only the fruits with the letter "a" in the name.

Without list comprehension you will have to write a for statement with a conditional test inside: """

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newList = [] 

for x in fruits:
    if "a" in x:
        newList.append(x)

print(newList)

sentences = [
    "The sun rises in the east.",
    "Cats love to nap in the sun.",
    "Pizza is my favorite food.",
    "Birds sing in the morning.",
    "Rainbows are beautiful after rain.",
    "Books open new worlds.",
    "Coffee wakes me up.",
    "Stars twinkle in the night sky.",
    "Flowers bloom in spring.",
    "Time flies when you're having fun.",
    "Laughter is contagious.",
    "Music soothes the soul.",
    "Dogs wag their tails when happy.",
    "Smiles can brighten someone's day.",
    "The moon glows at night.",
    "Dreams inspire creativity.",
    "Ice cream melts quickly in the sun.",
    "Hugs convey warmth and comfort.",
    "Kindness costs nothing.",
    "The ocean waves are calming.",
    "Sunsets are magical moments.",
    "Learning is a lifelong journey.",
    "Balloons float in the air.",
    "Butterflies symbolize transformation.",
    "Snowflakes are unique.",
    "Clouds form interesting shapes.",
    "Exercise energizes the body.",
    "The wind whispers through the trees.",
    "Friends make life richer.",
    "Every day is a new opportunity."
]

newbList = []

for b in sentences:
    if "the" in b:
        newbList.append(b)

#print(newbList) 

for nb in newbList:
    print(nb)
#print(len(newbList), "sentences" )    
print("{} sentences".format(len(newbList)))



