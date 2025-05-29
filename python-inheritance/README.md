# Python - Héritage (Niveau Master)

Ce projet approfondit le concept d’**héritage** en Python, y compris l’héritage multiple, le polymorphisme et l’utilisation des fonctions intégrées `super()`, `isinstance()` et `issubclass()`. Vous maîtriserez la création de hiérarchies de classes élégantes et réutilisables.

---

## 🎯 Objectifs Pédagogiques

À la fin de ce projet, vous serez capable d’expliquer et d’appliquer :

- Ce qu'est une **superclasse** (classe parente) et une **sous-classe**
- Comment lister tous les attributs/méthodes d'une classe ou instance (`dir()`)
- Quand une instance peut avoir de nouveaux attributs
- Comment hériter d'une classe et **surcharger** des méthodes/attributs
- Comment définir une classe avec **héritage multiple**
- La classe de base par défaut (`object`)
- Le rôle de l'héritage et son utilité dans la conception logicielle
- L'utilisation de `isinstance()`, `issubclass()`, `type()` et `super()`

---

## 🚀 Exemples Clés

### Héritage Simple et Surcharge
class Animal:
"""Classe parente générique."""
def init(self, nom):
self.nom = nom

text
def parler(self):
    print("Je suis un animal.")
class Chien(Animal):
"""Sous-classe spécialisée."""
def parler(self):
print("Woof!")
super().parler() # Appel de la méthode parente

Utilisation
a = Animal("Generic")
a.parler() # Je suis un animal.

c = Chien("Rex")
c.parler() # Woof! \n Je suis un animal.

text

### Héritage Multiple et MRO
class A:
def methode(self):
print("A")

class B(A):
def methode(self):
print("B")
super().methode()

class C(A):
def methode(self):
print("C")
super().methode()

class D(B, C):
pass

d = D()
d.methode() # B → C → A (suivi du MRO)
print(D.mro) # Ordre de résolution des méthodes

text

### Vérifications de Type
print(isinstance(d, A)) # True
print(issubclass(D, B)) # True
print(type(d) is D) # True

text

---

## 📚 Ressources Utiles

- [Héritage en Python - Documentation Officielle](https://docs.python.org/3/tutorial/classes.html#inheritance)
- [Héritage Multiple et MRO](https://realpython.com/python-super/)
- [Tutoriel Héritage - Learn to Program 10](https://www.youtube.com/watch?v=dQw4w9WgXcQ) (lien générique)

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
- **Tests** :
  - Dossier `tests/` avec fichiers `.txt`
  - Exécution : `python3 -m doctest ./tests/*`
  - Couverture des cas limites (edge cases)

---

**Auteur** : Guillaume  
**Niveau** : Master  
**Poids** : 1

---

L’héritage est un pilier de la POO. Maîtrisez ces concepts pour concevoir des architectures logicielles modulaires et extensibles ! 🧩