# **README**

---
**SWAPPING PROFILES RE-DOWNLOADS ALL MODS IN THE PROFILE EVERY TIME.**
**ALL CURRENT MODS WILL BE DELETED AND REPLACED WITH THE NEWLY DOWNLOADED MODS.**
---
**SWAPPING PROFILES RE-DOWNLOADS ALL MODS IN THE PROFILE EVERY TIME.**
**ALL CURRENT MODS WILL BE DELETED AND REPLACED WITH THE NEWLY DOWNLOADED MODS.**
---
**SWAPPING PROFILES RE-DOWNLOADS ALL MODS IN THE PROFILE EVERY TIME.**
**ALL CURRENT MODS WILL BE DELETED AND REPLACED WITH THE NEWLY DOWNLOADED MODS.**
---
**-YOU HAVE BEEN WARNED-**
---
─────────────────────────────────────────────────

    IMPORTANT NOTE
        
    As of now, there is no official support for mod packs or a mod manager to
    synchronize mods for BONE LABS. This program is my attempt to provide a
    user-friendly solution that does not involve redistributing mods, but
    instead utilizes direct download links from the official mod sources.

    My intention is to enhance the gaming experience for everyone and ensure a
    consistent and enjoyable multiplayer experience in BONE LABS using the Fusion
    mod. I hope you find this tool helpful and enjoyable to use.

    Please understand that my intentions are genuine, and I only wish to bring
    more fun and cohesion to the BONE LABS community. Your understanding is
    appreciated!

─────────────────────────────────────────────────

Quick Start Guide
---
Download the entire repository as a ZIP file and extract it to a location on your computer.

Create a new text file and name it <PROFILE_NAME_HERE>.txt inside the Profiles folder. Add the direct download links for the mods you want to download, one per line to the text file.
Double-click on run.bat to start the program. If you don't have Python 3.10 installed, the script will prompt you to install it, and it will download the installer for you.

When prompted, select the profile text file you created in step 2. (There can be multiple)

If it's your first time running the program, you'll be prompted to select a folder for the DLL files. This should typically be the Mods folder in your game directory (e.g., C:\Program Files (x86)\Steam\steamapps\common\BONE LABS\Mods).

The program will download the mods, extract the contents, and move the files to the appropriate locations.

That's it! You can create additional profiles by adding more text files to the Profiles folder with different sets of mod download links.

─────────────────────────────────────────────────

**Detailed README**
---
Introduction
---
This program is designed to simplify the process of downloading and installing mods for the game BONE LABS. You can create multiple profiles with different sets of mods and switch between them easily.

---
Requirements
---

Python 3.10: The program is written in Python and requires version 3.10. If you don't have it installed, the run.bat script will prompt you to install it, and it will download the installer for you.
The requests module: This module is necessary for downloading files. The run.bat script will attempt to install it automatically. If it fails, you may need to install Python 3.10 and the requests module manually.

---
Setup
---

Download the entire repository as a ZIP file and extract it to a location on your computer.
Create a new text file named mod_urls.txt inside the Profiles folder. Add the direct download links for the mods you want to download, one per line.

---
Usage
---

Double-click on run.bat to start the program.
When prompted, select the profile text file you created in the setup.
If it's your first time running the program, you'll be prompted to select a folder for the DLL files. This should typically be the Mods folder in your game directory (e.g., C:\Program Files (x86)\Steam\steamapps\common\BONE LABS\Mods).
The program will download the mods, extract the contents, and move the files to the appropriate locations.

---
Creating Additional Profiles
---

You can create additional profiles by adding more text files to the Profiles folder with different sets of mod download links. To switch between profiles, simply select the desired profile text file when prompted during program execution.

---
Troubleshooting
---

If you encounter any issues, make sure you have the correct mod download links in your profile text file.
Ensure that your game directory and Mods folder are correctly set up.
Check your internet connection if you're having issues downloading the mods.

---
Additional Notes
---

The program will always download and install the Fusion and BoneLib mods, regardless of whether they're in the <PROFILE>.txt file.
Every time you switch profiles, the Mods folder and the AppData LocalLow directory will be completely replaced with the new profile's mods to ensure only the active profile's mods are present.

Please remember that the program requires Python 3.10 to be installed. If you encounter issues during the pip installation process, make sure Python 3.10 is correctly installed on your system. The run.bat script will download the installer for you if it detects Python 3.10 is not installed, but you will need to install it manually before running the script again.
