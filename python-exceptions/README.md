# Python - Exceptions

Ce projet explique comment gérer les exceptions en Python pour rendre votre code plus robuste et éviter les plantages inattendus.

## Objectifs

- Comprendre la différence entre erreurs et exceptions
- Savoir quand et pourquoi utiliser les exceptions
- Apprendre à manipuler les blocs `try`, `except`, `else`, et `finally`
- Savoir lever (`raise`) et créer des exceptions personnalisées

## Résumé

En Python, une **erreur** est un problème critique qui empêche le programme de s’exécuter (ex: erreur de syntaxe). Une **exception** est un événement inattendu qui survient pendant l’exécution (ex: division par zéro) et que l’on peut intercepter pour éviter l’arrêt brutal du programme[1][5].

La gestion des exceptions se fait principalement avec le bloc `try...except` :

try:
# Code qui peut générer une exception
resultat = 10 / 0
except ZeroDivisionError:
print("Impossible de diviser par zéro !")

text

On peut aussi utiliser plusieurs types d’exceptions, ajouter un bloc `else` (exécuté si aucune exception), et un bloc `finally` (toujours exécuté, utile pour le nettoyage)[6] :

try:
f = open("data.txt")
num = int(input("Entrez un nombre : "))
value = 10 / num
except FileNotFoundError:
print("Fichier introuvable !")
except ValueError:
print("Veuillez entrer un nombre valide.")
except ZeroDivisionError:
print("Division par zéro interdite !")
else:
print("Tout s'est bien passé.")
finally:
print("Fin de la gestion des exceptions.")

text

On peut lever une exception personnalisée avec `raise` :

class MonErreur(Exception):
pass

if valeur < 0:
raise MonErreur("La valeur ne peut pas être négative")

text

## Bonnes pratiques

- Cibler les exceptions spécifiques (`except TypeError:` plutôt que `except:`)
- Garder les blocs `try` courts et précis
- Utiliser `finally` pour fermer les fichiers ou libérer des ressources
- Créer des exceptions personnalisées pour des cas métiers spécifiques[6]

## Pourquoi utiliser les exceptions ?

- Rendre le code plus sûr et lisible
- Anticiper les cas inattendus sans arrêter tout le programme
- Faciliter le débogage et la maintenance

---

*Pour plus de détails, consultez la documentation officielle Python et les ressources du projet.*
Ce résumé est prêt à être copié dans un fichier README.md sur GitHub, avec des exemples de code et des explications claires pour débutants.