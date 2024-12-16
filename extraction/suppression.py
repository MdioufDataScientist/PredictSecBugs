import os

def delete_specific_files(directory, filenames):
    """
    Parcours le répertoire donné et supprime les fichiers spécifiés dans tous les sous-répertoires.

    Args:
    directory (str): Le chemin du répertoire à parcourir.
    filenames (list): Une liste des noms de fichiers à supprimer.
    """
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file in filenames:
                file_path = os.path.join(root, file)
                try:
                    os.remove(file_path)
                    print(f"File {file_path} has been deleted successfully.")
                except Exception as e:
                    print(f"Failed to delete {file_path}. Reason: {e}")

# Chemin du répertoire de base
directory_path = 'C:\\Users\\Utilisateur\\Desktop\\fichier_paquage\\GHSA'

# Noms des fichiers à supprimer
files_to_delete = ['merged_after_process.csv', 'merged_before_process.csv']

# Appel de la fonction
delete_specific_files(directory_path, files_to_delete)
