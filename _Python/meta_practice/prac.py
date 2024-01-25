# file = open('../newtest', mode = 'r')

# data = file.readlines()

# print(data)

with open('newfile.txt', 'w') as file:
    file.write('This is a new file of farhan waseer created!')


file = open('first.txt',  'r')

data = file.readlines()

print(data)