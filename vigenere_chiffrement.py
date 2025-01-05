def genererCle(mot,cle):
    cle=list(cle) 
    if len(mot)==len(cle): 
        return(cle) 
    else: 
        for i in range(len(mot)-len(cle)): 
            cle.append(cle[i%len(cle)]) 
    return("".join(cle)) 
  
def chiffrement(mot,cle): 
    texte_crypté=[] 
    for i in range(len(mot)): 
        x =(ord(mot[i])+ord(cle[i]))%26
        x+=ord('A') 
        texte_crypté.append(chr(x)) 
    return("".join(texte_crypté))

mot=input("Message à chiffrer : ")
mot_clé=input("Clé : ")
clé=genererCle(mot,mot_clé)
texte_crypté=chiffrement(mot,clé)
print("Message chiffré : ", texte_crypté)