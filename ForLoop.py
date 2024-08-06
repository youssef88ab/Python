# ---------------------
# ----- FOR LOOP ------
# ---------------------

MyList = [1 ,2 ,3 ,4 ,5]

for Number in MyList : 
    if Number % 2 == 0 : print("Even")
    else : print("Odd")

# --------------------------------------

MyString = "Youssef"

for Letter in MyString :
    print(Letter)

print("Loop Finish")

# ---------------------------------------

MyRange = range(1,100)

for Number in MyRange :
    print(Number)

# ---------------------------------------

MyDict = {"One" : 1 , "Two" : 2 , "Three" : 3 , "Four" : 4 , "Five" : 5}

for Number in MyDict : 
    print(f"String {Number} , Number : {MyDict[Number]}")

