def report_status(scheduled_time, estimated_time):
    ''' (number, number) -> str
    A flight was scheduled to arrive at a particular time
    and it is now estimated to arrive at another time. 
    Write a function that return the flight status: 
    on time, early or delayed.

    Precondition: 0.0 <= schedule_time < 24 and
    0.0 <= estimated_time < 24

    >>> report_status(14.3, 14.3)
    'on time'
    >>> report_status(12.5, 11.5)
    'early'
    >>> report_status(9.0, 9.5)
    'delayed'
    '''

    
    if scheduled_time == estimated_time:
        return 'on time'
    elif scheduled_time > estimated_time:
        return "early"
    else :
        return 'delayed'



def is_even(num):
    '''(int) -> bool

    Return whether num is even.
    >>> is_even(4)
    True
    >>> is_even(77)
    False
    '''

    return num % 2 == 0
##    if num % 2 == 0:
##        return True
##    else:
##        return False


def same_abs(num1, num2):
    ''' (number, number) -> bool
    Return True if and only if num1 and num2 have the same absolute value.
    >>> same_abs(12.5, -12.5)
    True
    >>> same_abs(3, 4.5)
    False
    '''
    return abs(num1) == abs(num2)
##    if abs(num1) == abs(num2):
##        return True
##    else:
##        return False




def inhospitable_weather(temp):
    ''' (number) -> bool      
    Return True if and only if the given temperature in degrees Celsius is unpleasant (too hot or too cold).  
    >>> inhospitable_weather(20)
    False
    '''

    return temp <12 or temp >28 

##    if temp > 28:
##        return True
##    elif temp < 12:
##        return True
##    else:  
##        return False
