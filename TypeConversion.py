# ---------------------------------------------
# ------------ TYPE CONVERSION ----------------
# ---------------------------------------------

MyString = "Youssef" # String 
MyList   = [ 1 , 2 , 3 , 4 , 5 ] # List
MyDict   = {"One" : 1 , "Two" : 2 , "Three" : 3} #Dictionary
MySet    = ("A" , "B" , "C") # Set
MyTuple  = { "X" , "Y" , "Z"} # Tuple

print(tuple(MyString))
print(tuple(MyList))
print(tuple(MyDict))
print(tuple(MySet))

print("*" * 40)

print(list(MyString))
print(list(MyDict))
print(list(MyTuple))
print(list(MySet))

print("*" * 40)

print(set(MyString))
print(set(MyList))
print(set(MyDict))
print(set(MyTuple))

print("*" * 40)
