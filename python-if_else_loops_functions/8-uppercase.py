#!/usr/bin/python3

def uppercase(str):
    for c in str:
        if 'a' <= c <= 'z':  # Si c est une lettre minuscule
            # Convertir le caractère minuscule en majuscule
            print(chr(ord(c) - 32), end='')
        else:
            # Si c n'est pas une minuscule, l'afficher tel quel
            print(c, end='')
    print()  # Ajouter un saut de ligne après l'affichage de toute la chaîne
