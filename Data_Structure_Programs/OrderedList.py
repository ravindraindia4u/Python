"""  Ordered_list
 Read a List of Numbers from a file and arrange it ascending Order in a Linked List.
 Take user input for a number,
 if found then pop the number out of the list else insert the number in appropriate position
"""
from Data_Structure_Programs.LinkedList import LinkedList, Node

""" creating object for linked list..."""
obj = LinkedList()


def main():
    """ open the file and read the file"""
    fname = input("Enter the file name: ")
    file = open(fname, 'r')
    lines_of_file = file.readlines()
    for line in lines_of_file:
        number = line.lower().split()
        for num in number:
            element = Node(int(num))
            """Adding number into linkedlist into sorted order"""
            obj.sortList(element)
    print("The number in the linked list--->")
    """ Printing all the element into the list"""
    obj.traverse()
    """taking input from user to search the number into list"""
    search = int(input("Enter the number to search into list:"))
    if obj.search(search):
        """The searched number is found in list then deleteing the number into the list"""
        obj.delete_word(search)
        print("The number you searched is deleted :")
    else:
        """ The searched number is not found in the list then number is to be added to list """
        add_num = Node(search)
        obj.sortList(add_num)
        print("The word you searched is added to list!!")
    obj.traverse()


"""calling the function"""
main()
