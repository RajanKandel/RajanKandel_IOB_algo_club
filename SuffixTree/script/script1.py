class Node:
    """A node in the suffix tree."""
    
    def __init__(self):
        self.children = {}  # Dictionary mapping characters to child nodes
        self.suffixes = []  # List of suffix indices ending at this node


class SuffixTree:
    """Implementation of a suffix tree data structure."""
    
    def __init__(self, text):
        """
        Create a suffix tree for the given text.
        
        Args:
            text (str): The text for which to create the suffix tree.
        """
        self.text = text
        self.root = Node()
        self._build_tree()
    
    def _build_tree(self):
        """Build the suffix tree by inserting all suffixes of the text."""
        # Add a unique terminal character to ensure all suffixes end at a leaf
        text = self.text + "$"
        n = len(text)
        
        # Insert each suffix into the tree
        for i in range(n):
            self._insert_suffix(text[i:], i)
    
    def _insert_suffix(self, suffix, suffix_index):
        """
        Insert a suffix into the tree.
        
        Args:
            suffix (str): The suffix to insert.
            suffix_index (int): The starting index of the suffix in the original text.
        """
        current = self.root
        
        for char in suffix:
            if char not in current.children:
                current.children[char] = Node()
            current = current.children[char]
            current.suffixes.append(suffix_index)
    
    def search(self, pattern):
        """
        Search for a pattern in the text.
        
        Args:
            pattern (str): The pattern to search for.
            
        Returns:
            list: List of starting indices where the pattern occurs in the text.
        """
        current = self.root
        
        # Traverse the tree according to the pattern
        for char in pattern:
            if char not in current.children:
                return []  # Pattern not found
            current = current.children[char]
        
        # Return all suffix indices that contain this pattern
        return [idx for idx in current.suffixes if self.text[idx:idx+len(pattern)] == pattern]
    
    def visualize(self, node=None, prefix="", is_last=True, depth=0):
        """
        Visualize the suffix tree structure.
        
        Args:
            node (Node, optional): Current node in visualization. Defaults to root.
            prefix (str, optional): Prefix for the current line. Defaults to "".
            is_last (bool, optional): Whether current node is the last child. Defaults to True.
            depth (int, optional): Current depth in the tree. Defaults to 0.
            
        Returns:
            str: A string representation of the tree structure.
        """
        if node is None:
            node = self.root
            result = "Suffix Tree:\n"
        else:
            branch = "└── " if is_last else "├── "
            result = prefix + branch
            prefix += "    " if is_last else "│   "
        
        # Add node details if not root
        if depth > 0:
            char_on_edge = list(node.children.keys())[0] if node.children else "$"
            result += f"{char_on_edge} (suffixes: {node.suffixes})\n"
        else:
            result += "root\n"
        
        # Recursively visualize children
        items = list(node.children.items())
        for i, (char, child) in enumerate(items):
            result += self.visualize(child, prefix, i == len(items) - 1, depth + 1)
            
        return result

# Example usage
if __name__ == "__main__":
    text = "banana"
    tree = SuffixTree(text)
    
    print(f"Original text: {text}")
    print(tree.visualize())
    
    # Search examples
    patterns = ["na", "ana", "ban", "nan", "xyz"]
    for pattern in patterns:
        occurrences = tree.search(pattern)
        if occurrences:
            print(f"Pattern '{pattern}' found at positions: {occurrences}")
        else:
            print(f"Pattern '{pattern}' not found")