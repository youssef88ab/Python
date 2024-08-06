# ------------------------------
# ----- FUNCTION LAMBDA --------
# ----- ANONYMOUS FUNCTION -----
# ------------------------------
# [1] It Has No Name 
# [2] You Can Call It Inline Without Defining It
# [3] You Can Use It In Return Date From Another Function
# [4] Lambda Used For Simple Functions And Def For Large Tasks 
# [5] Lambda is One Single Expression Not Block Of Code
# [6] Lambda Type Is Function 
# -----------------------------------------------------

def Say_Hello(Name) :
    return (f"Hello {Name}")

Hello = lambda Name : f"Hello {Name}"

print(Say_Hello("Youssef"))
print(Hello("Youssef"))

print(Say_Hello.__name__)
print(Hello.__name__)

print(type(Hello))
