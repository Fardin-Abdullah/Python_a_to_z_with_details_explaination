name : str = "rafi"
year : int = 2006
gpa : float = 3.99
flag : bool = True

fruits : list = ["Mango","Guava","Apple"]
print(fruits)
fruits : list[str] = ["Mango","Guava","Apple"]
print(fruits)

coordinate : tuple = (23.67,90.34)
print(coordinate)
coordinate : tuple[float,float] = (23.67,90.34)
print(coordinate)

colors : set = {"green","blue","red","orange"}
print(colors)
colors : set[str] = {"green","blue","red","orange"}
print(colors)

capitals : dict = {"Bangladesh","Dhaka","England","London"}
print(capitals)
capitals : dict [str,str]= {"Bangladesh","Dhaka","England","London"}
print(capitals)

# use type hinting when your code will be used by many programmers or where we will use unit testing we will use type hinting some many says
