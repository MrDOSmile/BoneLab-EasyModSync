import os
import shutil
import zipfile
import requests
import pathlib
from tkinter import Tk
from tkinter.filedialog import askopenfilename, askdirectory

mandatory_mods = [
    "https://thunderstore.io/package/download/Lakatrazz/Fusion/1.3.2/",
    "https://thunderstore.io/package/download/gnonme/BoneLib/2.2.1/",
]

def download_file(url, save_path):
    response = requests.get(url, stream=True)
    content_disposition = response.headers.get('Content-Disposition')

    if content_disposition:
        file_name = content_disposition.split('filename=')[-1].strip('"')
    else:
        file_name = url.split('/')[-2] + '.zip'

    save_path = os.path.join(os.path.dirname(save_path), file_name)
    total_size = int(response.headers.get('content-length', 0))

    with open(save_path, 'wb') as f:
        for chunk in response.iter_content(chunk_size=8192):
            f.write(chunk)
            bytes_downloaded = f.tell()
            percentage = int(100 * bytes_downloaded / total_size)
            print(f"Downloading {url}: {percentage}%", end='\r')

    return save_path



def extract_zip(zip_path, extract_path):
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        for member in zip_ref.infolist():
            if not member.is_dir():
                print(f"Extracting {member.filename}...")
                try:
                    zip_ref.extract(member, extract_path)
                    print(f"Successfully extracted {member.filename}")
                except Exception as e:
                    print(f"Failed to extract {member.filename}: {e}")



def extract_and_move_files(extract_path, dll_destination, appdata_destination):
    for root, dirs, files in os.walk(extract_path):
        for file in files:
            file_path = os.path.join(root, file)

            # Move files from Mods folder to the specified folder
            if "Mods" in root:
                destination_path = os.path.join(dll_destination, file)
                print(f"Moving {file_path} to {destination_path}")
                shutil.move(file_path, destination_path)

            # Move files from Plugins folder to the specified folder
            if "Plugins" in root:
                plugins_path = os.path.join(os.path.dirname(dll_destination), "Plugins")
                destination_path = os.path.join(plugins_path, file)
                print(f"Moving {file_path} to {destination_path}")
                shutil.move(file_path, destination_path)

        # Move other contents to AppData LocalLow directory
        for directory in dirs:
            if directory not in ["Mods", "Plugins"]:
                source_path = os.path.join(root, directory)
                destination_path = os.path.join(appdata_destination, directory)
                print(f"Moving {source_path} to {destination_path}")
                shutil.move(source_path, destination_path)



def get_saved_dll_folder(file_path):
    if os.path.exists(file_path):
        with open(file_path, 'r') as f:
            return f.read().strip()
    return None

def save_dll_folder(file_path, folder_path):
    with open(file_path, 'w') as f:
        f.write(folder_path)

def clear_directory(directory):
    for item in os.listdir(directory):
        item_path = os.path.join(directory, item)
        if os.path.isfile(item_path):
            os.remove(item_path)
        else:
            shutil.rmtree(item_path)

def main():
    Tk().withdraw()
    profile_file = askopenfilename(title="Select Profile Text File")

    script_dir = os.path.dirname(os.path.realpath(__file__))
    config_file = os.path.join(script_dir, 'config.txt')
    dll_folder = get_saved_dll_folder(config_file)
    if not dll_folder:
        dll_folder = askdirectory(title="Select Folder for DLL Files")
        save_dll_folder(config_file, dll_folder)

    with open(profile_file, 'r') as file:
        download_links = file.read().splitlines()

    profile_dir = os.path.dirname(profile_file)

    download_links = list(set(download_links + mandatory_mods))

    clear_directory(dll_folder)
    app_data_folder = os.path.join(os.getenv('APPDATA'), '..\\LocalLow\\Stress Level Zero\\BONELAB\\Mods')
    clear_directory(app_data_folder)

    for link in download_links:
        file_name = link.split('/')[-1]
        save_path = os.path.join(profile_dir, file_name)
        save_path = download_file(link, save_path)

        file_name = os.path.basename(save_path)
        extract_folder = os.path.join(profile_dir, os.path.splitext(file_name)[0])
        extract_zip(save_path, extract_folder)

        extract_and_move_files(extract_folder, dll_folder, app_data_folder)

        os.makedirs(app_data_folder, exist_ok=True)

        for item in os.listdir(extract_folder):
            item_path = os.path.join(extract_folder, item)
            destination = os.path.join(app_data_folder, item)
            if os.path.isfile(item_path):
                shutil.move(item_path, destination)
            else:
                if os.path.exists(destination):
                    shutil.rmtree(destination)
                shutil.move(item_path, destination)

        os.remove(save_path)
        shutil.rmtree(extract_folder)

if __name__ == "__main__":
    main()
