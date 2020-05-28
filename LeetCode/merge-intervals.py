def merge_intervals(intervals):
    if len(intervals) <= 1: return intervals
    intervals.sort()
    out = [intervals[0]]
    for i in range(1, len(intervals)):
        overlap, merged_interval = overlaps( out[-1], intervals[i] )
        if overlap:
            out[-1] = merged_interval
        else:
            out.append(intervals[i])
    return out

def overlaps(x, y):
    merged_interval = None
    overlap = min(x[1], y[1]) - max(x[0], y[0]) >= 0
    if overlap:
        merged_interval = ( min(x[0], y[0]), max(x[1], y[1]) )
    return overlap, merged_interval
