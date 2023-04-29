import os
import shutil
import zipfile
import requests
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
        save_path = os.path.join(os.path.dirname(save_path), file_name)
    elif not os.path.splitext(save_path)[1]:
        save_path += '.zip'

    with open(save_path, 'wb') as f:
        for chunk in response.iter_content(chunk_size=8192):
            f.write(chunk)
    return save_path

def extract_zip(file_path, extract_path):
    with zipfile.ZipFile(file_path, 'r') as zip_ref:
        zip_ref.extractall(extract_path)

def move_files(src, dst, extension):
    for root, _, files in os.walk(src):
        for file in files:
            if file.endswith(extension):
                shutil.move(os.path.join(root, file), dst)

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

        move_files(extract_folder, dll_folder, '.dll')

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
