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
