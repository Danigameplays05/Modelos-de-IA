import turtle as tu
import re
import docx

# Open the Word document
data = docx.Document("Source//tulips.docx")

# Initialize lists to store the coordinate tuples and color tuples
coordinates = []
colour = []

# Loop through each paragraph in the document
for i in data.paragraphs:
    try:
        # Define regular expressions to match the desired patterns
        patron = r'[-+]?\.\d*\.\d*(?:[eE][-+]?\d+)?'
        patron_coord = r'\(' + patron + r' ?, ?' + patron + r'\)'
        patron_color = patron_coord + r' ?, ?' + patron + r'\)'

        # Search for the coordinate pattern
        match_coord = re.search(patron_coord, i.text)
        if match_coord:
            # Extract the coordinate tuple
            coord = tuple(map(float, re.findall(patron, match_coord.group())))
            coordinates.append(coord)

        # Search for the color pattern
        match_color = re.search(patron_color, i.text)
        if match_color:
            # Extract the color tuple
            col = tuple(map(float, re.findall(patron, match_color.group())))
            colour.append(col)

    except Exception as e:
        print(f"An error occurred: {e}")

# Use the extracted tuples to draw a shape using the turtle module
screen = tu.Screen()
screen.bgcolor("white")

# Create a turtle object
my_turtle = tu.Turtle()
my_turtle.speed(10)

# Loop through the coordinate tuples and draw lines between them
for i in range(len(coordinates)):
    if i == 0:
        my_turtle.penup()
        my_turtle.goto(coordinates[i])
        my_turtle.pendown()
    else:
        my_turtle.penup()
        my_turtle.goto(coordinates[i])
        my_turtle.pendown()
        my_turtle.color(colour[i-1])
        my_turtle.forward(10)

# Close the turtle window
my_turtle.hideturtle()
tu.done()


