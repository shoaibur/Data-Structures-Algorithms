def robot_return_origin(string):
    if len(string) == 0: return True
    if len(string) % 2: return False
    string = string.upper()
    up = string.count('U')
    down = string.count('D')
    left = string.count('L')
    right = string.count('R')
    if up != down or left != right:
        return False
    return True
    
