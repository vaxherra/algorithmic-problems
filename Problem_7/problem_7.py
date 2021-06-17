from collections import defaultdict
import re


class RouteTrieNode:
    """Represents a single node in the Trie"""

    def __init__(self, handler=None):
        """Initialize the node with children plus a handler"""
        self.children = defaultdict(RouteTrieNode)
        self.handler = handler

    def insert(self, path_step, handler):
        """Inserting a single path_step from a full path to a RouteTrieNode with a passed handler

        :param path_step: a single path step in a path, without the "/" separators
        :type path_step: string

        :param handler: a simplified handler
        :type handler: string
        """
        if path_step not in self.children:
            self.children[path_step] = RouteTrieNode(handler)


class RouteTrie:
    """RouteTrie stores routes and their associated handlers"""

    def __init__(self, handler=None):
        """ Initialize the trie with an root node and a handler, this is the root path or home page node"""
        self.root = RouteTrieNode(handler=handler)

    def insert(self, step_list, handler):
        """Add a path to a trie

        :param step_list: a pre-formatted path in the form of list
        :type step_list: list of strings (path_steps)

        :param handler: a handler for a path
        :type handler: string
        """

        node = self.root
        for step in step_list:
            node = node.children[step]
        node.handler = handler

    def find(self, prefix):
        """Find the RouteTrieNode handler that represents the prefix

        :param prefix: a pre-formatted path prefix
        :type prefix: list of strings

        :return: a handler for a given prefix
        :rtype: string (default handler type)
        """

        node = self.root

        for path_step in prefix:
            if path_step in node.children:
                node = node.children[path_step]
            else:
                return RouteTrieNode().handler  # a default empty page handler

        return node.handler


class Router:
    """  The Router class wraps the Trie and handle"""

    def __init__(self, root_handler="root handler", not_found_handler="404 page not found"):
        """Initialize a new RouteTrie for holding routes.
        Add a default handler for missing page '404 page not found' by default"""
        self.trie = RouteTrie(handler=root_handler)
        self.not_found_handler = not_found_handler

    def add_handler(self, path, handler):
        """Adds a handler for a path in the form of unformatted string"""
        if path:  # guard against Null path, we assume handler could be Null
            path_list = self.split_path(path)
            self.trie.insert(step_list=path_list, handler=handler)

    def lookup(self, path):
        """Lookup path and return the associated handler, or a default "not found handler" if
        path has no associated handler with it.

        :param path: string representing a path, each path step separated by "/"
        :type path: string
        :return: a handler if found for a given path, or a default "not_found_handler"
        """

        path_list = self.split_path(path)
        return_handler = self.trie.find(prefix=path_list)

        if return_handler:
            return return_handler
        else:
            return self.not_found_handler

    @staticmethod
    def split_path(path):
        """ Prepares a list of path steps for a given input path string.

        :param path: string with '/' characters splitting the path steps
        :type path: string

        :return: a list of path steps: without empty steps, no lingering '/' characters
        :rtype: list
        """

        if type(path) != str:
            return []

        # replace multiple occurrences of "/" with just one,
        # i.e. "page1//page2///page3" -> "page1/page2/page3"
        path = re.sub('/+', '/', path)
        path = path.split("/")  # form a list of path steps
        path = [x.lower() for x in path if x != ""]  # filter out empty strings, convert to lowercase

        return path


# --- PROVIDED TEST CASES
print("--- PROVIDED TEST CASES")
# create the router and add a route
router = Router(root_handler="root handler", not_found_handler="not found handler")
router.add_handler("/home/about", "about handler")  # add a route

# some lookups with the expected output
print(router.lookup("/") == "root handler")  # should print 'root handler'
# True
print(router.lookup("/home") == "not found handler")  # should print 'not found handler'
# True
print(router.lookup("/home/about") == "about handler")  # should print 'about handler'
# True
print(router.lookup("/home/about/") == "about handler")  # should print 'about handler'
# True
print(router.lookup("/home/about/me") == "not found handler")  # should print 'not found handler'
# True

# --- MY TEST CASES
print("--- MY TEST CASES")

# CASE #1 (edge case): lookup method with Null (None) path on a default router, returns "root handler"
myRouter = Router()
print(myRouter.lookup(path=None)=="root handler")
# True

# CASE #2 (edge case): add handler method on a Null Path and Null handler DOES NOT impact root handler
myRouter.add_handler(path=None,handler=None)
print(myRouter.lookup(None)=="root handler")

# CASE #3: text proper path splitting
my_handler = "my charming handler"
myRouter.add_handler(path="////some////unformatted////path////",handler=my_handler)
print(myRouter.lookup('some/unformatted/path')==my_handler)
# True
