def valid_parenthesis(s):
    if len(s) == 0: return True
    if len(s) % 2: return False
    if s[0] in ')}]': return False

    maps = { '(':')', '{':'}', '[':']' }

    stack = []
    for p in s:
        if p in '({[':
            stack.append(p)
        elif len(stack) > 0:
            popped = stack.pop()
            if maps[popped] != p:
                return False
        else:
            return False
    return len(stack) == 0
