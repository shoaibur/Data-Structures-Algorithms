# Given n ropes of different lengths, we need to connect these ropes into one rope. We can connect only 2 ropes 
# at a time. The cost required to connect 2 ropes is equal to sum of their lengths. The length of this connected 
# rope is also equal to the sum of their lengths. This process is repeated until n ropes are connected into a 
# single rope. Find the min possible cost required to connect all ropes.

# Min cost to connect ropes
def heapify(heap):
    for i in range(len(heap)-1,-1,-1):
        parent_index = i // 2
        if heap[parent_index] < heap[i]: # Max heap sorts elements, max to min
            heap[parent_index], heap[i] = heap[i], heap[parent_index]
    return heap

def connect_ropes(ropes):
    sticks = heapify(ropes)
    total_cost = 0
    while len(ropes)>=2:
        curr_cost = ropes.pop() + ropes.pop()
        ropes.append(curr_cost)
        total_cost += curr_cost
    return total_cost


# Using heapq package
import heapq
def connect_ropes(ropes):
    heapq.heapify(ropes)
    total_cost = 0
    while len(ropes) >= 2:
        curr_cost = heapq.heappop(ropes)+heapq.heappop(ropes)
        heapq.heappush(ropes,curr_cost)
        total_cost += curr_cost
    return total_cost

# Test
connect_ropes([20, 4, 8, 2]) # output 54
