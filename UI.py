from PC import *
#from os import *
RAM = {}
ROM = {}
EXP = {}
licznik = 0
#f = ""
a = int(input("RAM size(bytes)"))
for i in range(a):
    RAM[i] = "00000000"

    
b = input("TeleText or other Output?(T/O)")
if b == "T":
    EXP[0] = "00000000"
elif b == "O":
    pass#TODO : create other Output
else:
    print("incorect value")

    
#c = input("Where is ROM?")
#chdir(c)

#d = ""
d = str(input("ROM name"))


f = open(d,"r")
ROMf = f.read()
f.close()
f = open(d,"w")
f.write(ROMf)
f.close()  

    
    
for i in range(0, len(ROMf),8):
    ROM[licznik] = ROMf[i:i+8]
    licznik += 1


PC(RAM, ROM, EXP)  
#print("ROM",ROM,"\n")    
#print("RAM",RAM,"\n")
#print("EXP",EXP,"\n")   
