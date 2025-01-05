# Implémentation de l'algorithme DES (Data Encryption Standard)

## Description
Ce projet est une implémentation en Python de l'algorithme de chiffrement DES (Data Encryption Standard). DES est un algorithme de chiffrement symétrique qui opère sur des blocs de 64 bits, utilisant une clé de 56 bits effectifs. Il est l'ancêtre de l'algorithme AES (Advanced Encryption Standard).

## Fonctionnalités
- Chiffrement de messages en utilisant l'algorithme DES
- Conversion de chaînes de caractères en binaire
- Génération de 16 sous-clés pour le processus de chiffrement
- Implémentation complète des S-boxes et des tables de permutation
- Sortie du message chiffré en format hexadécimal

## Utilisation
1. Exécuter le script
2. Entrer le message à chiffrer
3. Entrer la clé de déchiffrement
4. Le programme affichera le message chiffré en hexadécimal

Exemple :
```python
Message : MonMessage
Clé : MaCle123
```

## Détails techniques
- Le message est traité par blocs de 64 bits
- La clé est réduite à 56 bits effectifs
- 16 sous-clés sont générées pour les rounds de chiffrement
- Utilisation de 8 S-boxes pour la substitution non-linéaire
- Plusieurs étapes de permutation pour assurer la diffusion