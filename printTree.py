class Node:
	def __init__(self):
		self.value = None
		self.left = None
		self.right = None

from collections import deque
def print_tree(root):
	print "=== start ===="
	q = deque()
	q.append(root)
	while len(q) > 0:
		put_back = deque()
		to_print = []
		while len(q) > 0:
			n = q.popleft()
			to_print.append(n.value)
			put_back.append(n)
		# print the level
		print ''.join(to_print)
		while len(put_back) > 0:
			n = put_back.popleft()
			if n.left is not None:
				q.append(n.left)
			if n.right is not None:
				q.append(n.right)
	print "=== done ===="

def test():
	a = Node()
	a.value = 'a'
	
	b = Node()
	b.value = 'b'
	
	c = Node()
	c.value = 'c'
	
	a.left = b
	a.right = c
	
	d = Node()
	d.value = 'd'
	
	e = Node()
	e.value = 'e'
	
	c.left = d
	c.right = e
	
	print_tree(a)

test()
	
			
		
		