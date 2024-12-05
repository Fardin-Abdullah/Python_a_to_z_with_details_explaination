"When we will implement any data structure or algorithm with python we have to test it will it work for different inputs"
"for this we use some methods"
#first method
#function to find the average of list numbers
def average(L):
    if not L:
        return None
    return sum(L)/len(L)
# now we are testing the function will it work or not
def average(L):
    if not L:
        return None
    return sum(L)/len(L)
if __name__ == "__main__":
    L = [1,2,3,4,5]
    print(average(L))
# here we know the average of that list number is 3 so we can say by watching this program works we can test like this
# but this work can be done more efficiently let's see
if __name__== "__main__":
    L = [1,2,3,4,5]
    expected_rsult = 3.0
    result = average(L)
    if expected_rsult == result:
        print("test passed")
    else:
        print("test failed!","received:",result,"expected",expected_rsult)

# go to second method file
# using assert to test the program
if __name__ == "__main__":
    L = [1,2,3,4,5]
    expected_rsult = 3.0
    assert expected_rsult == average(L),"average() produced incorrect result "
