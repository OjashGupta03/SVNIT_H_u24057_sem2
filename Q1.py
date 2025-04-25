class node:
    def __init__(self,data):
        self.data=data
        self.next=None
    def insertAtEnd(self,data):
        print("data inserted")
        newnode=node(data)
        a=self
        while((a.next)!=None):
            a=a.next
        a.next=newnode
    def insertAtBegin(self,data):
        newnode=node(data)
        newnode.next=self
        return newnode
    def display(self):
        a=self
        while(a!=None):
            print(a.data)
            a=a.next
head=node(10)
head.insertAtEnd(20)
head=head.insertAtBegin(5)
head.display()
