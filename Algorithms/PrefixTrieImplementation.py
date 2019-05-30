class AnotherTrie(object):
    def __init__(self):
        self.main = dict()

    def insert(self, word):
        node = self.main
        for val in word:
            if val not in node:
                node[val] = {}
            node = node[val]
        node['Flag_000'] = True


    def search(self, word):
        node = self.main
        for val in word:
            if val not in node:
                return False
            node = node[val]

        if 'Flag_000' not in node:
            return False
        else:
            return True

    def startsWith(self, prefix):
        node = self.main
        for val in prefix:
            if val not in node:
                return False
            node = node[val]

        return True


print(" - - - - - - - - ")
f = AnotherTrie()
f.insert('growth')
f.insert('start')
g = 'teleport'
f.insert(g)
print(f.startsWith('stt'))
print(f.startsWith('start'))
print(f.search('telep'))
print(f.search('teleport'))
print(f.main)




