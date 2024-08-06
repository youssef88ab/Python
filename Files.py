# ---------------------------------------
# ---------- FILES HANDLING -------------
# ---------------------------------------
# "a" Append  Open File For Appending Values , Create File If Not Exists 
# "r" Read    [Default Value] Open File For Read And Error If File Is Not Exists
# "w" Write   Open File For Writing , Create File If File Is Not Exists 
# "x" Create  Create File , Give Error If File Exists 
# # ------------------------------------------------------

import os 

print(os.getcwd())
print(os.path.abspath(__file__)) 
print(os.path.dirname(os.path.abspath(__file__)))



# --------------------------------------
# ----------- READ FILES ---------------
# --------------------------------------

# file = open("C:\youssef.txt","r")

# print(file)
# print(file.name)
# print(file.encoding)
# print(file.mode)

# print(file.read())
# print(file.read(4))

# print(file.realine())
# print(file.readlines())
# print(type(file.readlines()))

# for line in file :
#   
#    print(line)
#    
#    if (line.startswith("ab")) : 
#        break 
#    
# file.close()



# ----------------------------------------------------
# ------------- WRITE AND APPEND IN FILE -------------
# ----------------------------------------------------

#file = open("C:\youssef.txt.txt", "w") 
# file.write("Youssef" * 1000)

#MyList = ["Youssef\n" , "Ahmed\n" , "Mousa\n"]

#file.writelines(MyList)

# ------------------------------------------------
# file = open("C:\youssef.txt.txt", "a") 
# file.write("Youssef" * 1000)

# MyList = ["lsmfdks\n" , "hkylm med\n" , "Myldka\n"]

# file.writelines(MyList)

# ---------------------------------------
# ---------- IMPORTANT INFO -------------
# ---------------------------------------

# file = open("C:\youssef.txt.txt", "a") 

# file.truncate(5)
# print(file.tell())


file = open("C:\youssef.txt.txt", "r")

file.seek(5)
print(file.read()) 


import os 

os.remove("C:\youssef.txt.txt")
