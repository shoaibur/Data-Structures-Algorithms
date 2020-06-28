def reorderLogFiles(logs):
        logs.sort(key=sorting_key)
        return logs
    
def sorting_key(log):
    ids, rest = log.split(' ', 1)
    return (0, rest, ids) if rest[0].isalpha() else (1,)
