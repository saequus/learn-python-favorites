# import bs4 as bs
# import urllib.request
#
# sauce = urllib.request.urlopen('https://pythonprogramming.net/parsememcparseface/')
# soup = bs.BeautifulSoup(sauce, features='html.parser')
# # for paragraph in soup.find_all('p'):
# # #     print(paragraph.text)
#
# # for url in soup.find_all('a'):
# #     print(url.get('href'))
#
# nav = soup.nav
# #
# # for item in nav.find_all('a'):
# #     print(item.get('href'))
#
# body = soup.body
#
# # for div in soup.find_all('div', class_='body'):
# # #     print(div.text)
#
# for div in soup.find_all('div', class_='body'):
#     print(div.text)


class Node():
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def levelOrderTraversal(root):

    if not root:
        return []

    queue = [(root, 0)]
    res = []
    while queue:
        node, depth = queue.pop()

        if depth > len(res) - 1:
            res.append([node.val])
        else:
            res[depth] += [node.val]

        if node.left:
            queue += [(node.left, depth + 1)]

        if node.right:
            queue += [(node.right, depth + 1)]

    return res


root = Node(1)
root.left = Node(2)
root.right = Node(2)
root.left.left = Node(3)
root.left.right = Node(4)
root.right.left = Node(4)
root.right.right = Node(3)
print(levelOrderTraversal(root))
