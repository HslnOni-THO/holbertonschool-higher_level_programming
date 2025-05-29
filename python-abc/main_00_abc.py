#!/usr/bin/env python3
from task_00_abc import Animal, Dog, Cat

bobby = Dog()
garfield = Cat()

print(bobby.sound())     # Affiche "Bark"
print(garfield.sound())  # Affiche "Meow"

# Cette ligne doit provoquer une erreur car Animal est abstraite
animal = Animal()
print(animal.sound())
