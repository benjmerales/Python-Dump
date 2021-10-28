class Node:
	def __init__(self, data):
		self.left = None
		self.right = None
		self.data = data

	def PrintTree(self):
		if self.left:
			self.left.PrintTree()
		print(self.data, end = ", ")
		if self.right:
			self.right.PrintTree()
		print(self.data, end = ", ")

	def insert(self, data):
		if self.data:
			if data < self.data:
				if self.left is None:
					self.left = Node(data)
				else:
					self.left.insert(data)
			elif data > self.data:
				if self.right is None:
					self.right = Node(data)
				else:
					self.right.insert(data)
		else:
			self.data = data


root = Node(50)
root.insert(10)
root.insert(40)
root.insert(80)
root.insert(60)
root.PrintTree()