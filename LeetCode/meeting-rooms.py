# Can join all meetings?
def meeting_rooms(intervals):
    if not intervals: return None
    if len(intervals) == 1: return True
    intervals.sort()
    out = [intervals[0]]
    for i in range(1, len(intervals)):
        overlap = overlaps(out[-1], intervals[i])
        if overlap: return False
        out.append(intervals[0])
    return True
  
def overlaps(x, y):
    overlap = min(x[1],y[1]) - max(x[0],y[0]) > 0
    return overlap
