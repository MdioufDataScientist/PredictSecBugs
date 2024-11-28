import os
import pandas as pd

def process_csv(file_path):
    try:
        # Vérifiez si le fichier existe
        if not os.path.isfile(file_path):
            print(f"File {file_path} does not exist.")
            return

        # Lire le fichier CSV
        df = pd.read_csv(file_path)

        # Ajouter la colonne 'file' en extrayant le nom du fichier de 'file_path'
        df['file'] = df['file_path'].apply(lambda x: os.path.basename(x))

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
            if file == 'before_commit.csv':
                file_path = os.path.join(subdir, file)
                process_csv(file_path)

# Spécifiez le répertoire racine ici
root_directory = 'C:\\Users\\Utilisateur\\Desktop\\fichier_paquage\\GHSA'
traverse_and_process(root_directory)

#process_csv('C:\\Users\\Utilisateur\\Documents\\test_1\\00bc43b1672e662e5e3b8cecd79e67fc968fa246\\after_commit.csv')