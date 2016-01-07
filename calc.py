def square_return(num):
        return num ** 2

def square_print(num):
        print("The square of num is", num ** 2)

def area(base, height):
    '''(number, number) -> number

     return the area of a triangle with dimensions base
     and height

     >>> area(10, 5)
     25.0
     >>> area(2.5, 3)
     3.75
     '''

    return base * height / 2

def announce_location(country):
	print (country)
	return country


def count_letters(str):

        return len(str)

def find_vowels(sentence):
        count = 0
        vowels = "aeiuoAEIOU"
        for letter in sentence:
            if letter in vowels:
                count += 1
        #print (count)
        return count

def find_consonants(sentence):
        count = 0
        consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
        for letter in sentence:
            if letter in consonants:
                count += 1
        #print (count)
        return count
        
def count_letters(word):
        return (count_vowels(word) + count_consonants(word))

def compare_length(country1, country2):
        return longer(get_capital(country1), get_capital(country2))
                      

        

        
