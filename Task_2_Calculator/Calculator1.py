# Simple Calculator Program
# Task 2 - CodSoft Python Internship
class Calculator:
    def addition(self,a,b): 
        print("Result: ", a + b)
    def subtraction(self,a,b): 
        print("Result: ", a - b)
    def multiplication(self,a,b): 
        print("Result: ", a * b)
    def division(self,a,b): 
        if b == 0:
            print("Error: Divide by zero is not allowed!")
        print("Result: ", a / b)
    def ordinal_superscript(self,n):
        if n == 1:
            return "1ˢᵗ"
        else:
            return "2ⁿᵈ"

#Driver Code
cal = Calculator()
choice = 0
num1 =0
num2 =0

while(choice!=5):
    print("\n**********CALCULATOR**********")
    print("\n1. Addition")
    print("\n2. Subtraction")
    print("\n3. Multiplication")
    print("\n4. Division")
    print("\n5. Exit Application")
    choice= int(input("\nWhat Operation:: "))
        
    if choice in [1,2,3,4]:
        num1 = float(input(f"Enter the {cal.ordinal_superscript(1)} number: "))
        num2 = float(input(f"Enter the {cal.ordinal_superscript(2)} number: "))
            
    if choice == 1:
        cal.addition(num1,num2)
    elif choice == 2:
        cal.subtraction(num1,num2)
    elif choice == 3:
        cal.multiplication(num1,num2)
    elif choice == 4:
        cal.division(num1,num2)
    else:
        print("GOOD BYEE!!!")