def convert_to_celsius(fahrenheit):
    '''(number) -> number

    Return the number of Celsius degrees equivalent to fahrenheit degrees.

    >>> convert_to_celsius(32)
    0.0
    >>> convert_to_celisus(212)
    100.0
    '''
    return (fahrenheit - 32) * 5 / 9


def colder_temperature(temp1, temp2):
    '''(number, number) -> number

    Return the colder of the two temperatures, temp1 (degrees Celsius)
    and temp2 (degrees Fahrenheit), in degrees Celsius.
    '''

    temp2_celsius = convert_to_celsius(temp2)
    return min(temp1, temp2_celsius)

def usa_city_temperature(str):
    '''(str) -> number

    Return the temperature of a U.S. city in (degreees fahrenheit)

    '''
    Atlanta = 72

    return Atlanta

def announce_location(str):
    return (str)
    
