class Node:
	def __init__(self, data, choices):
		self.data = data
		self.choices = choices
		self.child = []

def newNode(key, choices):
	temp = Node(key, choices) 
	return temp

def LevelOrderTraversal(root):
	if root == None:
		return

	q = []
	q.append(root)
	while len(q) != 0:

		n = len(q)
		while n > 0:
			p = q[0]
			q.pop(0)
		
			print(p.data)
			for i in p.choices:
				print("\tChoice: \t", i)
			for i in range(len(p.child)):
				q.append(p.child[i])
			n -= 1
		print()

def Game(root):
        next_node = -1
        if root == None:
                return
        print(root.data)
        if len(root.choices) == 0:
        	print("End of Story")
        	return
        for i in root.choices:
                print("\t >>  ", i)
        while True:
                choice = input("Enter your choice: ")
                if choice in root.choices:
                        print("Valid Choice")
                        cnt = 0
                        for i in root.choices:
                                if i == choice:
                                        print("You Entered: ", choice)
                                        break
                                cnt +=1
                        next_node = cnt
                        break
                else:
                        print("Invalid Choice")
        Game(root.child[next_node])
if __name__ == '__main__':
	root = newNode("Do you yield?", ["Yes", "No"])
	(root.child).append(newNode("You have yield. Should you release the hostage", ["Yes", "No"]))
	(root.child).append(newNode("You didn't yield. Who do you shoot?", ["Sheriff", "Police", "Yourself"]))
	(root.child[0].child).append(newNode("You release the Hostages. You went to jail", []))
	(root.child[0].child).append(newNode("You didn't release the Hostages. The police shot you", []))
	(root.child[1].child).append(newNode("You shot the sheriff. The police shot you", []))
	(root.child[1].child).append(newNode("You shot the police. The sheriff shot you", []))
	(root.child[1].child).append(newNode("You shot yourself. It's over", []))

	
	#print("Level order traversal Before Mirroring")
	#LevelOrderTraversal(root)
	Game(root)
