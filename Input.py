# ---------------------
# ---- USER INPUT -----
# ---------------------

fname = input("Firstname : ")
lname = input("Lastname  : ")

fname = fname.strip().capitalize()
lname = lname.strip().capitalize()

print(f"Firstname : {fname} \nLastname : {lname} \nHappy To See You")

# -------------------------------------------
# --------- PRACTICAL SLICE EMAIL -----------
# -------------------------------------------

email = "yousef.aboueljihad@gmail.com"
print(email[:email.index("@")])


# ------------------------------------------
# --------- PRACTICAL AGE DETAILS ----------
# ------------------------------------------

# INPUT AGE 

Age = int(input("Enter Your Age : ").strip())

print(Age)
print(type(Age))

Months = Age * 12 
Weeks  = Months * 4 
Days   = Weeks * 7
Hours  = Days * 24 
Minuts = Hours * 60 
Second = Minuts * 60 

print(f"You Lived For : \nMonths : {Months:,} \nWeeks : {Weeks:,} \nDays : {Days:,} \nHours : {Hours:,} \nMinuts : {Minuts:,} \nSeconds : {Second:,}")

# Short If 

print("Kbir" if Age > 18 else "Sghir")


