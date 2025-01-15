#!/usr/bin/python3

def uppercase(str):
    for c in str:
        if 'a' <= c <= 'z':  # Vérifie si c est une minuscule
            print(chr(ord(c) - 32), end='')  # Convertit en majuscule
        else:
            print(c, end='')  # Affiche les autres caractères tels quels
    print()  # Pour ajouter un saut de ligne après l'affichage
