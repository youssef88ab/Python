# ---------------------------------
# LISTS 
# ---------------------------------

MyList = ["One" , "Two" , True , 89.7 , 1 ]

print(MyList)
print(MyList[1])
print(MyList[-1])
print(MyList[:4])
print(MyList[1:])
print(MyList[1:4])
print(MyList[::2])

# --------------------------------
# -------- LISTS METHODS --------- 
# --------------------------------

# APPEND()

BlackList = [ "Youssef" , "Mohamed" , "Omar" ]

MyList.append(False)
MyList.append(BlackList)
print(MyList)
print(MyList[6][2])

# EXTEND()

a = [1 , 2 , 3 , 4]
b = ["A" , "B" , "C" , "D"]

a.extend(b)
print(a)

# REMOVE()

a.remove(4)
print(a)

# SORT()

y = [1 ,3 , 58 , 2 , 18 , 45 , 34 , 77 , 90 ]
y.sort()
print(y)

y.sort(reverse=True)
print(y)

# REVERSE()

z = [1 , 4 , 8 , "You" , 98 , 45]
z.reverse()
print(z)

# CLEAR()

a = [1 ,2 ,3 ,4]
a.clear()
print(a)

# COPY()

b = z.copy()
z.append(2)
print(z)
print(b)

# COUNT()

print(b.count(8))

# INDEX()

print(b.index(8))

# INSERT()

f = [1 ,2 ,3 ,5 ,6 ,7]
f.insert(3 , 4)
print(f)

# POP()

f.pop()
print(f)
