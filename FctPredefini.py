from math import * 

Angle = pi/6 
Num   = 4 
print("Le Carre De {} = {} " .format(Num,sqrt(Num)))
print("Le Sinus De {} = {} " .format(Angle,sin(Angle)))

Mile = input("Mile : ")
Hour = input("Hour : ")
print("m/s : {}/{}".format((int(Mile)*1609),int(Hour*3600)))
print("km/h : {}/{}".format((int(Mile)*1609/1000),int(Hour)))

a = input("A : ")
b = input("B : ")
c = input("C : ")
d = input("D : ")
Air = sqrt(d*(d*a)*(d-b)*(d-c))

l = input("l : ")
g = input("g : ")
T = 2*pi*sqrt(l/g)



