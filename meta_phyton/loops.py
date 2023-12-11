
#favorites = ['Creme Brulee', 'Apple Pie', 'Churros', 'Tiramisú', 'Chocolate Cake']

#for i in range(20):
  #  print("looop", i)

#for i in range(10):
 #   print("loop", i)
    
#for items in favorites:
 #   print("testing loops ", items)

#count = 0

#while count < len(favorites):
 #   print("testing loops", favorites[count])
  #  count += 1

#for idx, items in enumerate(favorites):
 #   print(idx, items)

# Controlling Loops

#for desserts in favorites:
 #   if desserts == "Tiramisú":
  #     print('Yes! One of my favorite desserts is', desserts)
   #    break
    
   # else:
    #    print('No sorry, not a dessert on my list')

#########################

# nested loops

# outerloop 

import time
start_time = time.time()

for i in range(1000):
    # inner loop
    for j in range(100):
        print(0, end = " ")
    
print(round((time.time() - start_time), 2))   