import math

def check_number():
    while True:
        try:
            try_num = int(input("Enter a number: "))
            if try_num == 0:
                print("Please enter a non zero number")
            elif try_num % 2 == 0:
                print(f"{try_num} is even")
                break
            else:
                print(f"{try_num} is odd")
                break
        except ValueError:
            print("Invalid input. Please enter an integer.")




def calculator():
    print("Welcome to Calculator! Please choose a mathematical operation from 1-9")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exponentiation")
    print("6. Modulo")
    print("7. Pow")
    print("8. Logarithm")
    print("0. Exit")

    while True:
        operation = input("Enter your choice: ")
        first_num = int(input("Enter first number: "))
        second_num = int(input("Enter second number: "))
        if operation == "1":
            addition = first_num + second_num
            print(f"{addition}")
        elif operation == "2":
            subtraction = first_num - second_num
            print(f"{subtraction}")
        elif operation == "3":
            multiplication = first_num * second_num
            print(f"{multiplication}")
        elif operation == "4":
            division = first_num / second_num
            print(f"{division}")
        elif operation == "5":
            exponentiation = first_num ** second_num
            print(f"{exponentiation}")
        elif operation == "6":
            modulo = first_num % second_num
            print(f"{modulo}")
        elif operation == "7":
            power = first_num ** second_num
            print(f"{power}")
        elif operation == "8":
            result = math.log(first_num, second_num)
            print(f"log base {first_num} of {second_num} is {result}")
        elif operation == "0":
            break
        else:
            print("Invalid input. Please enter a valid input.")


def main():
    check_number()
    calculator()

main()
