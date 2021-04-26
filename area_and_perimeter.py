#!/usr/bin/env python3

# Created by: Cameron Carter
# Created on April 2021
# This program calculates the perimeter and area of a rectangle with
# inputted length and width

import math


def main():
    # This function calculates perimeter and area
    
    # Input
    length_of_rectangle = int(input("Enter the rectangle length (mm): "))
    width_of_rectangle = int(input("Enter the rectangle width (mm): "))
    
    # Process
    area_of_rectangle = length_of_rectangle * width_of_rectangle
    perimeter_of_rectangle = (2 * (length_of_rectangle + width_of_rectangle))
    
    # Output
    print("The area is {} mm².".format(area_of_rectangle))
    print("The perimeter is {} mm.".format(perimeter_of_rectangle))
    print("")
    print("Done.")


if __name__ == "__main__":
    main()
