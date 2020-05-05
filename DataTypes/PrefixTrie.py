class TrieNode:
	def __init__(self):
		self.children = [None]*100
		self.is_terminal = False


class Trie:
	def __init__(self):
		self.root = self.get_node()

	def insert(self, key):
		length = len(key)
		crawler = self.root
		for level in range(length):
			index = self.char_to_index(key[level])
			if not crawler.children[index]:
				crawler.children[index] = self.get_node()
			crawler = crawler.children[index]
		crawler.is_terminal = True

	def search(self, key):
		length = len(key)
		crawler = self.root
		for level in range(length):
			index = self.char_to_index(key[level])
			if not crawler.children[index]:
				return False
			crawler = crawler.children[index]
		return crawler and crawler.is_terminal is True

	def print_all_keys(self, node=None, prefix=None):
		if not node:
			node = self.root
		length = len(node.children)
		for level in range(length):
			index = node.children[level]
			if index:
				letter = self.index_to_char(level)
				if index.is_terminal:
					print(prefix + letter)
				else:
					prefix = prefix + letter if prefix else letter
					self.print_all_keys(node=index, prefix=prefix)

	@staticmethod
	def get_node():
		return TrieNode()

	@staticmethod
	def char_to_index(ch):
		return ord(ch) - ord('a')

	@staticmethod
	def index_to_char(index):
		return chr(index + ord('a'))


def main():
	ex_trie = Trie()
	ex_trie.insert('moon')
	ex_trie.insert('monday')
	ex_trie.insert('monitor')
	ex_trie.insert('molecule')
	ex_trie.insert('mule')
	print('Word "monitor" in trie: %s' % ex_trie.search('monitor'))
	print('Word "moonlight" trie: %s' % ex_trie.search('moonlight'))
	print('\nPrint out all keys in trie as a list:')
	ex_trie.print_all_keys()


if __name__ == '__main__':
	main()



