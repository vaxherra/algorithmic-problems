# Explanation
## HTTPRouter using a Trie. 

An HTTPRouter is implemented using a Trie. Trie contains part of the HTTP path at each node, building from the root node. In this simplified exercise, the handlers are simple strings, characterizing each Trie node.

This HTTPRouter class initializes with a trie that holds the routes, and their associated handlers. 

A method `add_handler` for adding a handler to a particular is implemented. It calls directly the `insert` method of a trie which traverses the root trie nodes, until it reaches the last path step, and then sets the handler. The children of a RootTrieNode is implemented as a `defaultdict` that simplifies the traversal. 

Finally, a method `lookup` calls a trie method `find` that returns a handler for a particular path. It traverses the `RouteTrie` and returns a handler. In the body of the `lookup` method, we check whether a non-null handler was returned. If a null handler is returned, the `Router` returns a `not_found_handler`. 

---

# Complexity analysis
The complexity analysis is similar to `problem 5`, as we're operating on a Trie. Here I am going to discuss the `Router` method complexities.

## Time complexity
- `add_handler` is `O(n)` - where `n` is the path length (not input path STRING length!)
  
    `split_path` is `O(n)` since we're iterating over each path_step, similarly `trie.insert` method depends on the path length. 

- `lookup` is `O(n)` - where `n` is the path length (not input path STRING length!)

    Similarly to `add_handler` we call `split_path` in the `lookup` method of a router. This takes `O(n)`. Then, the `lookup` method calls `find` on a trie, which iterates over each path step, so `O(n)`. 

## Space complexity
- `add_handler` is `O(n)` - where `n` is the path length (not input path STRING length!)

  The `split_path` creates a new structure (list) proportional to `n` (number of path steps), and trie `insert` method in the worst case `n` children nodes that need to be stored. This is `O(n)` 

- `lookup` is `O(n)` - where `n` is the path length (not input path STRING length!).

  Similarly, as above `split_path` is `O(n)`, but the trie `find` method does not need any auxiliary data structure, beyond already defined trie. This simplifies to `O(n)`.