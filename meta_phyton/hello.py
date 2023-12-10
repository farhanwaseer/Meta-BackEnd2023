print("hello world farhan")

x = str(3)
y = int(3)
z = float(3)

print(x)
print(y)
print(z)

# using casting 

w = str(20)
e = int(34)
r = float(21)
print(w)
print(e)
print(r)

q = 34
print(q)

q = float(34)
print(q)

# using type(x,y,z) function

print(type(x))
print(type(e))
print(type(q))

x, y, z = "Orange", "Banana", "Cherry"

print(x)
print(y)
print(z)


q, w, e = "Farhan", "Ahmed", "Waseer" 

print(q)
print(w)
print(e)

print(q,w,e)

a = s = d = "Red Light"

print(a)
print(s)
print(d)

# unpacking 

fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

x, y, z = "Orange", "Banana", "Cherry"

print(x)
print(y)
print(z)
print(10,y)

print("//////////////////")

Name = ["Farhan", "Ahmed", "Waseer"]
q, w, e = Name

print(q)
print(w)
print(e)

print(q,w,e)
print(q + w + e)
print(Name)
print("//////////////////")

code =[ """ x, y, z = "Orange", "Banana", "Cherry"

print(x)
print(y)
print(z)
print(10,y)

print("//////////////////")

Name = ["Farhan", "Ahmed", "Waseer"]
q, w, e = Name

print(q)
print(w)
print(e)

print(q,w,e)
print(q + w + e)
print(Name)
""" ]
print(code)

x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc()


y = "every thing will be right"

def myMood():

    x = "Hope" 
    print(x,"let is " + y)
myMood()    

#///////////////////
thislist = ["apple", "banana", "cherry"]

thislist.append("orange")


print(thislist)

name = ["farhan", "ahmed", "waseer"]
name.clear()


name.append("sukkur")
name.insert(2,"karachi")
name.extend(thislist)

print(name)

thislist.extend(name)
thislist.remove("apple")
thislist.pop(2)
del thislist[4]
del name

print(thislist)

#/////////////////////
thislist = ["apple", "banana", "cherry"]

for x in thislist:
 print(x)
 
name = ["farhan","ahmed","waseer"]
for b in name:
  print(b)
  
txtx = """you can also loop through the list items by referring to their index number 
"""

txtx = txtx.split()
print(txtx)
print(len(txtx))

for i in range(len(txtx)):
  print(txtx[i])
  
i = 0 

while i < len(thislist):
  print(thislist[i])
  i = i + 1
print("""?????????????""")

[print(x) for x in thislist]

