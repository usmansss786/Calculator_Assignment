num1: int= int(input("Enter the first number:"))
num2:  int= int(input("Enter the second number:"))
print("press 1 for addition \nPress 2 for subtraction \nPress 3 for division \nPress 4 for multiplication")
choice =int(input("Enter the number between 1-4:"))
if choice == 1:
    print("The addition of given two number is :",num1+num2)
elif choice == 2:
    print("The subtraction of given two number is :",num1-num2)
elif choice == 3:
    print("The division of given two number is :",num1//num2)
elif choice == 4:
    print("The multiplication of given two number is :",num1*num2)
else: 
    print("Invalid choice")