#!/usr/bin/python3

# Usage: python3 frequence.py fichier_texte


import sys


alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def lire_fichier(fichier):
    """Lit le fichier et retourne tout le texte"""
    return open(fichier, 'r').read()

def compter_lettres(texte):
    """Compte combien de fois chaque lettre apparaît et le total"""
    Occurrences = {}
    length = 0
    for c in texte:
        if c in alphabet:
            Occurrences[c] = Occurrences.get(c, 0) + 1
            length += 1
    return Occurrences, length

def afficher_frequences(Occurrences, length):
    """Affiche chaque lettre avec sa fréquence (0 à 1)"""
    for c in alphabet:
        freq = Occurrences[c] / length if c in Occurrences else 0.0
        print(c, freq)

def main():
    """Fonction principale qui exécute le programme"""
    fichier = sys.argv[1]
    texte = lire_fichier(fichier)
    Occurrences, length = compter_lettres(texte)
    afficher_frequences(Occurrences, length)

# --- On lance le programme via main ---
if __name__ == "__main__":
    main()