"If a function call it's self inside of his function then it is called recursion and the function is called recursive."
#example:
def my_fun():
    my_fun()

# what are the benefits of recurtion?
# one of the best example for understanding the recurtion is factorial problem 

def factorial(n):
    if n < 0:
        return None
    if n in [0,1]: # base condition
        return 1  
    return n * factorial(n-1)  # recursive funtion                  

# so to write a recursive function we need two things the base condition and the recursive function

print(factorial(4))
#let's explain what is happening here first n is 4 so 1.factorial(4) = 4*factorial(4-1).then n became 3 and calling 
# 2.factorial(3) = 3 * factorial(3-1) and then n became 2 so 3.factorial(2) = 2 * factorial(2-1) and now n become
# 1 so 4. factorial(1) = 1 the base condition the recursive function stops here
# now the 4th function call (value 1) will give the value to 3rd function (value 2) it will give to the 2nd function (value 6) and it will give 
# the value to the first function (value 24) we will get the factorial of 4