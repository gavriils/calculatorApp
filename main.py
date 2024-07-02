import sys
import numpy as np

def calculate_square_root(number):
    return np.sqrt(number)

# import numpy as np
 
# def calculate_square_root(number):
#    return np.sqrt(number)
 
# if __name__ == "__main__":
#    number = float(input("Enter a number to calculate its square root: "))
#    print(f"The square root of {number} is {calculate_square_root(number)}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python app.py <number>")
        sys.exit(1)

    try:
        number = float(sys.argv[1])
        print(f"The square root of {number} is {calculate_square_root(number)}")
    except ValueError:
        print("Please provide a valid number.")
        sys.exit(1)

