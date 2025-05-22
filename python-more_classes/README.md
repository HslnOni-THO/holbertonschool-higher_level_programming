# Python - More Classes and Objects (Niveau Master)

Plongez dans les concepts avancés de la programmation orientée objet (POO) en Python : attributs de classe, méthodes statiques, méthodes spéciales et bien plus. Ce projet renforce votre maîtrise de l’OOP pour écrire un code robuste et professionnel.

---

## 🎯 Objectifs Pédagogiques

À la fin de ce projet, vous serez capable d’expliquer et d’appliquer :

- La différence entre **attributs de classe** et **attributs d’instance**
- L’utilisation des méthodes de classe (`@classmethod`) et méthodes statiques (`@staticmethod`)
- Les méthodes spéciales `__str__` (pour l’utilisateur) et `__repr__` (pour le développeur)
- La différence entre `__str__` et `__repr__`
- Les bonnes pratiques pour les propriétés (properties) vs getters/setters
- La création dynamique d’attributs et la liaison à des objets/classes
- Le rôle de `__dict__` et son contenu pour les classes/instances
- Comment Python résout la recherche d’attributs (MRO)
- L’utilisation de `getattr()` pour accéder aux attributs dynamiquement

---

## 🚀 Exemples Clés

### Attributs de Classe vs Instance
class Compteur:
compteur_classe = 0 # Attribut de classe

text
def __init__(self):
    self.compteur_instance = 0  # Attribut d'instance
    Compteur.compteur_classe += 1
Utilisation
a = Compteur()
b = Compteur()
print(a.compteur_instance) # 0 (instance)
print(Compteur.compteur_classe) # 2 (classe)

text

### Méthodes de Classe et Statiques
class Date:
def init(self, jour, mois):
self.jour = jour
self.mois = mois

text
@classmethod
def from_string(cls, chaine):
    jour, mois = map(int, chaine.split('-'))
    return cls(jour, mois)

@staticmethod
def est_valide(jour, mois):
    return 1 <= jour <= 31 and 1 <= mois <= 12
Utilisation
date = Date.from_string("25-12")
print(Date.est_valide(25, 12)) # True

text

### `__str__` vs `__repr__`
class Point:
def init(self, x, y):
self.x = x
self.y = y

text
def __str__(self):
    return f"Point({self.x}, {self.y})"

def __repr__(self):
    return f"Point(x={self.x}, y={self.y})"
p = Point(3, 4)
print(str(p)) # Point(3, 4) (user-friendly)
print(repr(p)) # Point(x=3, y=4) (debugging)

text

---

## 📚 Ressources Utiles

- [Python Classes and Objects](https://docs.python.org/3/tutorial/classes.html)
- [Class and Instance Attributes](https://www.geeksforgeeks.org/class-instance-attributes-python/)
- [Python @classmethod and @staticmethod](https://realpython.com/instance-class-and-static-methods-demystified/)
- [str() vs repr() in Python](https://www.journaldev.com/22460/python-str-repr)

---

## 🛠️ Exigences Techniques

- **Python 3.8.5** sur Ubuntu 20.04 LTS
- **Éditeurs autorisés** : vi, vim, emacs
- **Style** : Conformité à pycodestyle (2.7.*)
- **Documentation** :
  - Docstrings obligatoires pour modules, classes et méthodes (format [Google Style](https://google.github.io/styleguide/pyguide.html))
  - Vérification via :  
    ```
    python3 -c 'print(__import__("my_module").__doc__)'
    ```
- **Fichiers** : Exécutables, shebang `#!/usr/bin/python3`, nouvelle ligne en fin de fichier

---

**Auteur** : Guillaume  
**Niveau** : Master  
**Poids** : 1

---

Ce projet vous prépare à concevoir des architectures logicielles élégantes et maintenables en exploitant pleinement la puissance de l’OOP en Python. Bon code ! 🚀