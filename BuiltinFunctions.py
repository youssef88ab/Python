# ------------------------------------------
# ---------- BUILT IN FUNCTIONS ------------
# ------------------------------------------
# all()
# any()
# bin()
# id() 
# Sum()
# round()
# range() 
# print()
# abs()
# pow()
# min()
# max()
# slice(start,end,step)

# --------------------------------------------------

MyList = [1 ,2 ,3 ,4 ,5 ]

if all(MyList) :
    
    print("All Elements Are True")
    
else :
    
    print("There Is At Least One Element False ")
    

# ---------------------------------------------------

if any(MyList) : 
    
    print("There is At Least One Element True")
    
else : 
    
    print("All Elements Are False")

# ---------------------------------------------------

print(bin(239012))

# --------------------------------------------------

print(id(MyList))

# --------------------------------------------------

print(sum(MyList))
print(sum(MyList , 15))

# -------------------------------------------------

print(round(1.34))
print(round(4.56))
print(round(8.457 , 2))
print(round(8.453 , 2))

# -------------------------------------------------

print(list(range(1, 20 , 2)))
print(list(range(10)))

# -------------------------------------------------

print("Hello Youssef How Are You")
print("Hello" , "Youssef" , "How" , "Are" , "You" , sep=" @ " )

print("First Line" , end=" @ ")
print("Second Line" , end="\n")
print("Third Line")

# ------------------------------------------------

print(abs(-1))

# ------------------------------------------------

print(pow(2,2))

# ------------------------------------------------

NumList = [ 2 , 3  , 1  , 0 , 4 , 5 ]
print(min(NumList))
print(max(NumList))

# ------------------------------------------------

MyList = ["One" , "Two" , "Three" , 1 , 2 , 3]

print(MyList[slice(2,5)])
print(MyList[slice(3)])

