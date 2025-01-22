from image_classes import Square, Rectangle, Canvas



# Function that prints the main menu
def menu():
    print("MATH PAINTER MAIN MENU")
    print("\n1. Draw a square on the canvas")
    print("2. Draw a rectangle on the canvas")
    print("3. Create the image")
    print("\nPlease choose one of the above options: ")

print("First, lets create the canvas for drawing our shapes on it.")
canvas_width = int(input("Give the canvas width: "))
canvas_height = int(input("Give the canvas height: "))
print("Let's input all the necessary parameters for the color of the canvas")
canvas_red = int(input("Give the intensity of red (integer from 0 to 255): "))
canvas_green = int(input("Give the intensity of green (integer from 0 to 255): "))
canvas_blue = int(input("Give the intensity of blue (integer from 0 to 255): "))
cnv = Canvas(canvas_width,canvas_height,[canvas_red,canvas_green,canvas_blue])


while True:
    menu()
    option = int(input(">"))
    # option 1: Draw a square.
    # User will be asked to give its top left corner position,
    # its side and its color
    if option == 1:
        print("Give the coordinates of the top left corner of the square:")
        axis_x = int(input("Give the x coordinate: "))
        axis_y = int(input("Give the y coordinate: "))
        square_side = int(input("Give the side of the square: "))
        print("Declaring the color of the square...")
        square_red = int(input("Give the intensity of red (integer from 0 to 255): "))
        square_green = int(input("Give the intensity of green (integer from 0 to 255): "))
        square_blue = int(input("Give the intensity of blue (integer from 0 to 255): "))
        sqr = Square(axis_x, axis_y, square_side, [square_red, square_green, square_blue])
        sqr.draw(cnv)
    # option 2: Draw a rectangle
    # User will be asked to give its top left corner position,
    # its width and height and its color
    elif option == 2:
        print("Give the coordinates of the top left corner of the rectangle:")
        axis_x = int(input("Give the x coordinate: "))
        axis_y = int(input("Give the y coordinate: "))
        rectangle_width = int(input("Give the width of the rectangle: "))
        rectangle_height = int(input("Give the height of the rectangle: "))
        print("Declaring the color of the rectangle...")
        rectangle_red = int(input("Give the intensity of red (integer from 0 to 255): "))
        rectangle_green = int(input("Give the intensity of green (integer from 0 to 255): "))
        rectangle_blue = int(input("Give the intensity of blue (integer from 0 to 255): "))
        rect = Rectangle(axis_x, axis_y, rectangle_width, rectangle_height, [rectangle_red, rectangle_green, rectangle_blue])
        rect.draw(cnv)
    # option 3: Create the image and exit the loop
    elif option == 3:
        cnv.make('image')
        break
