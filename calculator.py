print("Welcome, Let's Make Your Calculation Simple!")
num_1 = int(input("What was the first number ?\n"))
num_2 = int(input("What was the Second Number ?\n"))
cal = input("What was your calculation symbol e.g +, -, and so on ?\n")
if cal == "+":
    print("Your Answer is: ")
    print(num_1 + num_2)
elif cal == "-":
    print("Your Answer is: ")
    print(num_1 - num_2)
elif cal  == "/":
    print("Your Answer is: ")
    print(round(num_1 / num_2, 2))
elif cal == "*":
    print("Your Answer is: ")
    print(num_1 * num_2)
else:
    print("Calculation Error")