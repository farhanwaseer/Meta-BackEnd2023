#### Calculate bill tex

def calculate_tex(bill, tex_rate):
    return (bill * tex_rate) / 100

print("Calculate tex: ",calculate_tex(345,14) )

mybill = int(input("Enter Bill: "))
texRate = int(input("Enter Tex rate %: "))

print("Calculate tex 2 : ",calculate_tex(mybill,texRate))
