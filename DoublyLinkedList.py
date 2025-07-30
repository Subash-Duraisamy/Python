class Node:
    def __init__(self,data):
        self.data=data;
        self.prev=None;
        self.next=None;


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail=None;
    def insert(self,data):
        newnode = Node(data)
        if self.head is None:
            self.head=self.tail=newnode;
        else:
            newnode.prev=self.tail;
            self.tail.next=newnode;
            self.tail=newnode;
    def fowardlist(self):
        current=self.head;
        fl=[];
        while current:
            fl.append(current.data);
            current=current.next;
        print(''.join(map(str,fl)));
        return fl;
    def backwardlist(self):
        current=self.tail;
        bl=[];
        while current:
            bl.append(current.data);
            current=current.prev;
        print(''.join(map(str,bl)));
        return bl;




# ____________________
# MAIN_FUNCTION
N=int(input("Enter number of inputs"));

integerlist=list(map(int,input().split()));
dll=DoublyLinkedList();

for value in integerlist:
    dll.insert(value);

forward=dll.fowardlist();
backward=dll.backwardlist();

if forward==backward:
    print("YES , Palindrome");
else:
    print("NOT, Palindrome");

