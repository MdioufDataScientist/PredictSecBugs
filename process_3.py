import os
import pandas as pd

def merge_all_csvs(root_dir, output_file_path):
    all_dfs = []
    header_saved = False

    # Parcourir tous les sous-répertoires pour trouver les fichiers merged_output.csv
    for subdir, _, files in os.walk(root_dir):
        for file in files:
            if file == 'merged_before_process.csv':
                file_path = os.path.join(subdir, file)
                df = pd.read_csv(file_path)
                all_dfs.append(df)
    
    # Vérifiez s'il y a des DataFrames à fusionner
    if all_dfs:
        merged_df = pd.concat(all_dfs, ignore_index=True)

        # Sauvegarder le fichier CSV fusionné avec une seule en-tête
        merged_df.to_csv(output_file_path, index=False)
        print(f"merged_output.csv files have been merged and saved to {output_file_path}.")
    else:
        print("No merged_output.csv files found to merge.")

# Spécifiez le répertoire racine ici et le fichier de sortie
root_directory = 'C:\\Users\\Utilisateur\\Desktop\\fichier_paquage\\PyPI'
output_file = 'C:\\Users\\Utilisateur\\Desktop\\fichier_paquage\\bbbefore_commit_par_system\\PyPI_merged_output.csv'
merge_all_csvs(root_directory, output_file)
