import subprocess
import os
import shutil
import concurrent.futures

def run_command(command, cwd=None):
    try:
        result = subprocess.run(command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, cwd=cwd)
        print(result.stdout)
        return result.stdout
    except subprocess.CalledProcessError as e:
        print(f"Command '{e.cmd}' returned with error (code {e.returncode}): {e.stderr}")
        return None

def add_source_files_to_project(project_path, source_files_path):
    file_paths = []
    for root, dirs, files in os.walk(source_files_path):
        for file in files:
            file_path = os.path.join(root, file)
            file_paths.append(file_path)
    
    if file_paths:
        # Construct a single command to add all files
        command = ['und', 'add'] + file_paths + [project_path]
        run_command(command)

def calculate_metrics(understand_path, project_path, output_file):
    os.chdir(understand_path)

    # Setting metrics
    run_command(['und', 'settings', '-metrics', 'all', project_path])

    # Analyze the project
    print('Analyzing the project')
    run_command(['und', 'analyze', project_path])

    # Extract metrics and save to CSV
    metrics_output = run_command(['und', 'metrics', project_path])
    if metrics_output:
        with open(output_file, 'w') as file:
            file.write(metrics_output)
        print(f"Metrics extracted to {output_file}")

def delete_project_directory(project_dir):
    try:
        shutil.rmtree(project_dir)
        print(f'Understand project deleted: {project_dir}')
    except OSError as e:
        print(f'Error deleting Understand project: {e}')

def process_directory(understand_path, base_dir, sub_dir):
    try:
        commit_dir = os.path.join(base_dir, sub_dir, 'before_commit')
        project_path = os.path.join(base_dir, sub_dir, 'before_project.und')
        output_file = os.path.join(base_dir, sub_dir, 'before_commit_metrics.csv')

        # Create the Understand project
        print(f'Creating project for {sub_dir}')
        run_command(['und', 'create', '-languages', 'all', project_path])

        # Add source files to the project
        print(f'Adding files to project for {sub_dir}')
        add_source_files_to_project(project_path, commit_dir)

        # Calculate metrics
        print(f'Calculating metrics for {sub_dir}')
        calculate_metrics(understand_path, project_path, output_file)

    except Exception as e:
        print(f"Error processing directory {sub_dir}: {e}")

    finally:
        # Delete the Understand project directory
        print(f'Deleting project for {sub_dir}')
        delete_project_directory(project_path)

def main():
    understand_path = 'C:\\Program Files\\SciTools\\bin\\pc-win64'  # Replace with the path to Understand
    base_dir = 'C:\\Users\\Utilisateur\\Desktop\\fichier_paquage\\Maven'

    sub_dirs = [d for d in os.listdir(base_dir) if os.path.isdir(os.path.join(base_dir, d))]

    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
        futures = [executor.submit(process_directory, understand_path, base_dir, sub_dir) for sub_dir in sub_dirs]
        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print(f"Error in thread: {e}")

if __name__ == "__main__":
    main()
