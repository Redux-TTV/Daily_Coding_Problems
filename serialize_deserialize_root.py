#07/20/2018----------------------------------------------------------------------------------------------------
#Given the root to a binary tree, implement serialize(root), 
#which serializes the tree into a string, and deserialize(s), which deserializes the string back into the tree.
#For example, given the following Node class

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

#The following test should pass:

#node = Node('root', Node('left', Node('left.left')), Node('right'))
#assert deserialize(serialize(node)).left.left.val == 'left.left'

def serialize(root):
	print('serialize function')
	components = []

	def listLinkedNodes(root, components):
		components.append(root.val)
		if root.left:
			listLinkedNodes(root.left,components)
		if root.right:
			listLinkedNodes(root.right,components)

	listLinkedNodes(root, components)
	return '||'.join(components)


def deserialize(s):
	print('deserialize function')


if __name__ == '__main__':
	node = Node('root', Node('left',Node('left.left')), Node('right'))
	print(node.val, node.left.left.val, node.right.val)
	print(serialize(node))
	#deserialize(serialize(node))