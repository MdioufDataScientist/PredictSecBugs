import os

def shorten_directory_names(base_dir):
    # Liste tous les répertoires dans le répertoire de base
    dirs = [d for d in os.listdir(base_dir) if os.path.isdir(os.path.join(base_dir, d))]
    
    # Crée un dossier pour stocker les noms originaux si ce n'est pas déjà fait
    original_names_file = os.path.join(base_dir, 'original_names.txt')
    with open(original_names_file, 'w') as file:
        for i, dir_name in enumerate(dirs):
            # Détermine le nouveau nom
            new_name = f'dir_{i+1}'
            
            # Renomme le répertoire
            old_path = os.path.join(base_dir, dir_name)
            new_path = os.path.join(base_dir, new_name)
            os.rename(old_path, new_path)
            
            # Écrit les anciens et nouveaux noms dans le fichier
            file.write(f'{dir_name} -> {new_name}\n')
            print(f'Renamed: {dir_name} to {new_name}')

def main():
    base_dir = 'C:\\Users\\Utilisateur\\Documents\\data_memoire\\fichier_paquage\\1' 
    shorten_directory_names(base_dir)

if __name__ == "__main__":
    main()
