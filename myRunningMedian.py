#!/usr/bin/python3
from math import ceil
class Element:
	def __init__(self, data):
		self.data = data
		self.leftsubtree_count = 0 # node itself
		self.rightsubtree_count = 0 # node itself
		self.right = None
		self.left = None

class BST_median:
	def __init__(self):
		self.root = None

	def insert(self,data):
		element = Element(data)
		if(self.root==None):
			self.root=element

		else:
			tempPointer = self.root
			while(1):
				# tempPointer.subtree_count = tempPointer.subtree_count + 1
				if(data < tempPointer.data):
					tempPointer.leftsubtree_count = tempPointer.leftsubtree_count + 1
					if(tempPointer.left != None):

						tempPointer = tempPointer.left
					else:
						tempPointer.left = element
						break
				else:
					tempPointer.rightsubtree_count = tempPointer.rightsubtree_count + 1
					if(tempPointer.right != None):
						tempPointer = tempPointer.right

					else:
						tempPointer.right = element
						break

	def get_median(self):
		number_of_items = self.root.leftsubtree_count + self.root.rightsubtree_count + 1
		if(number_of_items %2 == 0):
			median_indexes = [number_of_items/2,number_of_items/2 + 1]
			median_elements = [None, None]
		else:
			median_indexes = [ceil(number_of_items/2)]
			median_elements = [None]

		if(DEBUG): print(number_of_items, median_indexes)
		tempPointer = self.root
		node_index = tempPointer.leftsubtree_count + 1
		node_index_before_right_subtree = 0
		while(None in median_elements):
			if(DEBUG): print("index:",node_index, "data",tempPointer.data)
			if(node_index in median_indexes):
				median_elements[median_indexes.index(node_index)]=tempPointer.data
			index_to_look_for = median_elements.index(None) if None in median_elements else -1
			if(DEBUG): print(index_to_look_for, median_indexes[index_to_look_for], median_indexes,median_elements)
			if(index_to_look_for != -1):
				if(median_indexes[index_to_look_for] < node_index): #when we are done with 0... we go for 1 :)
					tempPointer = tempPointer.left
					if(tempPointer != None):
						node_index = tempPointer.leftsubtree_count + node_index_before_right_subtree + 1
				else:
					tempPointer = tempPointer.right
					node_index_before_right_subtree = node_index
					if(tempPointer != None):
						node_index = node_index + tempPointer.leftsubtree_count + 1

		median = sum(median_elements)/len(median_elements)
		return median

	def test_inorder(self, head):
		if(head!=None):
			self.test_inorder(head.left)
			print(head.data, head.leftsubtree_count, head.rightsubtree_count)
			self.test_inorder(head.right)

DEBUG=0
myBST_median = BST_median()
number_of_items = eval(input())
while(number_of_items > 0):
	item = eval(input())
	myBST_median.insert(item)
	if(DEBUG): myBST_median.test_inorder(myBST_median.root)
	print("%0.2f" % myBST_median.get_median())
	number_of_items = number_of_items - 1
