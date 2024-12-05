"Two things are most important in case of data structure how to take from data from a data structure and how to add data to data structure"
#Understanding the concept of stack
"Suppose you have a box for keeping books you can keep 12 books here let's name the book as book1,book2.."
"book12 now and also it is not possible to take out any book from side because it is closed for this if we want"
"to take a book out so first i have to take out book1 first then book2 and at last book12 it is called stack"
"of books"

# now we will see stack of data and it's different types of operation
# first come last out let's make a class of stack now
class Stack:
    def __init__(self):
        self.items = []
    def push(self,item): # adding items to stack is called push keeping book in the box is called push
        self.items.append(item)
    def pop(self):
        return self.items.pop()
    def is_empty(self):
        if self.items == [] :
            return True
        return False
    def printInfo(self):
        while not s.is_empty():
            self.item = s.pop()
            print(self.item)
            
if __name__ == "__main__":
    s = Stack()
    s.push(1)
    s.push(2)
    s.push(3)

    s.printInfo()

# now question is what is the complexity for push and pop operation