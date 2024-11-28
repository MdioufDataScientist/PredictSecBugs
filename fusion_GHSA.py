import pandas as pd
import glob

def merge_csv_files(input_folder, output_file):
    # Récupérer la liste des fichiers CSV dans le dossier
    csv_files = glob.glob(f"{input_folder}/*.csv")
    
    # Lire le premier fichier pour obtenir l'en-tête
    merged_df = pd.read_csv(csv_files[0])
    
    # Lire les autres fichiers sans l'en-tête et les concaténer
    for file in csv_files[1:]:
        df = pd.read_csv(file)
        merged_df = pd.concat([merged_df, df], ignore_index=True)
    
    # Enregistrer le fichier fusionné
    merged_df.to_csv(output_file, index=False)

# Exemple d'utilisation
input_folder = 'C:\\Users\\Utilisateur\\Desktop\\fichier_paquage\\before'
output_file = 'C:\\Users\\Utilisateur\\Desktop\\fichier_paquage\\before\\fichier_fusionne.csv'
merge_csv_files(input_folder, output_file)
