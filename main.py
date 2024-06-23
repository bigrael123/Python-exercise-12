value1 = float(input("Type the first value of your mathematical operation: "))
value2 = float(input("Type the second value of your mathematical operation: "))
print("Select the type of operation:")
print("1 - Addition")
print("2 - Subtraction")
print("3 - Division")
print("4 - Multiplication")
type_of_operation = int(input("Type the number of the operation: "))
if(type_of_operation > 4 or type_of_operation<1):
    print("Invalid operation.")
elif(type_of_operation == 1):
    print(f"Your operation result {value1} + {value2} = {value1 + value2}")
elif(type_of_operation == 2):
    print(f"Your operation result {value1} + {value2} = {value1 - value2}")
elif(type_of_operation == 3):
    print(f"Your operation result {value1} + {value2} = {value1 / value2}")
elif(type_of_operation == 4):
    print(f"Your operation result {value1} + {value2} = {value1 * value2}")
