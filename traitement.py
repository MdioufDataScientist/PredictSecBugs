import os
import shutil

def group_and_move_directories(path):
    # Vérifie si le chemin est valide
    if not os.path.exists(path):
        print(f"Le chemin {path} n'existe pas.")
        return

    # Liste tous les dossiers dans le répertoire spécifié
    directories = [d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d))]

    # Trie les dossiers par ordre alphabétique (optionnel)
    directories.sort()

    # Groupe et déplace les dossiers par paquets de 100
    for i in range(0, len(directories), 100):
        group = directories[i:i+100]
        group_number = i // 100 + 1
        group_folder = os.path.join(path, str(group_number))

        # Crée le dossier de groupe s'il n'existe pas déjà
        if not os.path.exists(group_folder):
            os.makedirs(group_folder)

        # Déplace les dossiers dans le dossier de groupe
        for directory in group:
            shutil.move(os.path.join(path, directory), os.path.join(group_folder, directory))

        print(f"Groupe {group_number} créé et les dossiers ont été déplacés dans {group_folder}")

# Exemple 
path_to_directory = 'C:\\Users\\Utilisateur\\Documents\\data_memoire\\fichier_paquage\\PyPI'
group_and_move_directories(path_to_directory)
