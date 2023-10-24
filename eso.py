print("CSKA: 2023.10.22. szoft1")

a=float(input("Add meg a múlt heti csapadékmenyyiséget mm-ben: "))
b=float(input("Add meg az eheti csapadékmennyiséget mm-ben:"))
print("Csapadék mennyiség milliméterben:", a+b)
print("Aktuális heti csapadék: ", b)
print ("Előző heti csapadék: ", a)
if a>b:
    print("Kevesebb csapadék")
if a<b:
    print("Több csapadék")
if a==b:
    print("Ugyanannyi csapadék")
