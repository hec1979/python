import math

def area(base, height):
        ''' (number, number) -> number

        Return the area of a triangle with given base and
        height.

        >>> area(10, 40)
        200.0
        >>> area(3.4, 7.5)
        12.75
        '''
        
        return base * height / 2

def perimeter(side1, side2, side3):
        '''(number, number, number) -> number

        Return the permiter of the triangle with sides of
        length side1, side2, side3.

        >>> permiter(3, 4, 5,)
        12
        >>> permiter(10.5, 6, 9.3)
        25.8
        '''
        
        return side1 + side2 + side3

def semiperimeter(side1, side2, side3):
        '''(numbers, number, number) -> float

        Return the semipermiter of a triangle with sides of
        length side1m side2, side3.
        
        >>> semipermeter(3, 4, 5)
        6.0
        >>> semiperimeter(10.5, 6, 9.3)
        12.9
        '''

        return perimeter(side1, side2, side3) / 2

def     area_hero (side1, side2, side3):
        ''' (number, number, number) -> float
        >>> area_hero(3, 4, 5)
        6.0
        >>> area_hero(10.5, 6, 9.3)
        27.73168584850189
        '''

        semi = semiperimeter(side1, side2, side3)
        area = math.sqrt(semi * (semi - side1) * (semi - side2) * (semi - side3))
        return area
        
        
