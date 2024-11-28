import os
import pandas as pd

def arrange_columns_in_csv(file_path, output_file, desired_order):
    # Lire le fichier CSV
    df = pd.read_csv(file_path)
    
    # Réorganiser les colonnes selon l'ordre désiré
    # Si certaines colonnes ne sont pas présentes, elles seront ignorées
    df = df[[col for col in desired_order if col in df.columns]]
    
    # Sauvegarder le fichier avec les colonnes réorganisées
    df.to_csv(output_file, index=False)
    print(f"Fichier arrangé et sauvegardé dans: {output_file}")

# Exemple d'utilisation
file_path = 'C:\\Users\\Utilisateur\\Desktop\\fichier_paquage\\before\\before_language_par_langage\\dataset_finale.csv'
output_file = 'C:\\Users\\Utilisateur\\Desktop\\fichier_paquage\\before\\before_language_par_langage\\before_arranger.csv'
desired_order = ['Name', 'file', 'Kind', 'buggy', 'commit_date', 'commit_sha', 'extension', 'AvgLineCode', 
                 'CountDeclClass', 'RatioCommentToCode', 'CountStmtExe', 'AvgCyclomaticStrict', 'CountLine',
                 'SumCyclomatic', 'AvgCyclomatic', 'SumEssential', 'MaxCyclomatic', 'AvgLineComment',
                 'AvgCyclomaticModified', 'AvgEssential', 'SumCyclomaticModified', 'CountLineComment', 
                 'CountLineCode', 'MaxCyclomaticModified', 'CountLineBlank', 'CountStmtDecl', 'AvgLine', 
                 'MaxEssential', 'CountDeclFunction', 'MaxNesting', 'AvgLineBlank', 'SumCyclomaticStrict', 
                 'CountStmt', 'file_path']

arrange_columns_in_csv(file_path, output_file, desired_order)
