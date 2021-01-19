#int -> bool
#returns True if the starting number reduces to 42 otherwise False
def bears(n):
    """A True return value means that it is possible to win
    the bear game by starting with n bears. A False return value means
    that it is not possible to win the bear game by starting with n bears.
    """
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
            return False
        reduced = n - multi
        if bears(reduced) == True:
            return True
    if n % 5 == 0:
        reduced = n - 42
        if bears(reduced) == True:
            return True
    else:
        return False
