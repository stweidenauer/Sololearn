def make_integer(str_list):
    return int("".join(str_list))


correct_input = False
while not correct_input:
    incoming = input("Enter 4 Digit Number")
    try:
        a = int(incoming)
        if len(incoming) == 4:
            correct_input = True
        else:
            print("Please enter a 4(!) digit number!")
    except ValueError:
        print("This is not a number")

b = 0
while b != 7641:
    a_upwards = sorted(incoming)
    b_downwards = a_upwards[::-1]
    a = make_integer(a_upwards)
    b = make_integer(b_downwards)
    c = b - a
    print(b, " - ", a, " = ", c)
    incoming = str(c)
