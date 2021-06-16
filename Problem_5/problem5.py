import collections


class TrieNode:
    """Represents a single node in the Trie"""

    # Initialize this node in the Trie
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.is_word = False

    # Add a child node in this Trie
    def insert(self, char):
        if char not in self.children:
            self.children[char] = TrieNode()

    def suffixes(self, suffix=''):
        """
        Recursive function that collects the suffix for all complete words below this point

        :param suffix: a suffix string
        :type suffix: string

        :return: a list of suffixes mat
        :rtype: list
        """

        results = []
        if not self.children:  # if the dict is empty, stop recursing
            return results

        for c, node in self.children.items():
            if node.is_word:
                results.append(suffix+c)

            results += node.suffixes(suffix=suffix+c)

        return results


class Trie:
    """The Trie itself containing the root node and insert/find functions"""

    # Initialize this Trie (add a root node)
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        """
        Add a word to the Trie

        :param word: a word to be added to the trie
        :type word: string

        :return: None
        """

        node = self.root

        # only strings are accepted
        if type(word) != str:
            return
        for c in word:
            node = node.children[c]

        node.is_word = True

    def find(self, prefix):
        """Find the trie node that represents the prefix

        :parameter prefix: a prefix string searched in a trie node
        :return: a trie node that represents the prefix (empty trie node if no prefix is found)
        :rtype: TrieNode
        """
        node = self.root

        if type(prefix) != str:
            return node

        for c in prefix:
            if c in node.children:
                node = node.children[c]
            else:
                return TrieNode()
        return node


# TEST CASES

MyTrie = Trie()
wordList1 = [
    "ant", "anthology", "antagonist", "antonym",
    "fun", "function", "factory",
    "trie", "trigger", "trigonometry", "tripod"
]
for word in wordList1:
    MyTrie.insert(word)


# CASE #1: calling suffixes on a root of a Trie, returns the word list
print(MyTrie.root.suffixes('') == wordList1)
# True

# CASE #2: find an "ant" prefix, and return all suffixes from the above MyTrie
#          check against a manually filtered list for elements that start with "ant" from which the three characters
#          are removed (also empty string is filtered out)
print(MyTrie.find("ant").suffixes() == [x[3:] for x in wordList1 if (x.startswith("ant") and x[3:] != '')])
# True

# EDGE CASES:
# CASE #3: (edge case): empty Trie suffixes at root is an empty list
empty_try = Trie()
print(empty_try.find('').suffixes() == [])
# True

# CASE #4 (edge case): Null and empty inputs - inserting None or '' (empty string) to a Trie, does nothing
# here, an empty trie, remains an empty trie - with empty list of suffixes at root node.
MyTrie2 = Trie()

for _ in range(10):
    MyTrie2.insert(None)
    MyTrie2.insert('')

print(MyTrie2.find('').suffixes() == [])
# True


# CASE #5 (edge case): Null input (None) to find method, returns the root node
print(MyTrie.find(None).suffixes() == wordList1)
# True
