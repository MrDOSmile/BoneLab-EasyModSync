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
1. Ensure BONE LABS is installed on your computer.
2. In your Steam library, right-click on BONE LABS, go to "Properties," select the "Betas" tab, and choose "public-beta" from the dropdown menu.
3. Download and install Melon Loader v0.5.7 (https://github.com/HerpDerpinstine/MelonLoader/releases/tag/v0.5.7).
4. Run BONE LABS once with Melon Loader installed to generate the necessary folders.
5. On this GitHub repository page, click the green "Code" button located near the top-right corner, then select "Download ZIP" to download the entire repository. Extract the contents to a location on your computer.
6. Create a new text file named <PROFILE_NAME_HERE>.txt inside the 'Profiles' folder. To add mods, visit the official mod page, right-click on the "Windows Download" button, and select "Copy link address." Paste the direct download links for the mods you want, one per line, into the text file.
7. Double-click on the 'run.bat' script to start the program. The script will install Python 3.10 and the 'requests' module if they're not already installed.
8. When prompted, select the profile text file you created in step 6.
9. If it's your first time running the program, you'll be prompted to select a folder for the DLL files. This should typically be the 'Mods' folder in your game directory (e.g., C:\Program Files (x86)\Steam\steamapps\common\BONE LABS\Mods).
10. The program will download the mods, extract the contents, and move the files to the appropriate locations.
11. Launch BONE LABS, and your selected mods should now be active in the game.
12. To create additional profiles, simply add more text files with different sets of mod download links to the 'Profiles' folder, and select the desired profile text file when prompted during the program's execution.

─────────────────────────────────────────────────
---
Troubleshooting
---

If you encounter any issues, make sure you have the correct mod download links in your profile text file.
Ensure that your game directory and Mods folder are correctly set up.
Check your internet connection if you're having issues downloading the mods.

---
Additional Notes
---

**The program will always download and install the Fusion and BoneLib mods, regardless of whether they're in the <PROFILE>.txt file**.
Every time you switch profiles, the Mods folder and the AppData LocalLow directory will be completely replaced with the new profile's mods to ensure only the active profile's mods are present.

Please remember that the program requires Python 3.10 to be installed. If you encounter issues during the pip installation process, make sure Python 3.10 is correctly installed on your system. The run.bat script will download the installer for you if it detects Python 3.10 is not installed, but you will need to install it manually before running the script again.
