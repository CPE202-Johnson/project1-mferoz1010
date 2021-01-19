#int int -> str
#a recursive function that returns a string representing num in the base b
def convert(num, b):
    """Recursive function that returns a string representing num in the base b"""
    final_str = ''
    quotient = num // b
    remainder = num % b
    if quotient == 0:
        final_str += '1'
        return final_str
    else:
        if remainder > 9:
            remainder = chr(remainder + 55)
        final_str = str(convert(quotient, b)) + str(remainder)
        return final_str
    
    
