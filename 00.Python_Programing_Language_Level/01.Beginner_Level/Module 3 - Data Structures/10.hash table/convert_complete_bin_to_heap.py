# first we have to check if it follows the the rules of heap
# suppose a tree

def max_heapify(heap,heap_size,i):
    l = left(i)
    r = right(i)

    if l <= heap_size and heap[l] > heap[i]:
        largest = l
    else:
        largest = i
    
    if r <= heap_size and heap[r] > heap [largset]:
        largest = r
    
    if largest != i :
        heap[i],heap[largest] = heap[largest],heap[i]
        max_heapify(heap,heap_size,largest)