# Python - More Data Structures: Set, Dictionary

Ce projet vous fait découvrir deux structures de données puissantes de Python : **les ensembles (sets)** et **les dictionnaires (dicts)**. Vous apprendrez aussi à utiliser les fonctions lambda, map, filter et reduce pour manipuler vos données efficacement.

---

## 🎯 Objectifs

- Comprendre et utiliser les **sets** (ensembles) : création, méthodes courantes, itération, différences avec les listes
- Savoir quand utiliser un set plutôt qu’une liste
- Comprendre et utiliser les **dictionnaires** : création, clés/valeurs, itération, différences avec listes et sets
- Savoir quand utiliser un dictionnaire
- Maîtriser les **lambda functions** et les fonctions **map, filter, reduce**

---

## 🚀 Exemples clés

Set (ensemble)
fruits = {'pomme', 'banane', 'orange'}
fruits.add('kiwi')
fruits.remove('banane')
for fruit in fruits:
print(fruit)

Dictionnaire
ages = {'Alice': 25, 'Bob': 30}
ages['Charlie'] = 20
for name, age in ages.items():
print(name, age)

Lambda, map, filter, reduce
f = lambda x: x * 2
result = list(map(f, [1, # [2,ens = list(filter(lambda x: x % 2 == 0, [1, #

from functools import reduce
total = reduce(lambda x, y: x + y, [1, 2,0

text

---

## 🛠️ Exigences

- Python 3.8.5 sur Ubuntu 20.04 LTS
- Éditeurs : vi, vim, emacs
- Respect du style pycodestyle (2.7.*)
- Fichiers exécutables avec shebang `#!/usr/bin/python3`
- README.md obligatoire à la racine

---

**Auteur** : Guillaume  
**Niveau** : Novice  
**Poids** : 1

---

Apprenez à manipuler efficacement vos données avec les sets, les dictionnaires et les fonctions fonctionnelles de Python !