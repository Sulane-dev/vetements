from PIL import Image
import os
from concurrent.futures import ThreadPoolExecutor

# Récupérer le dossier du script
folder = os.path.dirname(os.path.realpath(__file__))

# Liste tous les fichiers PNG dans le dossier
png_files = [file_name for file_name in os.listdir(folder) if file_name.endswith('.png')]

# Fonction pour convertir une image PNG en WebP et supprimer le fichier PNG
def convert_to_webp(file_name, folder):
    file_path = os.path.join(folder, file_name)
    
    # Charger l'image PNG
    with Image.open(file_path) as img:
        # Enregistrer l'image en format WebP avec compression (quality de 75)
        webp_path = os.path.splitext(file_path)[0] + '.webp'
        img.save(webp_path, 'WEBP', quality=75)
        print(f'{file_name} converted to {webp_path}')
    
    # Supprimer le fichier PNG après conversion
    os.remove(file_path)
    print(f'{file_name} has been deleted after conversion.')

# Utiliser ThreadPoolExecutor pour exécuter les conversions en parallèle
def convert_images_in_parallel(png_files, folder):
    with ThreadPoolExecutor() as executor:
        # Exécute la fonction de conversion pour chaque fichier PNG
        for index, file_name in enumerate(png_files, start=1):
            executor.submit(convert_to_webp, file_name, folder)
            
        print("Conversion des fichiers lancée...")

# Démarrer la conversion en parallèle
convert_images_in_parallel(png_files, folder)
