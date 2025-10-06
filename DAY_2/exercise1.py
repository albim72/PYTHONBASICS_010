# Functions for rectangle calculations

def area_of_rectangle(width, height):
    """Return the area of a rectangle."""
    return width * height


def perimeter_of_rectangle(width, height):
    """Return the perimeter of a rectangle."""
    return 2 * (width + height)


def describe_rectangle(width, height):
    """Return both area and perimeter as a tuple."""
    area = area_of_rectangle(width, height)
    perimeter = perimeter_of_rectangle(width, height)
    return area, perimeter


# --- Main program ---

if __name__ == "__main__":
    width = 5
    height = 3

    # Call all three functions
    area = area_of_rectangle(width, height)
    perimeter = perimeter_of_rectangle(width, height)
    description = describe_rectangle(width, height)

    # Display the results
    print(f"Width: {width}, Height: {height}")
    print(f"Area: {area}")
    print(f"Perimeter: {perimeter}")
    print(f"Description (area, perimeter): {description}")

