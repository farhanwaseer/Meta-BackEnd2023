# step 1

menu = {
    1: {"name": 'espresso',
        "price": 1.99},
    2: {"name": 'coffee', 
        "price": 2.50},
    3: {"name": 'cake', 
        "price": 2.79},
    4: {"name": 'soup', 
        "price": 4.50},
    5: {"name": 'sandwich',
        "price": 4.99}
}

### Step 7 Solution One --->

def calculate_subtotal(order):
    print('Calculating bill subtotal...')
    itprices = []
    itprices = [itemx["price"] for itemx in order]
    pri_list = list(itprices)
    pri_list = sum(pri_list)
    # print(pri_list)
    # print(type(pri_list)) 
    return pri_list
    


    
 #-------------------------->

 ### Step 8 Solution Two ---->
 
def calculate_tax(subtotal):
    print('Calculating tax from subtotal...')
    
    sum_tex = round((subtotal * 15) / 100, 2) 
    
    return sum_tex

### Step 9

def summarize_order(order):
    print_order(order)
    itprices = []
    itprices = [itemx["price"] for itemx in order]
    pri_list = list(itprices)
    pri_list = sum(pri_list)
    tex = round((pri_list * 15) / 100, 2)
    total = pri_list + tex
    
    names = []
    names = [item["name"] for item in order]

    return names, total

# Step 5 
def print_order(order):
    print('You have ordered ' + str(len(order)) + ' items')
    items = []
    items = [item["name"] for item in order]
    print(items)
    return order


# step 2

def display_menu():
    print("----- Menu -----")
    for selection in menu: 
        print(f"{selection}. {menu[selection]['name'] : <9} | {menu[selection]['price'] : >5}")
    print("done")    

# step 3

def take_order():
    display_menu()
    order = []
    count = 1
    for i in range(3):
        item = input('Select menu item number ' + str(count) + ' (from 1 to 5): ')
        count += 1
        order.append(menu[int(item)])
    return order
     

# step 4

def main():
    order = take_order()
    print_order(order)

    subtotal = calculate_subtotal(order)
    print("Subtotal for the order is: " + str(subtotal))

    tax = calculate_tax(subtotal)
    print("Tax for the order is: " + str(tax))

    subtotal = summarize_order(order)


# Step 6 

if __name__ == "__main__":
    main()


