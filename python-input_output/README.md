# 📝 File Writer – Écriture de texte en Python

Bienvenue dans ce projet Python simple mais essentiel. Vous allez apprendre à manipuler les fichiers en Python, à comprendre comment écrire du texte dans un fichier en UTF-8, et à structurer votre code de manière claire, modulaire et professionnelle.

---

## 🎯 Objectifs pédagogiques

À la fin de ce projet, vous serez capable de :

- Écrire du texte dans un fichier en Python
- Utiliser le mode d’ouverture `"w"` (write) avec encodage UTF-8
- Gérer les fichiers avec une structure de type `with` (context manager)
- Retourner une valeur à partir d’une fonction
- Comprendre la portée des arguments dans une fonction
- Créer un module Python réutilisable
- Structurer un projet Python propre pour GitHub
- Écrire un test unitaire simple pour une fonction

---

## 📝 Bonnes pratiques et style

- **Indentation** : 4 espaces par niveau (conforme à la PEP8)
- **Commentaires** : Expliquez ce que fait chaque fonction et ligne importante
- **Shebang** : En haut de vos scripts exécutables : `#!/usr/bin/python3`
- **Encodage** : Toujours utiliser `encoding="utf-8"` pour gérer les caractères spéciaux
- **Tests** : Organisez vos tests dans un dossier `tests/` avec `pytest`
- **Fichiers** :
  - Nom de fichier explicite
  - Fichier se terminant par une ligne vide
  - Scripts exécutables si nécessaire (chmod +x)

---

## 🚀 Exemples d’utilisation

### ✅ Fonction principale

```python
from file_writer.writer import write_file

nb = write_file("example.txt", "Ceci est un test.\n")
print(f"{nb} caractères ont été écrits.")
📁 Structure du projet
bash
Copier
Modifier
file-writer/
│
├── file_writer/
│   └── writer.py           # Fonction write_file()
│
├── tests/
│   └── test_writer.py      # Tests unitaires avec pytest
│
├── README.md               # Ce fichier
├── requirements.txt        # Dépendances (facultatif ici)
└── setup.py                # Pour en faire un module installable (optionnel)
📚 Ressources utiles
Documentation officielle - open() en Python

PEP8 – Guide de style Python

Pycodestyle – Linting Python

pytest – Outil de test Python

🛠️ Exigences techniques
Éditeurs autorisés : vi, vim, emacs, VSCode, etc.

Python : Version 3.8 ou supérieure

Tests : pytest recommandé pour les tests

Style : Conforme à pycodestyle (2.7.* ou plus)

Structure : Projet modulaire, exécutable, lisible

✍ Auteur
Auteur : Guillaume
Niveau : Débutant à intermédiaire
Poids : 1

Maîtrisez les bases de la manipulation de fichiers et créez des fonctions réutilisables dans un projet Python bien organisé !

✅ file_writer/writer.py
python
Copier
Modifier
#!/usr/bin/python3
"""
Module file_writer.writer

Contient une fonction qui écrit du texte dans un fichier (UTF-8)
et retourne le nombre de caractères écrits.
"""

def write_file(filename="", text=""):
    """
    Écrit une chaîne dans un fichier texte (UTF-8) et retourne
    le nombre de caractères écrits.

    :param filename: Nom du fichier à écrire
    :param text: Texte à écrire dans le fichier
    :return: Nombre de caractères écrits
    """
    with open(filename, "w", encoding="utf-8") as file:
        return file.write(text)
✅ tests/test_writer.py
python
Copier
Modifier
import os
from file_writer.writer import write_file

def test_write_file_creates_file_and_writes_text():
    filename = "test_output.txt"
    text = "Hello, world!"

    nb_written = write_file(filename, text)

    assert nb_written == len(text)
    assert os.path.exists(filename)

    with open(filename, "r", encoding="utf-8") as f:
        content = f.read()
        assert content == text

    os.remove(filename)  # Nettoyage du test
💡 Utilise pytest pour exécuter ce test :

bash
Copier
Modifier
pytest tests/
✅ setup.py (optionnel mais prêt pour packaging)
python
Copier
Modifier
from setuptools import setup, find_packages

setup(
    name="file-writer",
    version="0.1.0",
    description="Une fonction simple pour écrire dans un fichier texte en UTF-8",
    author="Guillaume",
    packages=find_packages(),
    python_requires=">=3.6",
)
✅ requirements.txt
Ce projet n’a pas de dépendance externe, mais si tu veux pouvoir exécuter les tests :

shell
Copier
Modifier
pytest>=6.0.0