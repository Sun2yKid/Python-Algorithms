"""
前缀树，字典树
"""

from collections import defaultdict


class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.is_word = False

    def __repr__(self):
        return 'Trie(%r, %r)' % (dict(self.children), self.is_word)


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def __repr__(self):
        return '%s' % self.root

    def insert(self, words):
        node = self.root
        for w in words:
            node = node.children[w]
        node.is_word = True

    def search(self, words):
        node = self.root
        for w in words:
            node = node.children[w]
            if not node:
                return False
        return node.is_word

    def startswith(self, prefix):
        node = self.root
        for c in prefix:
            node = node.children[c]
            if not node:
                return False
        return True


trie_obj = Trie()
for word in ('hello', 'world', 'good', 'go'):
    trie_obj.insert(word)
print(trie_obj)

word_1 = trie_obj.search('world')
print(word_1)
word_2 = trie_obj.search('word')
print(word_2)
word_3 = trie_obj.startswith('hell')
print(word_3)


import string
string.ascii_uppercase