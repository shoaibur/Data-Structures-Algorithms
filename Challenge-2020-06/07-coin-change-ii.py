# You are given coins of different denominations and a total amount of money. 
# Write a function to compute the number of combinations that make up that amount. 
# You may assume that you have infinite number of each kind of coin.
# Inputs: coins = [1,2,5] and amount = 6
'''
k = range(0, amount+1)
IF amount >= coin:
    combinations[k] += combinations[k - coin]
    
k---------------> 0  1  2  3  4  5  6
coin [ ]--------> 1  -  -  -  -  -  -
coin [1]--------> 1  1  1  1  1  1  1
coin [2]--------> 1  1  2  2  3  3  4
coin [5]--------> 1  1  2  2  2  4  5
'''
