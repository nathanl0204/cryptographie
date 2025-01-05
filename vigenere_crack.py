import string
import time

def texte():
    chaine=""
    flux=open("C://Users/Nathan/Documents/Programmation/Crypto/texte_vigenere.txt","r",encoding="utf-8")
    L=flux.readlines()
    L=[L[i].replace(" ","") for i in range(len(L))]
    L=[L[i].replace("\n","") for i in range(len(L))]
    for i in range(len(L)):
        chaine+=L[i]
    flux.close()
    return chaine

def cesar(chaine,dec):
    alph=string.ascii_uppercase
    s=chaine.upper()
    return s.translate(str.maketrans(alph, alph[dec:] + alph[:dec]))

def frequences(chaine):
    freq=[0]*26
    for c in chaine:
        if c in string.ascii_uppercase:
            freq[ord(c)-ord('A')]+=1
    somme=sum(freq)
    freq=[v/somme*1000.0 for v in freq]
    return freq

def cherche_cle_cesar(chaine):
    francais=[942,102,264,339,1587,95,104,77,841,89,0,534,324,715,514,286,106,646,790,726,624,215,0,30,24,32]
    corr=[0]*26 
    for dec in range(26):
        res=frequences(cesar(chaine,-dec))
        corr[dec]=sum(a*b for a,b in zip(res,francais))
    return corr.index(max(corr))

def tableau(chaine):
    L=[chaine]
    for i in range(1,len(L[0])):
        L.append(i*" "+L[0][:-i])
    return L

def coincidences(L):
    L2=[]
    compteur=0
    for i in range(1,len(L)):
        for j in range(len(L[i])):
            if L[i][j]==L[0][j]:
                compteur+=1
        L2.append(compteur)
        compteur=0
    return L2

def longueurCle(L):
    maxi=max(L)
    compteur=0
    compteur2=0
    L2=[]
    for i in range(len(L)):
        compteur+=1
        if L[i]>maxi-5 and L[i]<maxi+5:
            L2.append(compteur)
            compteur=0
    for i in range(2,max(L2)+1):
        for x in L2:
            if x%i==0:
                compteur2+=1
        if compteur2==len(L2):
            return i
        compteur2=0

def cherche_cle_vigenere(chaine,n) :
    return "".join(chr(ord('A')+cherche_cle_cesar(chaine[i::n])) for i in range(n))

def dechiffrement(chaine, cle):
    l = len(cle)
    key_as_int = [ord(i) for i in cle]
    ciphertext_int = [ord(i) for i in chaine]
    plaintext = ''
    for i in range(len(ciphertext_int)):
        value = (ciphertext_int[i] - key_as_int[i % l]) % 26
        plaintext += chr(value + 65)
    return plaintext

debut=time.time()
fichier=texte()
L=tableau(fichier)
L2=coincidences(L)
l=longueurCle(L2)
cle=cherche_cle_vigenere(fichier,l)
print(dechiffrement(fichier,cle))
fin=time.time()
duree=fin-debut
print("Temps d'exécution :",duree,"ms")