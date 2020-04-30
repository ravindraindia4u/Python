"""
A binary tree is a tree which is characterized by any of the following properties:

It can be empty (null). It can contain a root node which contain some value and two subtree, left subtree and right
subtree, which are also binary tree. A binary tree is a binary search tree (BST) if all the non-empty nodes follows
both two properties:

If node has a left subtree, then all the values in its left subtree are smaller than the value of the current node.
If node has a right subtree, then all the value in its right subtree are greater than the value of the current node.

You are given N nodes, each having unique value ranging from [1, N], how many different binary search tree can be
created using all of them. """
node = int(input("Enter the number of node: "))


def factorial(number):
    fact = 1
    while number > 0:
        fact = fact * number
        number -= 1
    return fact


def totalNumberOfBinaryTree(node):
    a = factorial(2 * node)
    b = factorial(node + 1)
    c = factorial(node)
    total_num_of_bst = a // (b * c)
    return total_num_of_bst


print(f"Total number of binary search tree are: {totalNumberOfBinaryTree(node)}")
