"""
Program: inner_functions_assignment.py
Author: Lily Ellison
Last date modified: 02/15/2023

The purpose of this program is to use inner functions to calculate area and perimeter for
rectangles. A list of measurement values is passed to the outer function that has inner
functions to calculate area and perimeter, which is then built into a string and returned
to main by the outer function. Main displays the results.
"""

def measurements(list_rec_meas):  #outer function
    """
    Function docstring:
    Accepts a list of rectangle measurements, passing these to inner functions, builds a string
    from inner function outputs, and returns the string to main
    :param list_rec_meas: list of measurements for the rectangle in question, passed to inner
            functions
    :returns a string with results from inner functions
    """
    def area(list_rec_meas):  #inner function 1
        """
        Function docstring:
        Accepts a list of rectangle measurements, determines if it is a square or a rectangle,
        calculates area, and passes area to measurements()
        :param list_rec_meas: list of measurements for the rectangle in question, used to
                determine type of rectangle and calculate area
        :returns a float for the area of the rectangle
        """
        values_in_list = len(list_rec_meas) #counts the number of values in the list
        if(values_in_list == 1): #selects for when there is one value
            side = list_rec_meas[0] #sets that one value to a side variable
            area = side*side #calculates area for square
        elif(values_in_list == 2): #selects for 2 values
            if(list_rec_meas[0] == list_rec_meas[1]): #checks to see if both values are the same
                side = list_rec_meas[0] #if they are the same, one will be a "side"
                area = side*side #and area for a square is calculated
            else:
                length = list_rec_meas[0] #if they are different values, one set to length
                width = list_rec_meas[1] #one set to width
                area = length*width #area for rectangle calculated
        return area #value returned to outer function

    def perimeter(list_rec_meas): #inner function to calculate perimeter
        """
        Function docstring:
        Accepts a list of rectangle measurements, determines if it is a square or a rectangle,
        calculates area, and passes perimeter to measurements()
        :param list_rec_meas: list of measurements for the rectangle in question, used to
                determine type of rectangle and calculate perimeter
        :returns a float for the perimeter of the rectangle
        """
        values_in_list = len(list_rec_meas) #counts the number of values in list
        SQUARE_PERIMETER_MULTI = 4 #set constants for calculations to avoid magic numbers
        REC_PERIMETER_MULTI = 2
        if(values_in_list == 1): #selects for one value (square)
            side = list_rec_meas[0] #sets side
            perimeter = SQUARE_PERIMETER_MULTI * side #uses constant to calculate perimeter
        elif(values_in_list == 2): #selects for two values
            if(list_rec_meas[0] == list_rec_meas[1]): #checks if both are equal (square)
                side = list_rec_meas[0] #repeats steps for square if so
                perimeter = SQUARE_PERIMETER_MULTI * side
            else: #if 2 different values
                length = list_rec_meas[0] #one set to length
                width = list_rec_meas[1] #one set to width
                perimeter = REC_PERIMETER_MULTI * (length + width) #perimeter calculated for rectangle
        return perimeter #value returned to outer function

    area_rectangle = "The area is: " + str(area(list_rec_meas)) #calls area function and turns result into a string
    perimeter_rectangle = "The perimeter is: " + str(perimeter(list_rec_meas)) #calls perimeter function and turns result into a string

    return area_rectangle + "\n" + perimeter_rectangle #returns string with line break in the middle

if __name__ == '__main__': #selects when to run (start of main)
    rectangle = [2.1, 3.4] #first list
    result = measurements(rectangle) #calls outer function with first list
    print(result) #displays results
    square = [3.5] #second list
    result = measurements(square) #calls outer function with second list
    print(result) # displays results

    """
Results:
    The area is: 7.14
    The perimeter is: 11.0
    
    The area is: 12.25
    The perimeter is: 14.0
    """