def findClosestElements(arr, k, x):
    distances = [(-abs(x-num), -num) for num in arr]
    
    print(distances)
    
    heap = distances[:k]
    heapq.heapify(heap)
    
    for distance in distances[k:]:            
        heapq.heappushpop(heap, distance)
        
    return sorted( [-num for _, num in heap] )
