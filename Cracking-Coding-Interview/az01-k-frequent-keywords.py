# Given a list of reviews, a list of keywords and an integer k. Find the most popular k keywords in 
# order of most to least frequently mentioned. The comparison of strings is case-insensitive.
# Multiple occurances of a keyword in a review should be considred as a single mention.
# If keywords are mentioned an equal number of times in reviews, sort alphabetically.

# Input:
k = 2
keywords = ["anacell", "betacellular", "cetracular", "deltacellular", "eurocell"]
reviews = [
  "I love anacell Best services; Best services provided by anacell",
  "betacellular has great services",
  "deltacellular provides much better services than betacellular",
  "cetracular is worse than anacell",
  "Betacellular is better than deltacellular.",
]
# Output:
# ["anacell", "betacellular"]


def k_frequent_keywords(reviews, keywords, k):
    keywords = set(keywords)
    d = {}
    for review in reviews:
        for word in set(review.lower().split()):
            if word in keywords:
                d[word] = d.get(word, 0) + 1
    heap = [(-count, word) for word, count in d.items()]
    import heapq
    heapq.heapify(heap)
    return [heapq.heappop(heap)[1] for i in range(k)]

# Test
k_frequent_keywords(reviews, keywords, k)
