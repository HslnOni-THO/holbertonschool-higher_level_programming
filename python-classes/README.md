# Python - Classes and Objects

Ce projet vous initie à la programmation orientée objet (OOP) en Python. Vous allez comprendre et manipuler les concepts de classes, d’objets, d’attributs, de méthodes, d’encapsulation et bien plus, pour écrire un code structuré, réutilisable et professionnel.

---

## 🎯 Objectifs

À la fin de ce projet, vous serez capable d’expliquer et d’appliquer :

- Ce qu’est la programmation orientée objet (OOP) et la notion de “first-class everything”
- Ce qu’est une **classe**, un **objet** et une **instance**
- Différences entre classe, objet et instance
- Ce qu’est un **attribut** (public, protégé, privé) et comment les utiliser
- Le rôle de `self`
- Ce qu’est une **méthode** et la méthode spéciale `__init__`
- Les notions d’**abstraction**, **encapsulation** et **information hiding**
- Ce qu’est une **propriété** et la différence entre attribut et propriété
- La manière pythonique d’écrire des getters et setters
- Comment créer dynamiquement de nouveaux attributs pour une instance existante
- Comment lier des attributs à des objets et des classes
- Ce que contient le `__dict__` d’une classe ou d’une instance
- Comment Python retrouve les attributs d’un objet ou d’une classe
- Utilisation de la fonction `getattr`

---

## 🚀 Exemples clés

class Animal:
"""Classe représentant un animal générique."""
def init(self, name):
"""Initialise un animal avec un nom."""
self.name = name # Attribut public

text
def speak(self):
    """Affiche un message générique."""
    print(f"{self.name} fait un bruit.")
Création d'une instance
chat = Animal("Minou")
chat.speak() # Minou fait un bruit.

Attribut dynamique
chat.age = 3

Propriété avec getter/setter pythonique
class Person:
"""Classe représentant une personne avec un âge."""
def init(self, age):
self._age = age # Attribut protégé

text
@property
def age(self):
    """Retourne l'âge de la personne."""
    return self._age

@age.setter
def age(self, value):
    """Définit l'âge de la personne."""
    if value < 0:
        raise ValueError("L'âge ne peut pas être négatif.")
    self._age = value
text

---

## 📚 Ressources utiles

- [Object Oriented Programming - Python Docs](https://docs.python.org/3/tutorial/classes.html)
- [Properties vs. Getters and Setters](https://realpython.com/python-property/)
- [Learn to Program 9 : Object Oriented Programming](https://www.youtube.com/watch?v=apACNr7DC_s)
- [Python Classes and Objects - W3Schools](https://www.w3schools.com/python/python_classes.asp)

---

## 🛠️ Exigences

- Python 3.8.5 sur Ubuntu 20.04 LTS
- Éditeurs : vi, vim, emacs
- Respect du style pycodestyle (2.7.*)
- Fichiers exécutables avec shebang `#!/usr/bin/python3`
- README.md obligatoire à la racine
- **Documentation obligatoire** :
    - Chaque module, classe et fonction doit avoir un docstring explicatif (voir [Google Style Python Docstrings](https://google.github.io/styleguide/pyguide.html#38-comments-and-docstrings))
- La longueur des fichiers sera vérifiée avec `wc`

---

**Auteur** : Guillaume  
**Niveau** : Amateur  
**Poids** : 1

---

Expérimentez, testez, documentez : l’OOP en Python n’aura plus de secrets pour vous !