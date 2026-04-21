#!/usr/bin/python3

# Usage: python3 subst_mono.py CLEF c/d TEXTE
# CLEF : permutation des 26 lettres (ex: QWERTYUIOPASDFGHJKLZXCVBNM)

import sys

ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def subst_mono(texte, clef, mode):
    resultat = ""

    # Sécurité : vérifier que la clef est valide
    if len(clef) != 26:
        print("Erreur : la clef doit contenir 26 lettres.")
        sys.exit(1)

    if mode == 'c':  # chiffrement
        for lettre in texte:
            if lettre in ALPHABET:
                index = ALPHABET.index(lettre)
                resultat += clef[index]
            else:
                resultat += lettre

    elif mode == 'd':  # déchiffrement
        for lettre in texte:
            if lettre in ALPHABET:
                index = clef.index(lettre)
                resultat += ALPHABET[index]
            else:
                resultat += lettre

    else:
        print("Erreur : mode doit être 'c' ou 'd'")
        sys.exit(1)

    return resultat


if __name__ == "__main__":
    clef = sys.argv[1]
    mode = sys.argv[2]
    texte = sys.argv[3]

    print(subst_mono(texte, clef, mode))