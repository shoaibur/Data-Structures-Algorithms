import heapq

def distance_from_zero(point):
    return point[0]*point[0] + point[1]*point[1]

def kClosest(points)
      distances = [(-distance_from_zero(point), point) for point in points]
      heap = distances[:k]
      heapq.heapify(heap)
      for distance in distances[k:]:
          heapq.heappushpop(heap, distance)
      return [point for _,point in heap]
