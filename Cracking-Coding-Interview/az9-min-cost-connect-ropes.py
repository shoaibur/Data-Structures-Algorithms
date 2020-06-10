# Min cost to connect ropes
import heapq
def heapify(heap):
    for i in range(len(heap)-1,-1,-1):
        parent_index = i // 2
        if heap[parent_index] < heap[i]: # Max heap sorts elements, max to min
            heap[parent_index], heap[i] = heap[i], heap[parent_index]
    return heap

def connect_ropes(ropes):
    #heapq.heapify(ropes)
    sticks = heapify(ropes)
    total_cost = 0
    while len(ropes)>=2:
        #curr_cost = heapq.heappop(ropes)+heapq.heappop(ropes)
        #heapq.heappush(ropes,curr_cost)
        #total_cost += curr_cost
        curr_cost = ropes.pop() + ropes.pop()
        ropes.append(curr_cost)
        total_cost += curr_cost
    return total_cost

connect_ropes([20, 4, 8, 2])
