loyalty_customer = True
total_bill = 2224


if loyalty_customer and total_bill > 200:
    # give 20% discount 
    total_bill = total_bill - (float(total_bill) / 100) * 20

elif total_bill > 100:
    total_bill = total_bill - (float(total_bill) / 100) * 10

else :
    print("Sorry no Discount")

print("Total bill:" , float(total_bill))    








