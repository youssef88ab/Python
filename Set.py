# ------------------------------------
# ------------- SET ------------------
# ------------------------------------

# NOT ORDRED AND NOT INDEXED 
# SET ITEMS ARE UNIQUE

MySet = {"Youssef" , "Youssef"  , "Mostafa" , "Rim"}
print(MySet)

# CLEAR()

MySet.clear() 
print(MySet)

# UNION()

Set = {"Rim" , "Omar" , "Hamza"}
print(MySet.union(Set))

# ADD()

MySet = {"Youssef" , "Youssef"  , "Mostafa" , "Rim"}
MySet.add("Hamza")
print(MySet)

# COPY()

Set = MySet.copy()
print(Set)

# REMOVE()

MySet.remove("Youssef")
print(MySet)

# DISCARD()

MySet.discard("Youssef")

# THE DIFFERENCE BETWEEN DISCARD AND REMOVE
# THAT REMOVE HOW ERROR WHEN SHE DONT FIND THE ELMENT
# BUT DISCARD DONT SHOW ERROR WHEN YOU REMOVE 
# ELEMENT IN THE SET THAT DIDNT EXIST 

# POP()

MySet.pop()
print(MySet)

# UPDATE()

Setone  = {"Omar" , "Najm" , "Wahib" , "Rim" , "Mostafa"}
MySet.update(Setone)
print(MySet)

# DIFFIRENCE()

print(MySet.difference(Setone))

# DIFFIRENCE_UPDATE()

x = {1 , 2 , 3 , 4 ,5}
y = {1 , 2 , 3}
x.difference_update(y)
print(x)

# INTERSECTION()

x = {1 , 2 , 3 , 4 ,5}
y = {1 , 2 , 3 , 6}
print(x.intersection(y))

# INTERSECTION_UPDATE()

x = {1 , 2 , 3 , 4 , 5}
y = {1 , 2 , 3 , 6}
x.intersection_update(y)
print(x)

# SYMETRIC_DIFFERENCE()

x = {1 , 2 , 3 , 4 , 5 , 6 , 7 }
y = {1 , 2 , 4 , 8}
print(x.symmetric_difference(y))

# SYMETRCI_DIFFERENCE_UPDATE()

x = {1 , 2 , 3 , 4 , 5 , 6 , 7 }
y = {1 , 2 , 4 , 8}
x.symmetric_difference_update(y)
print(x)


# ISSUPERSET()

a = {1 , 2 , 3 , 4 , 5 }
b = {1 , 2 , 3}
c = {1 , 8 , 3}

print(a.issuperset(b)) #True
print(a.issuperset(c)) #False


# ISSUBSET() L3AKS DLFOQANYA 

a = {1 , 2 , 3 , 4 , 5}
b = {1 , 2 , 3}

print(a.issubset(b))   #FALSE
print(b.issubset(a))   #TRUE


