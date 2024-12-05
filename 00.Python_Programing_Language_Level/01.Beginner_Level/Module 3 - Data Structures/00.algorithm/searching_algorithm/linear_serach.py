'''If there are 5 books in a bookshelf I have to find a certain book among them I will find it easily what if there
are thousands of books in bookshelf and I have to find certain a book
solution: if we start finding the book elomelo vabe there is not chance to find the book
algorithm :if we start finding the book from the first shell of books till the last if there is the book we will find
best case: if the book is in first shelf and the first book of this shelf
worst case : if the book is at the last shelf and the last book of this shelf  '''
#consider the shelf as a list or array and the items as books
#code:
def linear_search(L,x):  # one algorithm can be written in different ways if it is possible to understand after which 
                        # work we have to do which one that means it is a correct algorithm
                        #we can implement algorithm in any programming language
    n = len(L)
    for i in range(n):
        if L[i] == x:
            return i
    return None
#code1:
def linear_search(L,x):
    n = len(n)
    i = 0

    while i < n:
        if L[i] == x:
            return i
        i += 1
    i = -1
    return i

'''
Space complexity O(1) because main algo uses some variables whatever the value of n for every case the same variables 
will be used
Time Complexity O(n)
because for n amounts of element we have to check n times
best case O(1) first element is our desired element
worst case O(n) last element is our desired element
average case O(n/2),O(n*1/2),O(n)*O(1/2),O(n)'''

#For different types of algorithm generally the complexity means the worst case 