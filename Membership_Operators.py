# ------------------------------
# ---- MEMBERSHIP OPERATORS ----
# ------------------------------
# in
# not in

# String 

string = "Mohamed"
print("M" in string)
print("s" in string)

# List 
MyList = [1 , 2 , 3]
print(0 in MyList)
print(1 in MyList)


Africa = ["Morocco" , "Egypt" , "Algeria" ]

Country = "Spain"
if   (Country in Africa)     : print("AFRICA")
elif (Country not in Africa) : print("OTHERS")

tries = 4 

mainpassword = "youssef3334AB"

inputpassword = input("PASSWORD :")

while inputpassword != mainpassword :

    tries -= 1

    print(f"Wrong Password , {'Last' if tries == 0 else tries } Chances Left ")

    inputpassword = input("PASSWORD :")

    if tries == 0 : break 

else : print("Correct Password")


