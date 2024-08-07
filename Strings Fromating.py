# String Formating

#-------------------------------------------------
# ----------------- OLD WAY ----------------------

Name = "Youssef"
Age = 19
print("Name : %s , Age : %d" % (Name , Age ))

string = "Hello People Iam Learn Python"
print("%.5s" % string)

#-------------------------------------------------
#-------------------------------------------------

#-------------------------------------------------
#----------------- NEW WAY -----------------------

print("Name : {:s} , Age : {:d} " .format(Name , Age))

print("{:.5s}" .format(string))

# Format Money

Money = 309589009
print("{:,d}" .format(Money))

# Rearange Items 

a , b , c = "One" , "Two" , "Three"
print("{} {} {}" .format(a,b,c))     # One Two Three
print("{1} {2} {0}" .format(a,b,c))  # Two Three One
print("{1:.3s} {2:.3s} {0:.3s}" .format(a,b,c))  # Two Three One


