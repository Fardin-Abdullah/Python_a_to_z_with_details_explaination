#code 1
n = int(input())

if n % 2 == 0 :
    print(n, "is even number")

else:

    print(n, "is odd number")

'''Time complexity for this code is O(1) 
Space complexity is O(1) for any value of n one variable iss use when we use any variable it uses the memory of computer
 so how much memory is ussed it depends on how many vfariables we have used not only variable but also for any data structures
 how much data we stored depending on that we can know how much memory is used'''

n = 100
even = [False] * (n+1)
for i in range(0,n+1,2):
    even[i] = True
print(even)
'''Time complexity is O(n)
Space Complexity if n is 100 the items in list are 101 if n is 1000 items will be 1001 so we can say that the item number in list
is proprtional the input n space complexity is O(n)
if there was not for loop the time complexity will be also O(n) because in even the list is created with n+1 size element
and every index has False'''

''' now there is a question for running n = int(input()) computer needs time why we dodnt count it?
Ans: it is not part of the algorithm on the other hand time complexity for this is O(1)now if the other part of programs
complexity is O(1) total complexity = O(1) + O(1) = 2*O(1) =O(1) if there is one statement complexity is O(1) and also 
for 5 statement complexity O(1) mainly O(1) does not mean one operation it means constant number of operation
if the other parts complexity is O(n) then O(n) + O(1) = O(n)  
here O(1)  is much more lesser than O(n)
similarly if there is O(n**4) + O(n**3) + O(n**2) + O(n**1) + O(1) = O(n**4+n**3+n**2+n**1+1) = O(n**4)
because the other value is much lower than n**4 we can avoid it
'''

'''n = 100 then O(n**4) = 100000000 and  O(n**4) + O(n**3) + O(n**2) + O(n**1) + O(1) = 101010101
 n = 10000 then O(n**4) = 10000000000000000 and  O(n**4) + O(n**3) + O(n**2) + O(n**1) + O(1) = 10001000100010001'''