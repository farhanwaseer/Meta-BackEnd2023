# Way 3 

with open('test.txt', 'r') as file:
    data = file.readlines()
    print(data)


# Way 2

'''

file = open('test.txt', 'r')

data = file.readlines()

print(data)

file.close()

'''
# Way 1

'''
file = open('test.txt', mode = 'r')

data = file.readlines()

print(data)

'''

