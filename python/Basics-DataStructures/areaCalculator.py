print("==========================\nArea Calculator\n==========================")

shape = ""
while shape != "Quit":
    print("1) Rectangle\n2) Square\n3) Triangle\n4) Circle\n5) Quit")
    shape = input("Which Shape: ")

    if shape == "Rectangle":
        b = int(input("Enter Breadth: "))
        w = int(input("Enter Wdith: "))
        area = 2*(b*w)
        print("Area of Rectangle : ", area)

    elif shape == "Square":
        s = int(input("Enter Side: "))
        area = 4*s
        print("Area of Square: ", area)

    elif shape == "Triangle":
        b = int(input("Enter Breadth: "))
        h = int(input("Enter Height: "))
        area = (1/2) * (b*h)
        print("Area of Triangle: ", area)
    
    elif shape == "Circle":
        r = int(input("Enter Radius: "))
        area = 3.14 * (r**2)
        print("Area of Circle: ", area)
    
    elif shape == "Quit":
        break

    else:
        print("Invalid")
