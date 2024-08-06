def function_Name(string , Num) :
    print (f"{string} , {Num}")

function_Name("Youssef" , 19)

MyDict = {"One" : 1 , "Two" : 2 , "Three" : 3 , "Four" : 4 , "Five" : 5}

def Dict(MyDict):
    for element in MyDict :
        print(element)
    
Dict(MyDict)

def Show_Skills(*Skills) : 
    for Skill in Skills  : 
        print(Skill)
    
Show_Skills("Html" , "Css" , "Js" , "Python")

x = 1 

def Function():

    global x
    x = 20 

    print(f"{x}")

Function()

print(x)









