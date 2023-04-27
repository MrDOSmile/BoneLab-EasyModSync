DOSmile's EasyModSync README for BoneLab
======================================

This set of scripts is designed to help you easily import and export mods for BoneLab, especially for players using the Fusion mod, which allows multiplayer gameplay but does not sync mods between players. It consists of two scripts, ImportMods.bat and ExportMods.bat, which handle the import and export processes, respectively.

Folder Structure:
-----------------
- Incoming
  - DLLs
  - LevelsAvatarsAndEverythingElse
- Outgoing
  - DLLs
  - LevelsAvatarsAndEverythingElse
- ImportMods.bat
- ExportMods.bat
- folder_picker.vbs

Instructions:
--------------

1. Download Mod Pack:
   - Download the entire mod pack from a source like Google Drive or GitHub.
   - The downloaded folder should have the same structure as the "Incoming" folder:
     * DLLs
     * LevelsAvatarsAndEverythingElse

2. Import Mods:
   - Merge the downloaded mod pack folder with the existing "Incoming" folder in the DOSmilesEasyModSync directory.
   - Ensure the mod files are placed into the appropriate folders inside the "Incoming" directory:
     * DLL files go into the "Incoming\DLLs" folder.
     * Levels, avatars, and other assets go into the "Incoming\LevelsAvatarsAndEverythingElse" folder.
   - Run ImportMods.bat by double-clicking it.
   - A folder picker window will open. Navigate to and select the "Mods" folder located in your BoneLab game installation directory.
   - The script will copy the contents of the "Incoming" folders to their respective destinations in your BoneLab game installation.

3. Export Mods:
   - Run ExportMods.bat by double-clicking it.
   - A folder picker window will open. Navigate to and select the "Mods" folder located in your BoneLab game installation directory.
   - The script will copy the contents from the outbound directories back to the "Outgoing" folder, maintaining the same structure as the "Incoming" folder.
   - Note that this step does not actually export the mods. It merely consolidates them in the "Outgoing" folder. To share your mod(s) list with others, you will need to upload the contents of the "Outgoing" folder to a platform like Google Drive or GitHub, and provide a download link.

Please ensure that you have the correct folder structure and that the mods are placed in the appropriate subfolders before running the scripts.
