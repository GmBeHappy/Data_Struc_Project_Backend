class LinkedList:
    class Node :
        def __init__(self,data,next = None) :
            self.data = data
            if next is None :
                self.next = None
            else :
                self.next = next
                
        def __str__(self) :
            return str(self.data)

    def __init__(self,head = None):
        if head == None:
                self.head = self.tail = None
                self.size = 0
        else:
            self.head = head
            t = self.head        
            self.size = 1
            while t.next != None :
                t = t.next 
                self.size += 1
            self.tail = t
            
    def __str__(self) :
        s = 'Linked data : '
        p = self.head
        while p != None :
            s += str(p.data)+' '
            p = p.next
        return s

    def __len__(self) :
        return self.size
    
    def append(self, data):
        p = self.Node(data)
        if self.head == None:
            self.head = self.tail = p
        else:
            t = self.tail
            t.next = p   
            self.tail =p  
        self.size += 1

    def removeHead(self) :
        if self.head == None : return
        if self.head.next == None :
            p = self.head
            self.head = None
        else :
            p = self.head
            self.head = self.head.next
        self.size -= 1
        return p.data
    
    def isEmpty(self) :
        return self.size == 0
    
    def nodeAt(self,i) :
        p = self.head
        for j in range(i) :
            p = p.next
        return p

class Queue:
    def __init__(self, list = None):
        self.items = LinkedList()
        if list == None:
            pass
        else:
            for i in list:
                self.enQueue(i)

    def __str__(self):
        if not self.isEmpty():
            out = 'Queue data : '
            for i in range(len(self.items)):
                val = self.items.nodeAt(i).data
                out += str(val) + ' '
            return out
        return 'Empty Queue'

    def __len__(self):
        return len(self.items)

    def enQueue(self, value):
        self.items.append(value)

    def deQueue(self):
        return self.items.removeHead()

    def isEmpty(self):
        return len(self.items) == 0

i = 0
stock = []
item = []
q = []
    

while True:
    
    print('1 | add new item')
    print('2 | In stock')
    inp = int(input('Enter choice : '))

    if inp == 1:
        nameItem = input('Enter name item : ')
        num = int(input('Enter amount of item : '))
        item.append(nameItem)
        queue = Queue()
    
        for j in range(num):
            queue.enQueue(j)
        q.append(queue)    
    elif inp == 2:
        if len(item) == 0:
            print('stock is empty.')
        else:
            print('>'*10)
            for j in range(len(item)):
                print(f'{item[j]} = {q[j]}')
            print('>'*10)

            print('1 > add amount of item')
            print('2 > dequeue item')
            print('3 > delete item')
            print('4 > clear item')
            print('5 > exit')
            inp = int(input('Enter choice: '))
            if inp == 1:
                name = input('Enter name item for add amount : ')
                num = int(input('Enter amount : '))
                index = item.index(name)
                for j in range(num):
                    q[index].enQueue(j)
                
                print('>'*10)
                for j in range(len(item)):
                    print(f'{item[j]} = {len(q[j])}')
                print('>'*10)
                
            elif inp == 2:
                name = input('Enter name item for dequeue amount : ')
                num = int(input('Enter amount : '))
                index = item.index(name)
                for j in range(num):
                    q[index].deQueue()

                print('>'*10)
                for j in range(len(item)):
                    print(f'{item[j]} = {q[j]}')
                print('>'*10)
                

            elif inp == 3:
                name = input('Enter name item for delete : ')
                index = item.index(name)
                q.pop(index)
                item.pop(index)

                print('>'*10)
                for j in range(len(item)):
                    print(f'{item[j]} = {len(q[j])}')
                print('>'*10)

            elif inp == 4:
                name = input('Enter name item for clear : ')
                index = item.index(name)
                while len(q[index]) != 0:
                    q[index].deQueue()
                print('>'*10)
                for j in range(len(item)):
                    print(f'{item[j]} = {len(q[j])}')
                print('>'*10)


            elif inp == 5:
                pass

    print('-'*50)

    i += 1
