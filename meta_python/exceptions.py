def divide_by(a , b):
    return a / b

# Step 1

'''
try:
    ans = print(divide_by(40,0))

except Exception as e:
    print("Some thing went wrong! ",e)
'''

# Step 2

try:
    ans = divide_by(54,0)
    print(ans)

except ZeroDivisionError as e:
    print(e, ",We cannot divide by zero")
except Exception as e:
    print(e, ",Some thing went wrong!")
    
  #  print(e.__class__)

# Exception Exercise 

# Starter Code 

items = [1,2,3,4,5]
try:
    item =  items[6]
    print(item)
except IndexError as e:
    print(e,", Item does not exist in the list")
except Exception as ex:
    print("Item does not exist in the list, ",ex)

  

   