##EX5----------------
def get_color(color):
    Loop = True
    No_of_try = 1
    while Loop == True:
        color_input = (input("Enter the value for " + color +\
            " color for message(0 - 255): "))
        try:
            color_str = int(color_input)
            if (type(color_str) == int) and (color_str in range(256)):
                return color_str
            else: color_str = int("fail")
        except:
            if No_of_try <= 2:
                print("Please enter valid value(0-255) Tries left = ", (3 - No_of_try))
                No_of_try += 1
            else:
                Loop = False
                return 0