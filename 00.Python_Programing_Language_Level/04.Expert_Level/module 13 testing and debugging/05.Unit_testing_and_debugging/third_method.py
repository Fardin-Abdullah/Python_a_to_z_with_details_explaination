#unit testing
"One of the most important things in software engineering is unit testing where every function or module "
"is considered as a module and we test it"
"For this in every modern programming language there is package for unit testing"
"in python there is package unittest and also pytest, pytest it is very popular third party package unit testing because it is easy to use"
"We can use concept of unit testing while implementing different types of algorithm"

def average(L):
    if not L:
        return None
    return sum(L)/len(L)

def test_average():
    assert 3.0 == average([1,2,3,4,5])

# we have to test every function by using pytest
# we have to test program by making a table this system is called table driven test
def test_average():
    test_cases = [
        {"name":"simple case 1",
        "input":[1,2,3],
        "expected":2.0},
        {"name": "simple case 2",
        "input": [1,2,3,4],
        "expected": 2.0},
        {"name":"list with one item",
        "input": [],
        "expected":100.0},
        {"name": "empty list",
        "input": [],
        "expected": None}

    ]
    for test_case in test_cases:
        assert test_case["expected"] == 
average(test_case["input"]),test_case["name"]
# in this program in list every dictionary is test case