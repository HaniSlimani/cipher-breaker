# Cipher Breaker

Boîte à outils Python pour le chiffrement, le déchiffrement et la **cryptanalyse automatique** de chiffrements mono-alphabétiques (César et substitution simple).

## Fonctionnalités

### Chiffrement
- **Chiffre de César** — décalage paramétrable
- **Substitution mono-alphabétique** — chaque lettre remplacée par une autre selon une clé arbitraire

### Cryptanalyse
- **Analyse de fréquences** des lettres et histogramme
- **Identification de la langue** d'un texte chiffré par comparaison à des distributions de référence
- **Cryptanalyse automatique par hill climbing** sur les fréquences de tétragrammes (groupes de 4 lettres) — casse une substitution mono-alphabétique sans connaissance de la clé

### Méthode du hill climbing

L'algorithme évalue la qualité d'un déchiffrement en sommant les `log` des fréquences des tétragrammes du texte dans un corpus français de référence. À chaque itération :

1. Permuter aléatoirement deux lettres dans la clé candidate
2. Recalculer le score
3. Si le score s'améliore, garder la nouvelle clé ; sinon revenir en arrière
4. S'arrêter après N itérations sans amélioration

Cette approche dégrossit rapidement le travail, là où une cryptanalyse manuelle serait fastidieuse.

## Structure

```
.
├── cesar.py                  # Chiffrement / déchiffrement César
├── subst_mono.py             # Chiffrement / déchiffrement mono-alphabétique
├── frequence.py              # Calcul des fréquences de lettres
├── cryptanalyse_subst.py     # Cryptanalyse interactive (assistée)
├── crypt_auto_mono.py        # Cryptanalyse automatique (hill climbing)
├── nb_tetra_fr.csv           # Table de référence des tétragrammes français
├── nettoie                   # Script bash : retire accents, ponctuation, espaces
├── dessine_histogramme       # Script bash : visualise un histogramme via gnuplot
├── textes/                   # Corpus de test
├── test-1-ex1-mono.py        # Tests fréquences
├── test-2-ex2-mono.py        # Tests chiffrement
├── test-3-ex3-mono.py        # Tests cryptanalyse
└── test-all.sh               # Lance la batterie complète
```

## Utilisation

### Calcul de fréquences sur un texte

```bash
./nettoie texte_brut texte_propre
python3 frequence.py texte_propre
```

### Affichage de l'histogramme

```bash
./nettoie < texte_brut | python3 frequence.py | ./dessine_histogramme
```

Nécessite `gnuplot` et `imagemagick` :
```bash
sudo apt install gnuplot imagemagick
```

### Cryptanalyse automatique

```bash
python3 crypt_auto_mono.py texte_chiffre
```

### Tests

```bash
./test-all.sh
```

## Dépendances

- Python 3
- `gnuplot` + `imagemagick` (pour l'affichage des histogrammes uniquement)

## Auteurs

- Hani Slimani
- [@akkaboutaina](https://github.com/akkaboutaina)
