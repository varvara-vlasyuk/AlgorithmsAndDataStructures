
class TrieNode:
    def __init__(self):
        self.children: dict = {}
        self.end: bool = False

    def __str__(self):
        return self.children.__str__()


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, in_string: str):
        node = self.root
        for char in in_string:
            next_node = node.children.get(char)
            if next_node is None:
                next_node = TrieNode()
                node.children[char] = next_node
            node = next_node
        node.end = True

    def search(self, string: str) -> bool:
        node = self.root
        for char in string:
            next_node = node.children.get(char)
            if next_node is None:
                return False
            node = next_node

        return node.end is True

    def delete(self, string: str):
        node = self.root
        stack = []
        str_len = 0
        for char in string:
            next_node = node.children.get(char)
            if next_node is None:
                return
            stack.append(node)
            node = next_node
            str_len += 1

        if node.end is True:
            node.end = False
        else:
            return
        # starting from last letter link
        for i in range(str_len-1, -1, -1):
            char = string[i]
            next_node = stack[i].children.pop(char)
            if next_node.children == {}:
                del next_node







def test_trie():
    trie = Trie()
    trie.insert('APP')
    trie.insert('API')
    trie.insert('APIS')
    print(trie.search('AP'))
    trie.delete('AP')
    print(trie.search('AP'))
    print("ready")


test_trie()