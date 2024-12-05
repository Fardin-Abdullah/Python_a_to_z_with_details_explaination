#code 1
n1 = 10
n2 = 20
res = n1 + n2
'''4 operations are done here 
1. in n1 keeping value
2. in n2 keeping value
3. summing up n1 + n2
4. keeping the sum in res
for any value of n1 and n2 the computer will do 4 operations one addition operation and 3 assignment operation.IN this case we 
can say the complexity is O(1). In this case instead of doing four operations if it does 10 operation the complexity
will be also O(1)
So we can say that for any input if the the number of operations remain constant then we will call the complexity O(1)'''
#code 2
n  = input()
n = int(input())
result = n * (n + 1) / 2
'''We will not take first two line in the last line 4 operations are done for this the complexity will be O(1)
because for any value of n the number of opeartions will be constant'''
#code 3
n = input()
n = int(input())
result = 0
for i in range (1,n+1):
    result = result + i
'''in line 3 one asssignment operation and then inside the loop there are 2 operations if n time the loop runs that 
means there will be n time assignment operation and n time addition operation
Here the numeber of operation is directly proportional to the input n so we can right this O(n)'''

'''Difference between O(1) and O(n)
suppose 1 addition and 1 assignment operation takes 1 microsec so which program has O(1) if the value of n is more than
1 lakh it will take 1microsec to run because the number of operations are constant here
On the other hand which has O(n) if the value of n is more than or equal 1 lakh it will take 1lakh microsec or 100milisec
because the numnber of operation is increasing linearly with the input'''

# So which one is better ?