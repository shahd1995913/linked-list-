#  1-- Rotate List

# Find the length in linked list 
import random
class Node:
     # Constructor to initialize the node object
    def __init__(self,val=0,next=None):
            self.val=val
            self.next=next

class LinkedList:
     # Function to initialize head
    def __init__(self):
        self.head=None



        # return ( self.range[pick])

 # Function to insert a new node at the beginning
    def push_element_to_linkedlist(self,new_data):
        element=Node(new_data)
        element.next=self.head
        self.head=element

    def size_of_linkedlist(self):
        count=0
        temp=self.head

        while(temp):
            count=count+1
            temp=temp.next
        return count

    # function print the linkedlist 

    def print_linkedlist(self):
        temp=self.head
        while(temp):
            print(temp.val)
            temp=temp.next

   # Function that routat the linked list 
    def routat_linkedlist(self,k):
        if (k==0):
           return 

        current =self.head

        count=1


        while(count<k and current is not None):

            current=current.next

            count=count+1

        if current is  None:
            return 

        kth=current

        while(current.next is not None):

            current=current.next

        current.next=self.head

        self.head=kth.next

        kth.next=None

    def Delete_Duplicates_sorted_linkedlist(self):
        head=self.head
        copy=Node(0,head)
        copy2=copy
        while(head):
            if(head.next and head.val==head.next.val):
                while(head.next and head.val==head.next.val):
                    head=head.next
                    copy2.next=head.next
            else:
                copy2= copy2.next

            head = head.next

        return copy.next


                   
                

 



 

if __name__=="__main__":
    l=LinkedList()
    l.push_element_to_linkedlist(5)
    l.push_element_to_linkedlist(5)
    l.push_element_to_linkedlist(3)
    l.push_element_to_linkedlist(1)
    l.push_element_to_linkedlist(2)


# for i in range(100,0,-20):
#     l.push_element_to_linkedlist(i)
print("size of node in linked list:",l.size_of_linkedlist())

l.print_linkedlist()
# print("------------")
# l.routat_linkedlist(2)
# print("Ater Routat")
# print("------------")

print("------------")
print("Ater Delete  Duplicates From sorted linked list")
print("------------")
l.Delete_Duplicates_sorted_linkedlist()
l.print_linkedlist()

