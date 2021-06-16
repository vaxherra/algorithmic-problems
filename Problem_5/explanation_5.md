# Explanation

Autocomplete with tries.

First, a Trie or a Prefix Tree is implemented. In particular we have:
- A `Trie` class that contains the root node (empty string)
- A `TrieNode` class that exposes the general functionality of the Trie, like inserting a word or finding the node which represents a prefix.

Secondly, a recursive function `suffixes()` is implemented in the `TrieNode` class. Given a particular `TrieNode` at any level, it recurrently traverses all the nodes in children nodes, and its all sub-children. If a given node represents a node, adds the aggregated suffix to the return list.

--

# Complexity analysis

## Time complexity

1. `insert` method: `O(n)`, `n` - length of the word (number of characters)


    Since we're iterating over the characters of the input word, the time complexity is linear.
   

2. `find` method: `O(n)`, `n` - length of the prefix
   

    In the worst case scenario we have to iterate over all characters in the provided `prefix` variable. Hence linear time `O(n)`.
   

3. `suffixes` - `O(n)`, `n` - number of nodes in a trie
    
    
    In the worst case senario, i.e. being at the root node of a Trie, we'd have to traverse through every node of the trie once. Hence a linear time in the number of nodes.

    Number of nodes is non-trivially proportional to the number of words and their length.


## Space complexity

1. `insert` - `O(n)` - where `n` is the total number of words in a tree


    The size of the Trie would grow in a non-trivial way with the words added. In other words - it depends on the statistical properties of words added, like: are the words completely unique, or do they share many suffixes? 

   

2. `find` - `O(1)`

   
   Regardless of the trie size, we do not create any new data structures, and return already existing fragment of a trie.
   In the worst case scenario `find(prefix='')`, we return the root of the trie node. 


3. `suffixes` - `O(n)`, `n` - number of nodes in a trie
   
   The function builds and stores all the suffixes of valid words in the children nodes of a `TrieNode`. 
   In the worst case scenario all of the suffixes are words, hence `O(n)`, where `n` is the number of children nodes in a given `TrieNode`