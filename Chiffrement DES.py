#<---------------- Traitement du message et de la clé ----------------------->

message = str(input("Message : "))

#Conversion str en binaire (sert pour le message et la clé)

def str_vers_bin(chaine):
    sequence = ""
    for lettre in chaine:
        bits = format(ord(lettre),"b")
        while len(bits) < 8:
            bits = "0"+bits
        sequence += bits
    return sequence

message = str_vers_bin(message) #Le message en clair est convertit en binaire

#On divise le message (de taille 64 bits) en deux parties (de 32 bits)

def coupe_en_deux(chaine):
    return chaine[:len(chaine)//2],chaine[len(chaine)//2:]

cle = str(input("Clé : "))
cle = str_vers_bin(cle) #La clé est aussi convertie en binaire

#<---------------- Création de 16 sous-clés de 48 bits ----------------------->

#On utilise un tableau de permutations pour créer une nouvelle clé de 56 bits (les bits de poids faible ne sont pas utilisés)
PC_1 = [57,49,41,33,25,17,9,
        1,58,50,42,34,26,18,
        10,2,59,51,43,35,27,
        19,11,3,60,52,44,36,
        63,55,47,39,31,23,15,
        7,62,54,46,38,30,22,
        14,6,61,53,45,37,29,
        21,13,5,28,20,12,4]

def permutation(sequence,tableau):
    nv_sequence = ""
    for i in tableau:
        nv_sequence += sequence[i-1]
    return nv_sequence

cle_prime = permutation(cle,PC_1) #Nouvelle clé

gauche_0,droite_0 = coupe_en_deux(cle_prime) #On divise la nouvelle clé (de taille 56 bits) en deux parties (de 28 bits)

#Pour créer les 16 sous-clés, on réalise d'abord des décalages à gauche successifs en partant de gauche_0 et droite_0
nb_dec_gauche = [1,1,2,2,2,2,2,2,1,2,2,2,2,2,2,1] #Spécifie le nombre de décalages à gauche à réaliser à chaque itération

#Décalage à gauche
def decalage_gauche(g,d,n):
    for i in range(n):
        g,d = g[1:] + g[0], d[1:] + d[0]
    return g,d

#Itération des décalages à gauche à partir de gauche_0 et droite_0
def itere(g,d):
    iteres = []
    for i in range(len(nb_dec_gauche)):
        g,d = decalage_gauche(g,d,nb_dec_gauche[i])
        sequence = g+d
        iteres.append(sequence)
    return iteres

concatenes = itere(gauche_0,droite_0)

#On utilise à nouveau un tableau de permutations pour former les 16 sous-clés
PC_2 = [14,17,11,24,1,5,
        3,28,15,6,21,10,
        23,19,12,4,26,8,
        16,7,27,20,13,2,
        41,52,31,37,47,55,
        30,40,51,45,33,48,
        44,49,39,56,34,53,
        46,42,50,36,29,32]

#Formation des sous-clés
def sous_cles():
    ss_cles = []
    for i in range(16):
        ss_cles.append(permutation(concatenes[i],PC_2))
    return ss_cles

ss_cles = sous_cles()

#<---------------- Opération initiale sur le message ----------------------->

#Permutation initiale des 64 bits du message à l'aide du tableau ci-dessous
IP = [58,50,42,34,26,18,10,2,
    60,52,44,36,28,20,12,4,
    62,54,46,38,30,22,14,6,
    64,56,48,40,32,24,16,8,
    57,49,41,33,25,17,9,1,
    59,51,43,35,27,19,11,3,
    61,53,45,37,29,21,13,5,
    63,55,47,39,31,23,15,7]

message_prime = permutation(message,IP)

gauche,droite = coupe_en_deux(message_prime) #On divise message_prime (de taille 64 bits) en deux parties (de 32 bits)

#On procède ensuite à 16 itérations sur les blocs gauche et droite à l'aide d'une fonction f calculée ci-dessous

#<---------------- Calcul des itérations de f ----------------------->

#On utilise un tableau pour "étendre" un bloc droite de 32 bits à 48 bits
E = [32,1,2,3,4,5,
    4,5,6,7,8,9,
    8,9,10,11,12,13,
    12,13,14,15,16,17,
    16,17,18,19,20,21,
    20,21,22,23,24,25,
    24,25,26,27,28,29,
    28,29,30,31,32,1]

#On fait ensuite l'opération "xor" entre le bloc droit "étendu" et la sous_clé correspondant au tour en cours
def xor(a,b):
    res = int(a,2) ^ int(b,2)
    return bin(res)[2:].zfill(len(a))

#On utilise maintenant les "S-boxes" pour asocier à chaque groupe de 6 bits du résultat précédent
#un nombre de 4 bits. Celles-ci sont implémentées ici sous forme de matrices puisqu'on utilise ici
#les coordonnées lignes/colonnes

S1 = [[14,4,13,1,2,15,11,8,3,10,6,12,5,9,0,7],
    [0,15,7,4,14,2,13,1,10,6,12,11,9,5,3,8],
    [4,1,14,8,13,6,2,11,15,12,9,7,3,10,5,0],
    [15,12,8,2,4,9,1,7,5,11,3,14,10,0,6,13]]

S2 = [[15,1,8,14,6,11,3,4,9,7,2,13,12,0,5,10],
    [3,13,4,7,15,2,8,14,12,0,1,10,6,9,11,5],
    [0,14,7,11,10,4,13,1,5,8,12,6,9,3,2,15],
    [13,8,10,1,3,15,4,2,11,6,7,12,0,5,14,9]]

S3 = [[10,0,9,14,6,3,15,5,1,13,12,7,11,4,2,8],
    [13,7,0,9,3,4,6,10,2,8,5,14,12,11,15,1],
    [13,6,4,9,8,15,3,0,11,1,2,12,5,10,14,7],
    [1,10,13,0,6,9,8,7,4,15,14,3,11,5,2,12]]

S4 = [[7,13,14,3,0,6,9,10,1,2,8,5,11,12,4,15],
    [13,8,11,5,6,15,0,3,4,7,2,12,1,10,14,9],
    [10,6,9,0,12,11,7,13,15,1,3,14,5,2,8,4],
    [3,15,0,6,10,1,13,8,9,4,5,11,12,7,2,14]]

S5 = [[2,12,4,1,7,10,11,6,8,5,3,15,13,0,14,9],
    [14,11,2,12,4,7,13,1,5,0,15,10,3,9,8,6],
    [4,2,1,11,10,13,7,8,15,9,12,5,6,3,0,14],
    [11,8,12,7,1,14,2,13,6,15,0,9,10,4,5,3]]

S6 = [[12,1,10,15,9,2,6,8,0,13,3,4,14,7,5,11],
    [10,15,4,2,7,12,9,5,6,1,13,14,0,11,3,8],
    [9,14,15,5,2,8,12,3,7,0,4,10,1,13,11,6],
    [4,3,2,12,9,5,15,10,11,14,1,7,6,0,8,13]]

S7 = [[4,11,2,14,15,0,8,13,3,12,9,7,5,10,6,1],
    [13,0,11,7,4,9,1,10,14,3,5,12,2,15,8,6],
    [1,4,11,13,12,3,7,14,10,15,6,8,0,5,9,2],
    [6,11,13,8,1,4,10,7,9,5,0,15,14,2,3,12]]

S8 = [[13,2,8,4,6,15,11,1,10,9,3,14,5,0,12,7],
    [1,15,13,8,10,3,7,4,12,5,6,11,0,14,6,2],
    [7,11,4,1,9,12,14,2,0,6,10,13,15,3,5,8],
    [2,1,14,7,4,10,8,13,15,12,9,0,3,5,6,11]]

#Calcul des images des groupes de 6 bits par les "S-boxes"
def sbox(n):
    res = ""
    boxes = [S1,S2,S3,S4,S5,S6,S7,S8]
    x = 0
    for k in range(0,len(n),6):
        box = boxes[x]
        nbr = n[k:k+6]
        i = nbr[0] + nbr[-1]
        i = int(i,2)
        j = nbr[1:-1]
        j = int(j,2)
        res += '{0:04b}'.format(box[i][j])
        x += 1
    return res

#L'opération finale pour calculer f est une permutation, à l'aide du tableau ci-dessous
P = [16,7,20,21,
    29,12,28,17,
    1,15,23,26,
    5,18,31,10,
    2,8,24,14,
    32,27,3,9,
    19,13,30,6,
    22,11,4,25]

#Calcul final
def f(r,k):
    res = permutation(r,E) #Attention, plutôt une "expansion" ici
    res = xor(k,res)
    res = sbox(res)
    res = permutation(res,P)
    return res

#Itérations
def itere_avec_f(g,d):
    for i in range(16):
        g,d = d,xor(g,f(d,ss_cles[i]))
    return g,d

gauche,droite = itere_avec_f(gauche,droite)

message_crypte = droite + gauche #On inverse l'ordre des deux blocs

#On applique une dernière permutation à l'aide du tableau ci-dessous
IP_inv = [40,8,48,16,56,24,64,32,
        39,7,47,15,55,23,63,31,
        38,6,46,14,54,22,62,30,
        37,5,45,13,53,21,61,29,
        36,4,44,12,52,20,60,28,
        35,3,43,11,51,19,59,27,
        34,2,42,10,50,18,58,26,
        33,1,41,9,49,17,57,25]

message_crypte = permutation(message_crypte,IP_inv)
message_crypte = f'{int(message_crypte,2):X}' #Conversion en hexadécimal
print(message_crypte)