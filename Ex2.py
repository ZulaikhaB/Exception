try:
    num1, num2 = eval(input("Enter two numbers,seprated by a coma : "))
    result = num1 / num2
    print("Result is", result)
#using multiple except block for differnt type of error 

except ZeroDivisionError:
    print("Divison by zero is error !!")

except SyntaxError: 
    print("comma is missing. Enter numbers separted by comma like this 1, 2")

except: 
    print("Wrong input")

else:
    print("No exceptions")

finally:
    print("This will execute no matter what")