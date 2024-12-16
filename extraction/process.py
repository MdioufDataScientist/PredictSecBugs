import os
import pandas as pd

import pandas as pd
import os

def process_csv(file_path, kind_values=['File', 'Module File']):
    try:
        # Vérifiez si le fichier existe
        if not os.path.isfile(file_path):
            print(f"File {file_path} does not exist.")
            return

        # Lire le fichier CSV
        df = pd.read_csv(file_path)

        # Filtrer les lignes où la colonne 'Kind' contient l'un des types spécifiés
        df = df[df['Kind'].isin(kind_values)]
        df = df.dropna(axis=1, how='all')
        df.insert(2, 'buggy', 0)

        # Sauvegarder le fichier CSV traité
        df.to_csv(file_path, index=False)
        print(f"File {file_path} has been processed and saved.")
    except PermissionError as e:
        print(f"PermissionError: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")


def traverse_and_process(root_dir):
    # Parcourir tous les sous-répertoires
    for subdir, _, files in os.walk(root_dir):
        for file in files:
            if file == 'before_project.csv':
                file_path = os.path.join(subdir, file)
                process_csv(file_path)

# Spécifiez le répertoire racine ici
root_directory = 'C:\\Users\\Utilisateur\\Desktop\\fichier_paquage\\GHSA'
traverse_and_process(root_directory)

#process_csv('C:\\Users\\Utilisateur\\Documents\\b42dd4badf803bb9fb71ac34cd9cb0c249262f2c\\after_project.csv')
