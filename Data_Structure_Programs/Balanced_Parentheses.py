"""
Take an Arithmetic Expression such as
(5+6)∗(7+8)/(4+3)(5+6)∗(7+8)/(4+3) where parentheses are used to order the
performance of operations. Ensure parentheses must appear in a balanced
fashion.
"""


# Creating object for stack class
from Data_Structure_Programs.stack import Node, Stack

obj = Stack()
expression = input("Enter any expression: ")


# Function for Balanced Parentheses
def balanced_parentheses(expression):
    open_parentheses = "({["
    closed_parentheses = ")}]"
    for brackets in expression:
        if brackets in open_parentheses:
            bracket = Node(brackets)
            obj.push(bracket)
        elif brackets in closed_parentheses:
            obj.pop()
    if obj.is_empty():
        print("Given expression is balanced!!")
    else:
        print("Given expression is not balanced!!")


balanced_parentheses(expression)
