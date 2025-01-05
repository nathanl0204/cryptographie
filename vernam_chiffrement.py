import random
import string

def genererCle(longueur):
    lettres = string.ascii_uppercase
    res = ''.join(random.choice(lettres) for i in range(longueur))
    return res

alphabet = {"A":0, "B":1, "C":2, "D":3, "E":4, "F":5, "G":6, "H":7, "I":8,
            "J":9, "K":10, "L":11, "M":12, "N":13, "O":14, "P":15, "Q":16,
            "R":17, "S":18, "T":19, "U":20, "V":21, "W":22, "X":23, "Y":24,
            "Z":25}

def cleDico(dico,valeur):
    for cle, val in dico.items():
        if valeur == val:
            return cle
    return "La clé n'existe pas"

def chiffrement(texte,cle):
    #assert (len(cle) == len(texte), "La clé doit être de la taille du texte ! ")
    L_cle = []
    L_texte = []
    L_res = []
    res = ""
    for x in cle:
        L_cle.append(alphabet[x])
    for y in texte:
        L_texte.append(alphabet[y])
    for i in range(len(L_texte)):
        n = L_texte[i] + L_cle[i]
        if n >= 26:
            L_res.append(n-26)
        else:
            L_res.append(n)
    for z in L_res:
        res += cleDico(alphabet,z)
    return res

texte = str(input("Texte à chiffrer : "))
cle = genererCle(len(texte))
print(chiffrement(texte,cle))