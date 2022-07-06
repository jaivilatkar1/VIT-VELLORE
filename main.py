#Program to find middle of linked list
#Create node
class node:
    def __init__(self,data):
        self.data=data
        self.next=None
#Creating,printing and finding middle element of Linkedlist. 
class Linkedlist:
    def __init__(self):
        self.head=None
    def push(self,data):
        new_node=node(data)
        new_node.next=self.head
        self.head=new_node
    def printlinkedlist(self):
        temp=self.head
        count=0
        while temp:
            print(temp.data,"->",end="")
            count+=1
            temp=temp.next
        print("Null")
        mnode=self.head
        for i in range(count//2):
            mnode=mnode.next
        print("Middle element is: ",mnode.data)
#Driver Code
llist=Linkedlist()
x=int(input("Enter number of values to be inserted:"))
for i in range(x,0,-1):
    llist.push(i)
    llist.printlinkedlist()