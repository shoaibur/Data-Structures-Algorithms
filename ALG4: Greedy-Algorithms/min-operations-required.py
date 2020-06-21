def min_operations(target):
    """
    Return number of steps taken to reach a target number
    input: target number (as an integer)
    output: number of steps (as an integer)
    """
    operation = 0
    while target > 0:
        if target % 2 == 0:
            target = target // 2
        else:
            target = target - 1
        operation += 1
    return operation
