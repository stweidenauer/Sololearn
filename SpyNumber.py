correct_input = False;

while not correct_input:
    input_string = input("Please enter Number to check: ")
    try:
        a = int(input_string)
        correct_input = True
    except ValueError:
        print("That is not a number!")

add = int(input_string[0])
mul = int(input_string[0])
for i in range(1, len(input_string)):
    add = add + int(input_string[i])
    mul = mul * int(input_string[i])

if add == mul:
    print("Addition: ", add)
    print("Multiplication: ", mul)
    print("Is a Spynumber:")
else:
    print("Addition: ", add)
    print("Multiplication: ", mul)
    print("Is not a Spynumber:")
