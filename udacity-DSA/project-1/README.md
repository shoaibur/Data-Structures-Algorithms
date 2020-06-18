# Problem 1: LRU Cache
* Solution approach
  * Use hash map (python dict) of size equal to capacity, so search is in O(1) time.
  * Idea for get/put operations: keys of the python dict are stored in the order at which they were added, e.g. first added key is dict.keys()[0], and so on.
  * get() -- If the request exists in the map, pop it and then add the request to make it most recent.
  * put() -- If the request already in the map, pop it, otherwise if the map is already in capacity, pop the least recent request. Then, add the request to the map
* Complexity
  * Time: All operations are in O(1)
  * Space: For the hash map -- O(m), where m is the cache capacity.

# Problem 2: File Recursion
* Solution approach
  * Used os.listdir in a recursive way to find the files in a directory and it's sub-directories. If the files ends with the desired extension, print either the full path of the file or only the file name.
* Complexity
  * Time: The program looks for all files in directory, so run time is O(n), where n is the total number of files.
  * Space: Ignoring space requiremnt for printing, the program does not require any additional space, so it is O(1).
  
# Problem 3: Huffman Coding
* Solution approach
  * Dict --> heap --> tree map --> encode --> decode
* Complexity
  * Time: For creating the dict, runtime is O(n), where n is the number of characters in the message. Each heappop/heappush for the priority queue requires O(log(p)) runtime, where p is the number of unique characters. So, for all unique characters in dict, runtime is O(p log(p)). However, total number of characters/punctuations/numbers is fixed in English languate, so this runtime may be considered constant. In such case, the runtime will be O(n+m), where n is the number of characters in the message for encoding, and m is the number of bits in the message to be decoded.
  * Space: With same argument as in time complexity, the space required for the dict may considered constant. So, space complexity will be O(n+m) for encoding and decoding.
  
# Problem 4: Active Directory
* Solution approach
  * 
* Complexity
  * Time: O(n)
  * Space: 
  
# Problem 5: Blockchain
* Solution approach
  * 
* Complexity
  * Time: 
  * Space: 
  
# Problem 6: Union and Intersection
* Solution approach
  * Traverse the linked list and add the items into a hash map (similar to a counter of each item) for each linked list. Then traverse one map and:
    * Union: include the items into an array and then traverse the other map and if the item does not exists in the previous map, then inlcude the item into the array.
    * Intersection: see if the item also exist in the other map. If so, include that into an array.
  * Convert the array into linked list and return.
* Complexity
  * Time: Traversing two linked list is O(n+m). Traversing the hash mpas is alos O(n+m). Converting arrays into linked list is also O(n+m) worst case. So, overall runtime is O(n+m), where n and m are the sizes of the two linked lists.
  * Space: For storing arrays, we need O(n+m) space, ignoring the constant multiplier.
  
