#!/usr/bin/python3

def uppercase(str):
    for c in str:
        if 'a' <= c <= 'z':  # Vérifie si c est une lettre minuscule
            # Convertit la minuscule en majuscule en ajustant son code Unicode
            print(chr(ord(c) - 32), end='')
        else:
            print(c, end='')
    print()  # Ajoute un saut de ligne à la fin
