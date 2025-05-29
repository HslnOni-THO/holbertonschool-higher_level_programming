# Python - Classes Abstraites et Interfaces (Niveau Amateur)

Plongez dans les concepts avancés de la POO en Python : classes abstraites, interfaces, duck typing et sous-classage des collections standard. Ce projet vous apprendra à concevoir des architectures flexibles et maintenables.

---

## 🎯 Objectifs Pédagogiques

À la fin de ce projet, vous serez capable d’expliquer et d’appliquer :

- L'utilisation des **classes abstraites** pour définir des contrats communs
- Le concept d’**interfaces** et de **duck typing** pour le polymorphisme
- Le sous-classage des types natifs (listes, dictionnaires) pour des comportements personnalisés
- La **surcharge de méthodes** pour adapter les fonctionnalités héritées
- L’**héritage multiple** et les **mixins** pour composer des comportements
- L’implémentation de méthodes abstraites avec le module `abc`

---

## 🚀 Concepts Clés et Exemples

### Classe Abstraite avec `abc`
from abc import ABC, abstractmethod

class Forme(ABC):
@abstractmethod
def aire(self):
pass

class Cercle(Forme):
def init(self, rayon):
self.rayon = rayon

text
def aire(self):
    return 3.14 * self.rayon ** 2
text

### Duck Typing en Action
class Canard:
def voler(self):
print("Je vole comme un canard")

text
def nager(self):
    print("Je nage")
def tester_vol(obj):
if hasattr(obj, 'voler'):
obj.voler()
else:
raise TypeError("Objet incompatible")

tester_vol(Canard()) # Fonctionne !

text

### Sous-classage de List
class ListeSuperieure(list):
def moyenne(self):
return sum(self)/len(self) if self else 0

notes = ListeSuperieure()
notes.extend()
print(notes.moyenne()) # 15.666...

text

### Mixin et Héritage Multiple
class LoggerMixin:
def log(self, message):
print(f"[LOG] {message}")

class Compteur(LoggerMixin):
def init(self):
self.total = 0

text
def ajouter(self, valeur):
    self.total += valeur
    self.log(f"Total: {self.total}")
text

---

## 📚 Ressources Recommandées

- [Documentation Python : Classes Abstraites (abc)](https://docs.python.org/fr/3/library/abc.html)
- [Real Python : Héritage Multiple et Mixins](https://realpython.com/python-super/#multiple-inheritance-overview)
- [Corey Schafer : POO en Python (Playlist YouTube)](https://www.youtube.com/playlist?list=PL-osiE80TeTsqhIuOqKhwlXsIBIdSeYtc)
- [Tutoriel avancé sur les ABCs](https://www.pythontutorial.net/python-oop/python-abstract-base-class/)

---

## 🛠️ Exigences Techniques

- **Python 3.8.5** sur Ubuntu 20.04 LTS
- **Éditeurs autorisés** : vi, vim, emacs
- **Style** : Conformité à pycodestyle (2.7.*)
- **Fichiers** :
  - Exécutables avec shebang `#!/usr/bin/python3`
  - Nouvelle ligne en fin de fichier
  - README.md obligatoire à la racine
- **Documentation** :
  - Docstrings explicites pour modules/classes/méthodes (format Google)
  - Vérification via :
    ```
    python3 -c 'print(__import__("my_module").MyClass.__doc__)'
    ```

---

**Auteur** : Javier Valenzani  
**Niveau** : Amateur  
**Poids** : 1

---

Maîtrisez ces concepts pour créer des systèmes modulaires où le comportement prime sur le type ! 🦆🧩