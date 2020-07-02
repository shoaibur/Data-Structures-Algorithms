def prisonAfterNDays(cells, N)
    if N == 0: return cells
    day1cells = nextday(cells)
    cells = day1cells
    N -= 1
    count = 1
    while N > 0:
        cells = self.nextday(cells)
        if cells == day1cells:
            N = N % count
        count += 1
        N -= 1
    return cells

def nextday(cells):
    day = [0] * len(cells)
    for i in range(1, len(cells)-1):
        day[i] = 1 - cells[i-1] ^ cells[i+1]
    return day
