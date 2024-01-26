# file = open('../newtest', mode = 'r')

# data = file.readlines()

# print(data)

# with open('newfile.txt', 'w') as file:
#     file.write('This is a new file of farhan waseer created!')


# file = open('first.txt',  'r')

# data = file.readlines()

# print(data)

# file.close()



try:
    with open('newtest.txt', 'r') as file:
        data = file.readlines()
        print(data)
except FileNotFoundError as e:
    print(e, "Error")

with open('newtest.txt',  'a') as file:
    file.writelines(["\n This is new line for file created 2","\n This is new line 3, \nthis is line 3 for view"])

with open('newtest.txt', 'r') as file:
    data = file.readlines()
    # print(data)


for fda in data:
  print(fda)