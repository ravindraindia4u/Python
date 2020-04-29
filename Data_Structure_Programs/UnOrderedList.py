"""Read the Text from a file, split it into words and arrange it as Linked List.
Take a user input to search a Word in the List
If the Word is not found then add it to the list, and if it found then remove the word from the List.
In the end save the list into a file
"""

from linkedlist import Linked_List
from linkedlist import Node

""" Creating object for linked list"""

obj=Linked_List()

def main1():
    """ open the file and read the file"""

    file=open( 'file1', 'r')
    lines_of_file=file.readlines()
    for singl in lines_of_file:
        words =singl.lower().split()
        for word in words:
            first=Node(word)
            """Inserting the element into linked list"""
            obj.insert(first)
    print("The word in the linked list--->")
    obj.traverse()

    """Taking input from user the element to be searched"""

    search1=input(("Enter the word you want to search in the list:"))
    if obj.search(search1):
        """ If search word is found then deleting this word from file
        as well as from linked list"""

        obj.delete_word(search1)
        """Deleting word from file by over writting ."""
        f=open("file1",'w')
        f.write("")
        f.close()
        length=obj.len()
        f=open('file1','a+')
        for i in range(0,length):
            f.write(" "+obj.index(i))
        f.close()
        print("The word you searched is deleted :")
    else:
        """The search element is not found then adding the element into Linkedlist 
        as well as into the file"""

        add_word=Node(search1)
        obj.insert(add_word)
        f=open('file1','a+')
        f.write(" "+search1)
        f.close()
        print("The word you search is added to the list:")
    print("After the searching the word your list is updated!!")
    obj.traverse()

main1()
