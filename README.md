# Bibliothèque d'algorithmes cryptographiques

Cette bibliothèque contient différentes implémentations d'algorithmes cryptographiques classiques et modernes (en Python).

## Contenu

### Chiffrement DES (Data Encryption Standard)
- Fichier : `Chiffrement DES.py`
- Implémentation complète de l'algorithme DES incluant :
    - Traitement du message et de la clé
    - Génération des 16 sous-clés
    - Permutations initiales et finales
    - Fonction de Feistel
    - S-boxes pour la substitution
- Le message chiffré est retourné en format hexadécimal

### Chiffrement de Vigenère
- Fichiers : `vigenere_chiffrement.py` et `vigenere_crack.py`
- Fonctionnalités :
    - Chiffrement classique avec génération de clé
    - Outil de cryptanalyse complet permettant de :
        - Analyser les fréquences
        - Détecter la longueur de la clé par analyse des coïncidences
        - Casser le chiffrement automatique
    - Inclut un fichier de test : `texte_vigenere.txt`

### RSA (Rivest-Shamir-Adleman)
- Fichier : `rsa.py`
- Caractéristiques :
    - Génération de nombres premiers avec test de Miller-Rabin
    - Calcul des clés publiques et privées
    - Chiffrement et déchiffrement
    - Utilisation de grands nombres (1024 bits) pour la sécurité

### Chiffrement de Vernam (One-Time Pad)
- Fichier : `vernam_chiffrement.py`
- Fonctionnalités :
    - Génération de clés aléatoires
    - Chiffrement par addition modulaire
    - Implémentation avec l'alphabet latin majuscule

## Exemples d'utilisation

### DES
```python
Message : MonMessage
Clé : MaCle
```

### Vigenère
```python
Message à chiffrer : MONMESSAGE
Clé : CLE
```

### RSA
```python
Message à chiffrer : 42
# Génère automatiquement les nombres premiers et la clé
```

### Vernam
```python
Texte à chiffrer : MONMESSAGE
# Génère automatiquement une clé de même longueur
```