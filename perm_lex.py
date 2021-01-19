#str -> list
#Returns a Python list of strings where each string represents a permutation of the input string
def perm_gen_lex(a):
    final_list = []
    if a == '':
        return []
    elif len(a) == 1:
        return [a]
    else:
        for char in a:
            simpler_a = a.replace(char, '')
            for perm in perm_gen_lex(simpler_a):
                final_list.append(char + perm)
        return final_list
