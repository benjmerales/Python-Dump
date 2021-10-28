global count
def external():
	global count
	count = 1
	print("init", count)
	def internal():
		count+=1
		print("called" ,count)
		return
	internal()
	print("final", count)
	return

external()