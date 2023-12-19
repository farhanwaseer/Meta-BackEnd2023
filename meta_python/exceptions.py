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



  

   