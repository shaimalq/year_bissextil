def bissextile(n):
    if(n%4 and n!=100 or n%400):
       k=True
    else:
        k=False
        return k

def siecle(s):
    for i in((s-1)*100,(s-1)*100+99):
     if bissextile(i)==True:
        print(i)

annee=input("entrer l' annee:")
print(annee,"est bissextile")
for i in ((annee-1)*100,(annee-1)*100+99):
    print(i)