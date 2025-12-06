def area_rectangle(x, y):
    return x * y

def area_square(x):
    return x * x

def area_circle(x):
    return 3.14 * x * x

AREA = {
    "rectangle": area_rectangle,
    "square": area_square,
    "circle": area_circle
}

def calculate_area(shape, x, y=0):
    if shape == "rectangle":
        return AREA["rectangle"](x, y)
    else:
        return AREA[shape](x)
if __name__ == "__main__":
    print("Area of rectangle (5, 10):", calculate_area("rectangle", 5, 10))
    print("Area of square (4):", calculate_area("square", 4))
    print("Area of circle (3):", calculate_area("circle", 3))
