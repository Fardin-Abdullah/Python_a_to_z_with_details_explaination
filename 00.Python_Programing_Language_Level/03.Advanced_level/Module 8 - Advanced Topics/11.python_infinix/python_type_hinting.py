"Python is dynamically typed programming language and C,C++,Java etc are statically typed programming language"
"dynamically means where we don;t need to say the type of variable and statically means where we have to say the "
"the type of variables"
# in python type hinting here we can say types of variables,parameters of function and also for return type hinting ,makes code easy to understand
# let's see example
def is_eligible(platform,age):
    if platform == "facebook" and age >= 13:
        return True
    if platform == "twitter" and age >= 18:
        return True
    return False

if __name__ == "__main__":
    platform = "facebook"
    age = 15
    print(is_eligible(platform,age)) 

# type hinting start
def is_eligible(platform:str,age:int):# we can write the function like it
    if platform == "facebook" and age >= 13:
        return True
    if platform == "twitter" and age >= 18:
        return True
    return False

#final code
def is_eligible(platform:str,age:int) -> bool: # we can write the function like it bool says it returns boolean value
    if platform == "facebook" and age >= 13:
        return True
    if platform == "twitter" and age >= 18:
        return True
    return False
if __name__ == "__main__":
    platform: str = "facebook"
    age: str = 15 # if i write here str = 5 it will also work to fix this see next code
    print(is_eligible(platform,age))
