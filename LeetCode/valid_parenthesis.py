def is_valid(parenthesis):
    n = len(parenthesis)
    if n == 0 or n % 2 or parenthesis[0] in ')}]':
        return False
    pairs = {')':'(', '}':'{', ']':[''}
    stack = []
    for p in parenthesis:
        if p in '({[':
            stack.append(p)
        elif stack == []:
            return False
        else:
            popped = stack.pop()
            if pairs[p] != popped:
                return False
    return True
    
