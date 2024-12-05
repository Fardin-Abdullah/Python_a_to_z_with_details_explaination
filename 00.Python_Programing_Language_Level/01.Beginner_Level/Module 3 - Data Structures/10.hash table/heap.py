#your heap 19,7,17,3,5,12,10,1,2
# suppose we are keeping the tree in a list
heap = [None] * 10
# now will keep root of heap in heap[1] suppose 19 is root
heap[1] = 19
#root node has two child 7 and 17 we will keep it in 1*2 = 2 and 1*2 + 1=3
heap[1*2] = 7
heap[1*2+1] = 17
print(heap)
# now node 7 is in no 2 index [note we are indexing here not from 0 from 1 for better understanding] for this
# left child of this will stay at 2*2 = 4 at no 4 indexand right child will stay 2*2 + 1 = 5 no index for this
# node 17 in  3rd index so it's left child will stay at 3*2 = 6 index and right child will stay at 3*2+1 = 7
# index
heap[2*2]=3
heap[2*2+1]=5
heap[3*2]=12
heap[3*2+1]=10
print(heap)
# node 3 in 4 index so the child will be at 8,9 index
heap[4*2]=1
heap[4*2+1]=2
print(heap)

def left(i):
    return 2 * i
def right(i):
    return 2 * i + 1
def parent(i):
    return i // 2

# function to check if a list is max heap or not
def is_max_heap(H):
    n = len(H) - 1
    for i in range(n,1,-1):
        p = parent(i)
        if H[p] < H[i]:
            return False
    return True

if __name__=="__main__":
    H = [None,19,7,17,3,12,10,1,2]
    print(H,is_max_heap(H))
    H = [None,19,7,17,3,5,12,10,1,4]
    print(H,is_max_heap(H))