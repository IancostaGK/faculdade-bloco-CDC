class TrieNode:
    def __init__(self):
        self.children = {}
        self.end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.end_of_word = True

    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.end_of_word

    def autocomplete(self, prefix):
        suggestions = []
        node = self.root
        for char in prefix:
            if char not in node.children:
                return suggestions
            node = node.children[char]
        self._find_words_with_prefix(node, prefix, suggestions)
        return suggestions

    def _find_words_with_prefix(self, node, prefix, suggestions):
        if node.end_of_word:
            suggestions.append(prefix)
        for char, child_node in node.children.items():
            self._find_words_with_prefix(child_node, prefix + char, suggestions)

    def list_words(self):
        words = []
        self._list_words_recursive(self.root, "", words)
        return words

    def _list_words_recursive(self, node, prefix, words):
        if node.end_of_word:
            words.append(prefix)
        for char, child_node in node.children.items():
            self._list_words_recursive(child_node, prefix + char, words)

trie = Trie()
palavras = ["python", "java", "javascript", "ruby", "c", "cplusplus", "swift"]
for palavra in palavras:
    trie.insert(palavra)

print("Palavras armazenadas na Trie:", trie.list_words())

busca = "py"
print("Sugestões para '{}':".format(busca), trie.autocomplete(busca))

busca = "jav"
print("Sugestões para '{}':".format(busca), trie.autocomplete(busca))

busca = "c"
print("Sugestões para '{}':".format(busca), trie.autocomplete(busca))

busca = "p"
print("Sugestões para '{}':".format(busca), trie.autocomplete(busca))

print("Existe 'python' na Trie?", trie.search("python"))
print("Existe 'java' na Trie?", trie.search("java"))
print("Existe 'c++' na Trie?", trie.search("c++"))
print("Existe 'swift' na Trie?", trie.search("swift"))
print("Existe 'php' na Trie?", trie.search("php"))
