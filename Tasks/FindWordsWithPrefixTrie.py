w = ['oath', 'ally', 'enemy']
b = [['o', 'b', 'j', 'e'],
     ['a', 't', 'b', 'n'],
     ['a', 'h', 'm', 'e'],
     ['l', 'l', 'y', 'u']]


g1 = [["a","b"],["c","d"]]
g2 = ["ab","cb","ad","bd","ac","ca","da","bc","db","adcb","dabc","abb","acb"]


def construct_trie(words):
    dtrie = {}
    for word in range(len(words)):
        node = dtrie
        for letter in words[word]:
            if letter not in node:
                node[letter] = {}
            node = node[letter]
        node['Flag_000'] = True
    return dtrie


def find_word(words, board):
    res = []
    for row in range(len(board)):
        for letter in range(len(board[row])):
            for word in words:
                print(word, row, letter)
                if word.startswith(board[row][letter]):
                    i = 0
                    condition = True
                    while i < len(word) - 2 and condition:
                        condition, row, letter = is_next_letter_good(board, row, letter, word, i)
                        i += 1
                    if i == len(word) - 2:
                        res.append(word)
    return res


def is_next_letter_good(board, y, x, word, n):

    for dy, dx in [
        [-1, 0], [0, 1], [0, -1], [1, 0]
    ]:
        if 0 <= dy + y < len(board) and 0 <= x + dx < len(board[0]):
            if n < len(word) - 1:
                if word[n + 1] == board[y+dy][x+dx]:
                    return True, dy + y, dx + x
    return False, dy + y, dx + dx


class TrieNode(object):
    def __init__(self):
        self.sons = {}
        self.word = None


class Trie(object):
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for ch in word:
            if ch not in node.sons:
                node.sons[ch] = TrieNode()
            node = node.sons[ch]
        node.word = word


class Solution(object):
    def findWords(self, board, words):

        self.res = set()
        trie = Trie()
        for word in words:
            trie.insert(word)

        for i in range(len(board)):
            for j in range(len(board[i])):
                self.search(board, i, j, trie.root)

        return list(self.res)

    def search(self, board, i, j, trienode):
        if board[i][j] not in trienode.sons:
            return

        node = trienode.sons[board[i][j]]
        if node.word != None:
            self.res.add(node.word)

        temp = board[i][j]
        board[i][j] = '#'
        for (x, y) in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
            if 0 <= x < len(board) and 0 <= y < len(board[0]):
                self.search(board, x, y, node)
        board[i][j] = temp


f = Solution()
print(f.findWords(b, w))
print(f.findWords(g1, g2))