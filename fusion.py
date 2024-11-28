import pandas as pd

# Liste des chemins de vos datasets
file_paths = [
    'C:\\Users\\Utilisateur\\Desktop\\fichier_paquage\\bbbefore_commit_par_system\\final_data\\updated_dataset_GHSA.csv',
    'C:\\Users\\Utilisateur\\Desktop\\fichier_paquage\\bbbefore_commit_par_system\\final_data\\updated_dataset_Maven.csv',
    'C:\\Users\\Utilisateur\\Desktop\\fichier_paquage\\bbbefore_commit_par_system\\final_data\\updated_dataset_npm.csv',
    'C:\\Users\\Utilisateur\\Desktop\\fichier_paquage\\bbbefore_commit_par_system\\final_data\\updated_dataset_NuGet.csv',
    'C:\\Users\\Utilisateur\\Desktop\\fichier_paquage\\bbbefore_commit_par_system\\final_data\\updated_dataset_OSS-Fuzz.csv',
    'C:\\Users\\Utilisateur\\Desktop\\fichier_paquage\\bbbefore_commit_par_system\\final_data\\updated_dataset_Packagist.csv',
    'C:\\Users\\Utilisateur\\Desktop\\fichier_paquage\\bbbefore_commit_par_system\\final_data\\updated_dataset_Pypi.csv'
]

# Lire le premier dataset avec les en-têtes
merged_dataframe = pd.read_csv(file_paths[0])

# Lire les autres datasets sans les en-têtes et les ajouter au dataframe fusionné
for file in file_paths[1:]:
    temp_df = pd.read_csv(file, header=None, skiprows=1)
    temp_df.columns = merged_dataframe.columns  # Assigner les colonnes du premier dataframe
    merged_dataframe = pd.concat([merged_dataframe, temp_df], ignore_index=True)

# Enregistrer le dataframe fusionné dans un fichier CSV
merged_dataframe.to_csv('C:\\Users\\Utilisateur\\Desktop\\fichier_paquage\\bbbefore_commit_par_system\\final_data\\\\all_files_before.csv', index=False)

print("Fusion terminée avec succès!")
