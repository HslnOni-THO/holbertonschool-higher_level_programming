# Python - Data Structures: Lists, Tuples

Ce projet vous initie aux structures de données fondamentales en Python : **listes** et **tuples**. Vous apprendrez leurs différences, méthodes courantes, et notions clés comme le packing/unpacking.

---

## 🎯 Objectifs

- Comprendre et utiliser les listes (mutables) et tuples (immutables)
- Différences et similitudes entre chaînes et listes
- Méthodes fréquentes des listes (append, remove, insert)
- Utiliser listes comme piles (stack) et files (queue)
- Maîtriser les list comprehensions
- Comprendre séquences, tuple packing/unpacking
- Utiliser l’instruction `del`

---

## 🚀 Exemples clés

Listes et tuples
my_list =
my_tuple = (1, 2, 3)

Modifier liste
my_list = 10

Méthodes listes
my_list.append(4)
my_list.remove(2)

Pile (stack)
stack = []
stack.append(1)
stack.pop()

File (queue)
from collections import deque
queue = deque()
queue.append(1)
queue.popleft()

List comprehension
squares = [x**2 for x in range(5)]

Packing/unpacking
coords = (10, 20)
x, y = coords

Del
del my_list

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

Maîtrisez ces bases pour écrire un code Python clair et efficace !