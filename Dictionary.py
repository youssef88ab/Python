# -----------------------------------------
# ----------------- DICT ------------------
# -----------------------------------------

User = {
    "Name" : "Youssef" , 
    "Age"  :  19 ,
    "Country" : "Morocco" , 
    "Skills" : ["C" , "C++" , "Python" , "Java" , "J2EE"] 
}

# KEYS() + VALUES()

print(User)
print(User["Age"])
print(User.get('Country'))
print(User.keys())
print(User.values())


# TWO - DIMENSIONAL DICTIONARY

CV = {
    "Languages" : {
        "ARABIC" : 100 ,
        "FRENCH" : 40  , 
        "ENGLISH": 50  
    } , 
    "Skills" : {
        "Web-Dev" : ["Html" , "Css" , "Js" ] , 
        "Databases" : ["SQL SERVER" , "ORACLE"] 
    }
}

print(CV)
print(CV["Skills"])
print(CV["Skills"]["Web-Dev"])


# CREATE DICTIONARY FROM VARIABLES 
Dict1 = {
    "Name" : "Html" , 
    "Progres" : 30
} 

Dict2 = {
    "Name" : "css" , 
    "Progres" : 40 
}

Dict3 = {
    "Name" : "JS" , 
    "Progres" : 0
}

Dictionary  = {"One" : Dict1 , "Two" : Dict2 , "Three" : Dict3}
print(Dictionary)


# CLEAR()

Dictionary.clear()
print(Dictionary)

# UPDATE()

Member = { "Name" : "Youssef"}
Member["Age"] = 19
print(Member)
Member.update({"Country" : "Morocco"})
print(Member)

# COPY

Dictionary = Member.copy()
print(Dictionary)

# SET DEFAULT (TY9LEB 3LA CHI KEY LA MAL9ATOUCH KYTB3 VALEUR LI 3TITIH )

print(Dictionary.setdefault("skill" , 88))

# POPITEM()

print(Member)
print(Member.popitem())
print(Member)

# ITEMS

Dictionary = Member.items()
print(Dictionary)
Member["Skill"] = "Xbox"
print(Dictionary)

# FROMKEYS()

a = ('One', 'Two' , 'Three')
b = "X"
print(dict.fromkeys(a,b)) # ONE , X , TWO , X , THREE , X