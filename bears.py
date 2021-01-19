#int -> bool
#returns True if the starting number reduces to 42 otherwise False
def bears(n):
    if n == 42:
        return True
    if n < 42:
        return False
    if n % 2 == 0:
        reduced = n//2
        if bears(reduced) == True:
            return True
    if n % 3 == 0 or n % 4 == 0:
        multi = int(str(n)[len(str(n))-1]) * int(str(n)[len(str(n))-2])
        if multi == 0:
            pass
        else:
            reduced = n - multi
            if bears(reduced) == True:
                return True
    if n % 5 == 0:
        reduced = n - 42
        if bears(reduced) == True:
            return True
    else:
        return False
