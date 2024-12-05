#Undesrtanding the concept of queue
"Suppose there is a counter in for taking an appointment with doctor those who will come first or in line who is in"
"first he will get apppointment first and the last one will get last if one person comes in line it is called"
"enqueue and if one person left it is called dequeue"

# now we will see queue of data and different types of operation of data
# first come first out let's make a queue right now
class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            return "Queue is empty"

    def is_empty(self):
        return len(self.items) == 0

    def print_info(self):
        while not self.is_empty():
            person = self.dequeue()
            print(person)

    def peek(self):
        if not self.is_empty():
            for item in self.items:
                print(item)
        else:
            print("Queue is empty")

if __name__ == "__main__":
    q = Queue()
    q.enqueue("rafi")
    q.enqueue("ilmaa")
    q.enqueue("arabi")
    print("Queue contents:")
    q.peek()
    print("\nDequeue and print:")
    q.print_info()
