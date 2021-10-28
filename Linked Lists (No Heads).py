class Node:
	def __init__(self, dataval=None):
		self.dataval = dataval
		self.nextval = None

class SLinkedList:
	def __init__(self):
		self.headval = None
	def size(self):
		cnt = 0
		current = self.headval
		while current is not None:
			current = current.nextval
			cnt += 1
		return cnt
	def listprint(self):
		printval = self.headval
		while printval is not None:
			print(printval.dataval)
			printval = printval.nextval
	def atBeginning(self,newdata):
		NewNode = Node(newdata)
		NewNode.nextval = self.headval
		self.headval = NewNode
	def atEnd(self,newdata):
		NewNode = Node(newdata)
		if self.headval is None:
			self.headval = NewNode
			return
		laste = self.headval
		while laste.nextval:
			laste = laste.nextval
		laste.nextval = NewNode
	def inBetween(self, middle_node, newdata):
		if middle_node is None:
			print("Specified Node is empty")
			return
		NewNode = Node(newdata)
		NewNode.nextval = middle_node.nextval
		middle_node.nextval = NewNode
	def removeNode(self, Removekey):
		HeadVal = self.head
		if HeadVal is not None:
			if HeadVal.data == Removekey:
				self.head = HeadVal.next
				HeadVal = None
				return
		while HeadVal is not None:
			if HeadVal.data == Removekey:
				break
				prev = HeadVal
				HeadVal = HeadVal.next
		if HeadVal is None:
			return
		prev.next = HeadVal.next
		HeadVal = NewNode                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                

list1 = SLinkedList()
list1.headval = Node("Mon")
list1.atEnd("Tue")
list1.atEnd("Wed")
list1.atEnd("Fri")
list1.inBetween(list1.headval.nextval.nextval, "Thu")
print("Size of Linked List: ", list1.size())
list1.listprint()