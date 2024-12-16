import os
import pandas as pd

def process_csvs(commit_file_path, project_file_path, output_file_path):
    try:
        # Vérifiez si les fichiers existent
        if not os.path.isfile(commit_file_path):
            print(f"File {commit_file_path} does not exist.")
            return
        if not os.path.isfile(project_file_path):
            print(f"File {project_file_path} does not exist.")
            return

        # Lire les fichiers CSV
        df_commit = pd.read_csv(commit_file_path)
        df_project = pd.read_csv(project_file_path)

        # Fusionner les DataFrames sur les colonnes 'file' et 'Name'
        df_merged = pd.merge(df_commit, df_project, left_on='file', right_on='Name', suffixes=('_commit', '_project'))

        # Sauvegarder le fichier CSV fusionné
        df_merged.to_csv(output_file_path, index=False)
        print(f"File {output_file_path} has been processed and saved.")
    except PermissionError as e:
        print(f"PermissionError: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

def traverse_and_process(root_dir):
    # Parcourir tous les sous-répertoires
    for subdir, _, files in os.walk(root_dir):
        commit_file = None
        project_file = None

        for file in files:
            if file == 'after_commit.csv':
                commit_file = os.path.join(subdir, file)
            elif file == 'after_project.csv':
                project_file = os.path.join(subdir, file)

        if commit_file and project_file:
            output_file_path = os.path.join(subdir, 'merged_before_process.csv')
            process_csvs(commit_file, project_file, output_file_path)


root_directory = 'C:\\Users\\Utilisateur\\Desktop\\fichier_paquage\\GHSA'
traverse_and_process(root_directory)
