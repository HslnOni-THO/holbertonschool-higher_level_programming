Python - Import & Modules
Bienvenue dans ce projet dédié à l’utilisation des modules et de l’import en Python. Vous apprendrez ici à organiser votre code, à réutiliser des fonctions, à utiliser les arguments en ligne de commande, et à respecter les bonnes pratiques de style Python.

🎯 Objectifs pédagogiques
À la fin de ce projet, vous serez capable d’expliquer et d’appliquer :

Pourquoi la programmation Python est puissante et flexible

Comment importer des fonctions ou modules depuis un autre fichier (import, from ... import ...)

Comment utiliser les fonctions importées dans vos scripts

Comment créer un module Python (fichier .py avec fonctions/routines)

Comment utiliser la fonction intégrée dir() pour explorer le contenu d’un module

Comment empêcher l’exécution de code lors de l’import d’un script (if __name__ == "__main__":)

Comment utiliser les arguments de la ligne de commande avec sys.argv ou argparse

📝 Bonnes pratiques et style
Placez vos instructions import en début de fichier.

Utilisez pycodestyle pour vérifier la conformité de votre code.

Tous vos scripts doivent commencer par #!/usr/bin/python3, être exécutables, et se terminer par une nouvelle ligne.

🚀 Exemples d’utilisation
Importer un module entier :

python
import example
example.add(4, 5)  # Utilisation de la fonction add du module example
Importer une fonction spécifique :

python
from example import add
add(4, 5)  # Utilisation directe de la fonction add
Importer plusieurs fonctions :

python
from example import add, sub
Importer tout (à éviter en production) :

python
from example import *
Lister le contenu d’un module :

python
import example
print(dir(example))
Protéger le point d’entrée d’un script :

python
if __name__ == "__main__":
    # Ce code ne s’exécute pas lors d’un import
    main()
Arguments en ligne de commande :

python
import sys
print(sys.argv)  # Affiche la liste des arguments passés au script
📚 Ressources utiles
[Modules - Python Docs]

[Command line arguments]

[Pycodestyle – Guide de style Python Code]

🛠️ Exigences techniques
Éditeurs autorisés : vi, vim, emacs

Python : Version 3.10.* sur Ubuntu 22.04 LTS

Style : Respect de pycodestyle (2.7.*)

Fichiers : Exécutables, nouvelle ligne en fin de fichier, shebang obligatoire, README.md à la racine du projet

Auteur : Guillaume
Niveau : Novice
Poids : 1

Organisez, réutilisez et rendez votre code plus puissant grâce aux modules Python !