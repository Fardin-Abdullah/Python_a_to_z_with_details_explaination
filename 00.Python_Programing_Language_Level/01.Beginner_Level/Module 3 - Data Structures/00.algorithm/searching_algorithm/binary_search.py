'''suppose we have given a list of numbers and we have to find m and also said that it is sorted from lower to higher
now we will take the number which is in middle if there is two we will take the first one

Then we will compare it with m if it is equal to m done or m is larger thean the middle we are sure that we wont find
the number in first half 

If m is lesser than the middle number we wont find the number in rthe second half

Now in which part there is m we will take that part and we will repeat the process what we have done earlier

Ater doing this process repeatedly one time there will not remain any item then we can say the item does not exist'''
def binary_search(L,x):
    n = len(L)
    left,right = 0 , n-1
    while left<=right:
        mid =  (left + right) //  2
        if L[mid] == x:
            return mid
        elif L[mid] < x:
            left = mid + 1
        else:
            right = mid - 1
    return -1
'''
Space complexity O(1) here we are using just some constant amount of variables n,left,right,mid

Time complexity O(logn)
if b**y = x then logbx= y
log2 16 = 4 cause 2**4 = 16
if we multiply 1 with 2 5 times we get (1*2*2*2*2*2)=32 or 2**5=32 , log2 32 = 5
 that means if we keep dividing 32 with 2 5 times we will get 1
1.32/2=16,2.16/2=8,3.8/2=4,4.4/2=2,5.2/2=1
thus we are dividing into half the list in binary search we will able to do it maximum log2 n times
for this complexity of binary search O(logn)'''