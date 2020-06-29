def findJudge(N, trust)
    people = range(1,N+1)
    trusters = [pair[0] for pair in trust]
    trusted = [pair[1] for pair in trust]
    judge = list(set(people) - set(trusters))
    
    # There must be only one judge only
    if len(judge) != 1: return -1
    
    # Everyone but judge must trust judge
    judge = judge[0]
    count = 0
    for person in trusted:
        count += person == judge
    return (judge if count==N-1 else -1)
