class Element:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def put(self, data):
        element = Element(data)
        if(self.head==None):
            self.head=element
            self.tail=element
        else:
            self.tail.next = element
            self.tail = element

    def pop(self):
        if(self.head != None):
            data = self.head.data
            self.head = self.head.next
        else:
            data = None
        return data

    def peek(self):
        if(self.head != None):
            data = self.head.data
        else:
            data = None
        return data

test_queue = Queue()
number_of_commands = 0

while(1):
    try:
        number_of_commands = eval(input()) # try except!
        break
    except:
        print("enter a number")
        number_of_commands = -1


while(number_of_commands > 0):
    data = None
    command = input()
    command_decoded = command.split(' ')
    if(len(command_decoded) > 1):
        data=command_decoded[1]
    if(command_decoded[0].strip()=='1'):
        if(data != None):
            test_queue.put(data)
        else:
            raise Exception('missing data for queue element!')
    elif(command_decoded[0].strip()=='2'):
        test_queue.pop()
    elif(command_decoded[0].strip()=='3'):
        print(test_queue.peek())
    else:
        raise Exception('invalid command (Valid commands are 1,2,3...)')
    number_of_commands = number_of_commands - 1