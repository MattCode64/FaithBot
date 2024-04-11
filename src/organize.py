import os
import shutil


def main():
    print(f"Starting {main.__name__}")
    source_path = ""
    target_path = ""

    # Créez le dossier cible s'il n'existe pas
    if not os.path.exists(target_path):
        os.makedirs(target_path)

    for root, dirs, files in os.walk(source_path):
        for file in files:
            if file.endswith('.md'):
                file_path = os.path.join(root, file)
                dest_file_path = os.path.join(target_path, file)
                shutil.copy(file_path, dest_file_path)
                print(f'Copied {file} to {target_path}')

    print("Tous les fichiers Markdown ont été copiés avec succès.")


if __name__ == '__main__':
    main()
