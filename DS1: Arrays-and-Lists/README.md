Two basic type of arrays:

1) Python Lists
  * plist = [3, 8, 2, 5, 1, 7, 9]
  * Runtime:
    * Search: O(n)
    * Insert: O(n), prepend: O(n), append: O(1)
    * Delete: O(n), .pop(0): O(n), .pop(): O(1)
    * Retrieval: O(1)
    * Swap: O(1)
    * Reversal: O(n)
  * Space complexicity can be constant for each of the operations above.

2) Linked Lists
  * Each node mush have two methods:
    * value: indicating the value at the node
    * next: pointing to the next node
  * Runtime
    * Search: O(n)
    * Insert: O(n), prepend: O(1), append: O(n)
    * Delete: O(n)
    * Retrieval: O(n)
    * Swap: O(n)
    * Reversal: O(n)
  * Exercises
    * Create a linked list
    * Convert a python list to a linked list
    * Traverse a linked list or convert a linked to a python list
    * Write functions for: (i) search (ii) insert (iii) prepend (iv) append (v) delete
    * Swap two nodes
    * Reverse a linked list

Problems: Implement functions using python list and/or linked list:
  * Add one to the list
  * Rearrange elements such that all even numbers are after the odd numbers
  * Find the duplicate number in the array
  * Find a the maximum sum of a subarray in the array
  * Compute the elements of pascal triangle at n-th row
  * Given two integers i and j, keep every i values and then remove every j values and repeat the process for the entire array.
