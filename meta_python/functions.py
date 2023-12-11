#### Calculate bill tex

def calculate_tex(bill, tex_rate):
    return round((bill * tex_rate) / 100, 2)

print("Calculate tex: ",calculate_tex(345,14) )

mybill = int(input("Enter Bill: "))
texRate = int(input("Enter Tex rate %: "))

print("Calculate tex 2 : ",calculate_tex(mybill,texRate))

### Marks to percentage 

def calculate_marks(total, obtain):
    return (obtain * 100 / total)

total_marks = int(input("Total Marks : "))
obtain_marks = int(input("Obtain Marks : "))

print("Your Marks percentage is ", calculate_marks(total_marks,obtain_marks))
