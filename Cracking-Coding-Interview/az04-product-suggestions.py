# Given an array of strings products and a string searchWord. We want to design a system that 
# suggests at most three product names from products after each character of searchWord is typed. 
# Suggested products should have common prefix with the searchWord. If there are more than three 
# products with a common prefix return the three lexicographically minimums products.
# Return list of lists of the suggested products after each character of searchWord is typed. 

# Input: 
products = ["mobile","mouse","moneypot","monitor","mousepad"]
searchWord = "mouse"
# Output:
[["mobile","moneypot","monitor"],
 ["mobile","moneypot","monitor"],
 ["mouse","mousepad"],
 ["mouse","mousepad"],
 ["mouse","mousepad"]]


def product_suggestion(products, searchWord):
    products.sort()    
    # Use two iter to hold the target words between
    start, end, ret = 0, len(products)-1, []
    for n_th, c in enumerate(searchWord):
        # Check between start and end to prevent unusable move
        # Check lenth of current "product string" to prevent "search word" longer than "product string"
        while start <= end and (products[start][n_th] < c if len(products[start])>n_th else True):
            start += 1
        while start <= end and (products[end][n_th] > c if len(products[end])>n_th else True):
            end -= 1

        # Append at most three element array
        ret.append(products[start:start+3] if end > start+1 else products[start:end+1])
    return ret

# Test
product_suggestion(products, searchWord)
