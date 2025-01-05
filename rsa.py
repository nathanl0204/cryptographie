""""Mémo : Les attaques par la force brute sur le chiffrement RSA reposent
essentiellement sur la nécessité de connaître le produit initial n=p*q et de
décomposer n en produit de facteurs premiers. Cette décomposition croît
exponentiellement avec la longueur de la clé. À ce jour, il n'existe pas
d'algorithme de ce type pour réaliser une attaque par la force brute avec
des ordinateurs classiques."""

import random

def testMillerRabin(n,nbessais): #test de primalité probabiliste
    nbMaxDivisionsPar2=0
    composantPair=n-1
    while composantPair%2==0:
        composantPair>>=1
        nbMaxDivisionsPar2+=1
    assert(2**nbMaxDivisionsPar2*composantPair==n-1)
    def compositeTest(test):
        if pow(test,composantPair,n)==1:
            return False
        for i in range(nbMaxDivisionsPar2):
            if pow(test,2**i*composantPair,n)==n-1:
                return False
        return True
    for i in range(nbessais):
        test=random.randrange(2,n)
        if compositeTest(test):
            return False
    return True

def nombreAleatoire(n):
    nb=random.randrange(2**(n-1)+1,2**n-1)
    while not(testMillerRabin(nb,100)):
        nb=random.randrange(2**(n-1)+1,2**n-1)
    return nb

def euclide_etendu(a, b):
    r0,u0,v0=a,1,0
    r1,u1,v1=b,0,1
    while r1!=0:
        r2=r0%r1
        q2=r0//r1
        u,v=u0,v0
        r0,u0,v0=r1,u1,v1
        r1,u1,v1=r2,u-q2*u1,v-q2*v1
    return r0,u0,v0

def cle_privee(p,q,e):
    n=p*q
    phi=(p-1)*(q-1)
    c,d,dd=euclide_etendu(e,phi)
    return d%phi

def chiffrement_rsa(m,n,e):
    return pow(m,e,n)

def dechiffrement_rsa(x,n,d):
    return pow(x,d,n)

def rsa(p,q,e,m):
    d=cle_privee(p,q,e)
    n=p*q
    x=chiffrement_rsa(m,n,e)
    mdéchiffré=dechiffrement_rsa(x,n,d)
    return x,mdéchiffré

message=int(input("Message à chiffer : "))
print(rsa(nombreAleatoire(1024),nombreAleatoire(1024),nombreAleatoire(1024),message))