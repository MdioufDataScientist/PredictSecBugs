import os
import pandas as pd

def merge_files(directory):
    """
    Parcours le répertoire donné et fusionne les fichiers before_commit.csv et before_project.csv
    dans tous les sous-répertoires.

    Args:
    directory (str): Le chemin du répertoire à parcourir.
    """
    for root, dirs, files in os.walk(directory):
        if 'after_commit.csv' in files and 'after_project.csv' in files:
            before_commit_path = os.path.join(root, 'after_commit.csv')
            before_project_path = os.path.join(root, 'after_project.csv')
            
            try:
                # Lecture des fichiers CSV
                before_commit_df = pd.read_csv(before_commit_path)
                before_project_df = pd.read_csv(before_project_path)
                
                # Fusion des fichiers
                merged_df = pd.merge(before_commit_df, before_project_df, left_on='file', right_on='Name')
                
                # Sauvegarde du fichier fusionné
                merged_output_path = os.path.join(root, 'merged_after_commit_project.csv')
                merged_df.to_csv(merged_output_path, index=False)
                
                print(f"Files {before_commit_path} and {before_project_path} have been merged successfully into {merged_output_path}.")
            except Exception as e:
                print(f"Failed to merge files in {root}. Reason: {e}")

# Chemin du répertoire de base

directories = [
    'C:\\Users\\Utilisateur\\Desktop\\fichier_paquage\\PyPI',
    'C:\\Users\\Utilisateur\\Desktop\\fichier_paquage\\Packagist',
    'C:\\Users\\Utilisateur\\Desktop\\fichier_paquage\\OSS-Fuzz',
    'C:\\Users\\Utilisateur\\Desktop\\fichier_paquage\\NuGet',
    'C:\\Users\\Utilisateur\\Desktop\\fichier_paquage\\npm',
    'C:\\Users\\Utilisateur\\Desktop\\fichier_paquage\\Maven',
    'C:\\Users\\Utilisateur\\Desktop\\fichier_paquage\\GHSA',
]
#directory_path = 'C:\\Users\\Utilisateur\\Documents\\test_1'

# Fusion des fichiers before_commit.csv et before_project.csv
for directory_path in directories:
    merge_files(directory_path)
