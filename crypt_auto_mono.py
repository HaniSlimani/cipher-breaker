#!/usr/bin/python3

# Usage python3 crypt_auto_mono.py file
# Where file contains the ciphertext

import sys
import math
import random

def load_tetragrams(filepath="nb_tetra_fr.csv"):
    tetragrams = {}
    with open(filepath, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            parts = line.split(";")
            if len(parts) >= 2:
                tetra = parts[0].strip().upper()
                try:
                    count = float(parts[1].strip())
                    tetragrams[tetra] = count
                except ValueError:
                    pass
    return tetragrams

UNKNOWN_COUNT = 0.001

def evaluate(text, tetragrams):
    score = 0.0
    for i in range(len(text) - 3):
        tetra = text[i:i+4]
        count = tetragrams.get(tetra, UNKNOWN_COUNT)
        score += math.log(count)
    return score

def apply_substitution(ciphertext, key):
    result = []
    for c in ciphertext:
        if c.isalpha():
            result.append(key[ord(c.upper()) - ord('A')])
        else:
            result.append(c)
    return ''.join(result)

def swap_two(key):
    key = list(key)
    i, j = random.sample(range(26), 2)
    key[i], key[j] = key[j], key[i]
    return ''.join(key)

# ---- Read ciphertext ----
with open(sys.argv[1], "r", encoding="utf-8") as f:
    raw = f.read()

ciphertext = ''.join(c.upper() for c in raw if c.isalpha())

tetragrams = load_tetragrams("nb_tetra_fr.csv")

ciphertext_eval = evaluate(ciphertext, tetragrams)

# ---- Iterative hill-climbing with restarts ----
MAX_ITER = 15000
MAX_NO_IMPROVE = 2000

best_key = None
best_eval = float('-inf')
best_text = ""

for restart in range(3):
    decryption_key = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    random.shuffle(decryption_key)
    decryption_key = ''.join(decryption_key)

    current_text = apply_substitution(ciphertext, decryption_key)
    current_eval = evaluate(current_text, tetragrams)

    no_improve = 0

    for it in range(1, MAX_ITER + 1):
        new_key = swap_two(decryption_key)
        new_text = apply_substitution(ciphertext, new_key)
        new_eval = evaluate(new_text, tetragrams)

        if new_eval > current_eval:
            decryption_key = new_key
            current_eval = new_eval
            current_text = new_text
            no_improve = 0
        else:
            no_improve += 1

        if no_improve >= MAX_NO_IMPROVE:
            break

    if current_eval > best_eval:
        best_eval = current_eval
        best_key = decryption_key
        best_text = current_text

plaintext = best_text
plaintext_eval = best_eval
decryption_key = best_key

# Compute encryption_key (inverse of decryption_key)
encryption_key = ['A'] * 26
for i in range(26):
    encryption_key[ord(decryption_key[i]) - ord('A')] = chr(ord('A') + i)
encryption_key = ''.join(encryption_key)

iter_total = MAX_ITER * 3

# Do not modify these lines except for variable names
print ("texte chiffré\n" + ciphertext)
print ("évaluation " + str(ciphertext_eval))
print ("\nAprès " + str(iter_total) + " itérations, texte déchiffré\n" + plaintext)
print ("substitution appliquée au texte fourni " + encryption_key)
print ("clef " + decryption_key)
print ("évaluation " + str(plaintext_eval))