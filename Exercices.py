a , b = 0 , 32
Sum = 0 
ptr = a 
while ( ptr < b) : 
    if ((ptr%3) == 0 and (ptr%5) == 0) : Sum = Sum + ptr
    ptr = ptr + 1
print(Sum)

# ------------------------------------------------------------- 

Nom = input("ENTRER VOTRE NOM : ")
Sexe = input("ENTRE VOTRE SEXE : ")
if (Sexe == "M") : print("CHEZ MONSIEUR {} " .format(Nom))
else : print("Chez Modmoiselle {}" .format(Nom))

# ------------------------------------------------------------

Mylist = ['Jean-Michel', 'Marc', 'Vanessa', 'Anne', 'Maximilien',
          'Alexandre-Benoît', 'Louise']

i = 0
while(i < len(Mylist)) : 
    print(Mylist[i] , " : " , len(Mylist[i]))
    i = i + 1

# -----------------------------------------------------------