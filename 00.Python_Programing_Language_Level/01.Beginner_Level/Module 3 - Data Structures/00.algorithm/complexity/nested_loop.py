n = int(input()) # suppose n is 3 
count = 0
for i in range(n):
    for j in range(n):
        count += 1
print("n=",n,"count=",count)
''' 
if n is 3 that means inside the first loops the task will run 3 time and the task in 2nd loop the task will also
 run 3 time 
 the second loop has 1 addition operation 1 assignment operation
 for the first loop 
 for n = 0 the second loop will run 3 time  (3 times 2 operation = 6 operations) count = 3
 for n = 1 the second loop will run 3 times (3 times 2 operation = 6 operations) count = 6
 for n = 2 the second loop will run 3 times (3 times 2 operation = 6 operations) count = 9
 here we can see 3 times 2 operation for 3 times that means total 9 times the 2 operations run 9 is square of 3
 so if we input n the operations inside the second loop will run n*n times 
 So time complexity for this program is O(n**2)
 '''
n = int(input())
count = 0
for i in range(n):
    for j in range(n):
        for k in range(n):
            count += 1
print("n=",n,"count=",count)
'''
if n is 3 that means the first loop run 3 times second loop run 3 times third loop runs 3 times
for the first loop
if n = 0 in 2nd loop n = 0 in 3rd loop n = 0 one time tasks done (count = 1)
   n = 0 in 2nd loop n = 0 in 3rd loop n = 1 one time tasks done (count = 2)
   n = 0 in 2nd loop n = 0 in 3rd loop n = 2 one time tasks done (count = 3)

   n = 0 in 2nd loop n = 1 in 3rd loop n = 0 one time tasks done (count = 4)
   n = 0 in 2nd loop n = 1 in 3rd loop n = 1 one time tasks done (count = 5)
   n = 0 in 2nd loop n = 1 in 3rd loop n = 2 one time tasks done (count = 6)

   n = 0 in 2nd loop n = 2 in 3rd loop n = 0 one time tasks done (count = 7)
   n = 0 in 2nd loop n = 2 in 3rd loop n = 1 one time tasks done (count = 8)
   n = 0 in 2nd loop n = 2 in 3rd loop n = 2 one time tasks done (count = 9)

   n = 1 in 2nd loop n = 0 in 3rd loop n = 0 one time tasks done (count = 10)
   n = 1 in 2nd loop n = 0 in 3rd loop n = 1 one time tasks done (count = 11)
   n = 1 in 2nd loop n = 0 in 3rd loop n = 2 one time tasks done (count = 12)

   n = 1 in 2nd loop n = 1 in 3rd loop n = 0 one time tasks done (count = 13)
   n = 1 in 2nd loop n = 1 in 3rd loop n = 1 one time tasks done (count = 14)
   n = 1 in 2nd loop n = 1 in 3rd loop n = 2 one time tasks done (count = 15)

   n = 1 in 2nd loop n = 2 in 3rd loop n = 0 one time tasks done (count = 16)
   n = 1 in 2nd loop n = 2 in 3rd loop n = 1 one time tasks done (count = 17)
   n = 1 in 2nd loop n = 2 in 3rd loop n = 2 one time tasks done (count = 18)

   n = 2 in 2nd loop n = 0 in 3rd loop n = 0 one time tasks done (count = 19)
   n = 2 in 2nd loop n = 0 in 3rd loop n = 1 one time tasks done (count = 20)
   n = 2 in 2nd loop n = 0 in 3rd loop n = 2 one time tasks done (count = 21)

   
   n = 2 in 2nd loop n = 1 in 3rd loop n = 0 one time tasks done (count = 22)
   n = 2 in 2nd loop n = 1 in 3rd loop n = 1 one time tasks done (count = 23)
   n = 2 in 2nd loop n = 1 in 3rd loop n = 2 one time tasks done (count = 24)

   
   n = 2 in 2nd loop n = 2 in 3rd loop n = 0 one time tasks done (count = 25)
   n = 2 in 2nd loop n = 2 in 3rd loop n = 1 one time tasks done (count = 26)
   n = 2 in 2nd loop n = 2 in 3rd loop n = 2 one time tasks done (count = 27) 

   so here if we input n the operation or the tasks in the 3rd loop will run n * n * n time
   So the complexity is O(n**3)
   '''