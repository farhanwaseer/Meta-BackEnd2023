employee_list = [
    (12345, "John", "Kitchen"),
    (12458, "Paul", "House Floor"),
    (13579, "Sarah", "Reception"),
    (14682, "Michael", "Maintenance"),
    (15824, "Emily", "Customer Service"),
    (16937, "David", "IT Department"),
    (17293, "Olivia", "Human Resources"),
    (18456, "Daniel", "Security"),
    (19758, "Sophia", "Marketing"),
    (20891, "Christopher", "Finance"),
    (21124, "Emma", "Housekeeping"),
    (22367, "Matthew", "Engineering"),
    (23478, "Ava", "Event Planning"),
    (24689, "William", "Front Desk"),
    (25901, "Isabella", "Legal"),
    (26134, "James", "Catering"),
    (27345, "Mia", "Logistics"),
    (28456, "Ethan", "Health and Safety"),
    (29768, "Amelia", "Training"),
    (30879, "Alexander", "Sales"),
]

# def get_employee(id):
#     for employee in employee_list:
#         if employee[0] == id:
#            return {"id": employee[0], "name": employee[1], "department": employee[2]}
        

# print(get_employee(24689))       

def print_employee_details(employee_id ):
    for employee in employee_list:
        if employee[0] == employee_id:
            print(f"Employee ID: {employee[0]}")
            print(f"Name: {employee[1]}")
            print(f"Department: {employee[2]}")
            return
    print(f"No employee found with ID {employee_id}")


# Print details for employee with ID 12458
print_employee_details(12458)
# print_employee_details(16977737)

