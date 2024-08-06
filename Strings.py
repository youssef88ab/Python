# STRING METHODS 
string = "  youssef-abou-el-jihad  "
lignes  = """
HELLO 
IAM 
YOUSSEF
""" 
number = "2"
stabes = "Hello\tIam\tYoussef"

print(number.zfill(3))            # 002
print(string.capitalize())        # Make First Char Upper
print(string.title())          
print(string.strip())
print(string.rstrip())
print(string.lstrip())
print(string.upper())             # Trasnform String To Upper
print(string.lower())             # Transform String To Lower
print(string.split("-" , 3))   
print(string.rsplit("-"))   
print(string.center(31))          # SPACES
print(string.center(31,"#"))      # HASHES 
print(string.rjust(31,"#"))       # HASHES RIGHT
print(string.ljust(31,"#"))       # HASHES LEFT
print(string.count("youssef"))    # Count How Many Time The Argument Repeated
print(string.count("you",2,7))    # Count How Many Time The Argument Repeated From Index to other
print(string.swapcase())          # Transform Lower To Upper And Upper To Lower
print(string.startswith("y"))     # False
print(string.startswith(" "))     # True
print(string.startswith(" ",3,9)) # Check if String starts with Caracter from Index Given
print(string.endswith("d"))       # Same As startswith but in the END 
print(string.index("y"))          # 2
print(string.index("y",1,6))      # 2
print(string.index("y",0,20))     # Error if not found
print(string.find("y"))           # 2 
print(string.find("y",15,20))     # -1 Because Not Found
print(lignes.splitlines())        # Return List Of Words For Each Line
print(stabes.expandtabs(2))       # Control Size Of Tabes
print(string.istitle())           # Check is string Is Title
print(string.isspace())
print(string.islower())
print(string.isupper())
print(string.isidentifier())     # Check if string can be name of variable 
print(string.isalpha())          # Check if string is alphabetical (not contain numbers)
print(string.isalnum())          # returns True if all the characters are alphanumeric, meaning alphabet letter (a-z) and numbers (0-9).
print(string.replace("youssef","Moustafa",1)) # Replace (Old Value , New Value , Count)
myList = ["Youssef" , "Mostafa" , "Rim"]
print("-".join(myList))