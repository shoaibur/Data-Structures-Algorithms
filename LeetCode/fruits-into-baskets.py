def fruits_into_baskets(tree):
    if len(tree) <= 2: return len(tree)
    
    basket = {}
    max_fruit = 0
    start = 0
    
    for i, fruit in enumerate(tree):
        basket[fruit] = basket.get(fruit, 0) + 1
        while len(basket) > 2:
            basket[tree[start]] = basket.get(tree[start]) - 1
            if basket[tree[start]] == 0:
                basket.pop(tree[start])
            start += 1
        max_fruit = max(max_fruit, i-start+1)
    return max_fruit
