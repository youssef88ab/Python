# ----------------------------------
# ------------ TUPLES --------------
#-----------------------------------

MyTuple = (0,1,2,3,4,5)

# Tuple Indexing

print(MyTuple[1])

# Tuple Concatenation

Tuple = (6,7,8,9,10)
Sum   = MyTuple + Tuple
print(Sum)

# Tuple , List , String Repetead()

MyString = "Youssef"
MyList   = [1,2,3,4,5]

print(MyString * 3)
print(MyList * 3)
print(MyTuple * 3)

# Count()

print(MyTuple.count(1))

# Index()

print(MyTuple.index(1))

# Tuple Deustruct 

TUPLE = (1 , 2 , 3)
x, y, z = TUPLE

print(x)
print(y)
print(z)