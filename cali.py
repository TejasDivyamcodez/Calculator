print("Calculator")
print("-----------------------------------------------------------------")
print("Select from these:-")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
print("5. Integer Division")
print("6. Modulus")
print("7. Exponential")
print("-----------------------------------------------------------------")
user_input_1 = int(input("Pls enter the first value:\t"))
user_input_2 = int(input("Pls enter the second value:\t"))
op = input("pls enter the operator[1.+] [2.-] [3.*] [4./] [5.//] [6.**] : ")
if op == "+":
    print(f'Result:\n {user_input_1} + {user_input_2} = {user_input_1 + user_input_2}')
elif op == "-":
    print(f'Result:\n {user_input_1} - {user_input_2} = {user_input_1 - user_input_2}')
elif op == "*":
    print(f'Result:\n {user_input_1} * {user_input_2} = {user_input_1 * user_input_2}')
elif op == "/":
    print(f'Result:\n {user_input_1} / {user_input_2} = {user_input_1 / user_input_2}')
elif op == "//":
    print(f'Result:\n {user_input_1} // {user_input_2} = {user_input_1 // user_input_2}')
elif op == "**":
    print(f'Result:\n {user_input_1} ** {user_input_2} = {user_input_1 ** user_input_2}')
else:
    print(f'[Error]')
