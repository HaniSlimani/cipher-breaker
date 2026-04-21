#!/usr/bin/python3

# Usage: python3 cesar.py clef c/d phrase
# Returns the result without additional text

import sys

def cesar(texte, clef, mode):
    # clef : entier (decalage)
    # mode : 'c' pour chiffrer, 'd' pour dechiffrer

    resultat = ""
    clef = ord(clef) - ord('A')   # on convertit en entier

    # si on dechiffre on inverse le decalage
    if mode == 'd':
        clef = -clef

    for lettre in texte:
        if 'A' <= lettre <= 'Z':
            position = ord(lettre) - ord('A')
            nouvelle_position = (position + clef) % 26
            resultat += chr(nouvelle_position + ord('A'))
        else:
            resultat += lettre

    return resultat


if __name__ == "__main__":

    clef = sys.argv[1]
    mode = sys.argv[2]
    phrase = sys.argv[3]

    print(cesar(phrase, clef, mode))