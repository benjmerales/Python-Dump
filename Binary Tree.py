class Node:
	def __init__(self,data = None):
		self.data = data
		self.left = None
		self.right = None
def insert(root, key):
	if root is None:
		return Node(key)
	else:
		if root.data == key:
			return root
		elif root.data < key:
			root.right = insert(root.right, key)
		else:
			root.left = insert(root.left, key)
	return root

def inorder(root):
	if root:
		inorder(root.left)
		print(root.val)
		inorder(root.right)


r = Node(30)
r = insert(r, 20)
r = insert(r, 40)
r = insert(r, 60)
r = insert(r, 35)
inorder(r)