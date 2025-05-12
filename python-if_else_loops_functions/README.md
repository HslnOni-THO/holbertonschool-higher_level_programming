# Python - if/else, loops, functions

Bienvenue dans ce projet sur le contrôle du flux en Python. Vous allez découvrir l’importance de l’indentation, l’utilisation des conditions, des boucles, des fonctions et les bonnes pratiques de base pour écrire du code Python lisible et efficace.

---

## 🎯 Objectifs pédagogiques

À la fin de ce projet, vous serez capable d’expliquer et d’appliquer :

- Pourquoi l’**indentation** est essentielle en Python
- Comment utiliser les instructions `if`, `elif`, `else`
- Comment écrire des **commentaires**
- Comment affecter des valeurs à des **variables**
- Comment utiliser les boucles `while` et `for`
- Comment utiliser les instructions `break` et `continue`
- Comment utiliser la clause `else` sur les boucles
- À quoi sert l’instruction `pass` et quand l’utiliser
- Comment utiliser `range`
- Ce qu’est une **fonction** et comment la définir/appeler
- Ce que retourne une fonction sans instruction `return`
- La notion de **portée des variables** (scope)
- Ce qu’est un **traceback**
- Les **opérateurs arithmétiques** et leur utilisation

---

## 📝 Bonnes pratiques et style

- **Indentation** : Utilisez **4 espaces** par niveau d’indentation (recommandé par PEP8)[3][6][8]. L’indentation est obligatoire pour délimiter les blocs de code (après `if`, `for`, `while`, fonctions, etc.)[1][4][5][7].
- **Commentaires** : Utilisez `#` pour expliquer votre code.
- **Shebang** : La première ligne de chaque fichier doit être `#!/usr/bin/python3`.
- **pycodestyle** : Vérifiez la conformité de votre code avec la commande `pycodestyle`.
- **Fichiers** : Tous vos scripts doivent être exécutables et se terminer par une nouvelle ligne.

---

## 🚀 Exemples de base

### If / Else

x = 10
if x > 5:
print("x est supérieur à 5")
elif x == 5:
print("x vaut 5")
else:
print("x est inférieur à 5")

text

### Boucles

for i in range(3):
print(i) # Affiche 0, 1, 2

n = 0
while n < 3:
print(n)
n += 1

text

### Break, Continue, Else sur les boucles

for i in range(5):
if i == 3:
break
print(i)
else:
print("Boucle terminée sans break")

text

### Pass

if x > 5:
pass # À utiliser quand aucune action n’est nécessaire pour l’instant

text

### Fonctions

def hello(name):
print(f"Bonjour, {name}!")

hello("Alice")

text

---

## 📚 Ressources utiles

- [More Control Flow Tools (docs.python.org)][2]
- [IndentationError][1]
- [PEP8 – Guide de style Python][3]
- [Learn to Program 2 : Looping][4]
- [Pycodestyle][3]

---

## 🛠️ Exigences techniques

- **Éditeurs autorisés** : vi, vim, emacs
- **Python** : Version 3.8.* sur Ubuntu 20.04 LTS
- **Style** : Respect de pycodestyle (2.7.*)
- **Fichiers** : Exécutables, nouvelle ligne en fin de fichier, shebang obligatoire, README.md à la racine du projet

---

**Auteur** : Guillaume  
**Niveau** : Novice  
**Poids** : 1

---

Maîtrisez les bases du contrôle de flux et des fonctions pour écrire du code Python clair, robuste et professionnel !