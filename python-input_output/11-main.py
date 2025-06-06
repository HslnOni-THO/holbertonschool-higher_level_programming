#!/usr/bin/python3
import os
import sys

Student = __import__('11-student').Student
read_file = __import__('0-read_file').read_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

# Récupère le chemin passé en argument
path = sys.argv[1]

# Supprime le fichier s’il existe déjà
if os.path.exists(path):
    os.remove(path)

# Création de l'étudiant original
student_1 = Student("John", "Doe", 23)
j_student_1 = student_1.to_json()

print("Initial student:")
print(student_1)
print(type(student_1))
print(type(j_student_1))
print("{} {} {}".format(student_1.first_name, student_1.last_name, student_1.age))

# Sauvegarde dans un fichier JSON
save_to_json_file(j_student_1, path)

# Lecture brute du fichier pour affichage
read_file(path)
print("\nSaved to disk")

# Création d'un faux étudiant
print("Fake student:")
new_student_1 = Student("Fake", "Fake", 89)
print(new_student_1)
print(type(new_student_1))
print("{} {} {}".format(new_student_1.first_name, new_student_1.last_name, new_student_1.age))

# Chargement du dictionnaire JSON depuis le fichier
print("Load dictionary from file:")
new_j_student_1 = load_from_json_file(path)

# Mise à jour du faux étudiant avec les vraies données
new_student_1.reload_from_json(new_j_student_1)
print(new_student_1)
print(type(new_student_1))
print("{} {} {}".format(new_student_1.first_name, new_student_1.last_name, new_student_1.age))
