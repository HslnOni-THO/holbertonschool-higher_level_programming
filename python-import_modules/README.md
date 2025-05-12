# Python - Import & Modules

Bienvenue dans ce projet dédié à l’utilisation des **modules** et de l’**import** en Python.  
Vous apprendrez à organiser votre code, à réutiliser des fonctions, à utiliser les arguments en ligne de commande, et à respecter les bonnes pratiques de style Python.

---

## 🎯 Objectifs pédagogiques

À la fin de ce projet, vous serez capable d’expliquer et d’appliquer :

- Pourquoi la programmation Python est puissante et flexible
- Comment **importer des fonctions** ou modules depuis un autre fichier (`import`, `from ... import ...`)
- Comment **utiliser les fonctions importées** dans vos scripts
- Comment **créer un module** Python (fichier `.py` avec fonctions/routines)
- Comment utiliser la fonction intégrée `dir()` pour explorer le contenu d’un module
- Comment **empêcher l’exécution de code** lors de l’import d’un script (`if __name__ == "__main__":`)
- Comment **utiliser les arguments de la ligne de commande** avec `sys.argv` ou `argparse`

---

## 📝 Bonnes pratiques et style

- Placez vos instructions `import` en début de fichier.
- Utilisez `pycodestyle` pour vérifier la conformité de votre code.
- Tous vos scripts doivent commencer par `#!/usr/bin/python3`, être exécutables, et se terminer par une nouvelle ligne.

---

## 🚀 Exemples d’utilisation

**Importer un module entier :**
import example
example.add(4, 5) # Utilisation de la fonction add du module example

text

**Importer une fonction spécifique :**
from example import add
add(4, 5) # Utilisation directe de la fonction add

text

**Importer plusieurs fonctions :**
from example import add, sub

text

**Importer tout (à éviter en production) :**
from example import *

text

**Lister le contenu d’un module :**
import example
print(dir(example))

text

**Protéger le point d’entrée d’un script :**
if name == "main":
# Ce code ne s’exécute pas lors d’un import
main()

text

**Arguments en ligne de commande :**
import sys
print(sys.argv) # Affiche la liste des arguments passés au script

text

---

## 📚 Ressources utiles

- [Modules - Python Docs](https://docs.python.org/3/tutorial/modules.html)
- [Command line arguments](https://docs.python.org/3/library/sys.html#sys.argv)
- [Pycodestyle – Guide de style Python Code](https://pycodestyle.pycqa.org/en/latest/)

---

## 🛠️ Exigences techniques

- **Éditeurs autorisés** : vi, vim, emacs
- **Python** : Version 3.10.* sur Ubuntu 22.04 LTS
- **Style** : Respect de pycodestyle (2.7.*)
- **Fichiers** : Exécutables, nouvelle ligne en fin de fichier, shebang obligatoire, README.md à la racine du projet

---

**Auteur** : Guillaume  
**Niveau** : Novice  
**Poids** : 1

---

Organisez, réutilisez et rendez votre code plus puissant grâce aux modules Python !