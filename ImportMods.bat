@echo off
setlocal enabledelayedexpansion

:: Select the target folder for "DLLs" using folder picker
echo Please select the target folder for "DLLs"...
for /f "delims=" %%i in ('cscript //nologo folder_picker.vbs') do set dlls_target_folder=%%i
echo Selected target folder for "DLLs": %dlls_target_folder%

:: Get the current script directory and set the "LevelsAvatarsAndEverythingElse" and "DLLs" folders
set script_directory=%~dp0
set levelsavatars_folder=%script_directory%Incoming\LevelsAvatarsAndEverythingElse
set dlls_folder=%script_directory%Incoming\DLLs

:: Set the target directory for LevelsAvatarsAndEverythingElse
set levelsavatars_target=C:\Users\%username%\AppData\LocalLow\Stress Level Zero\BONELAB\Mods

:: Move contents from "LevelsAvatarsAndEverythingElse" to the target directory
echo Moving contents from "LevelsAvatarsAndEverythingElse" to %levelsavatars_target%
xcopy /E /I /Y "%levelsavatars_folder%" "%levelsavatars_target%"

:: Move contents from "DLLs" to the selected folder
echo Moving contents from "DLLs" to %dlls_target_folder%
xcopy /E /I /Y "%dlls_folder%" "%dlls_target_folder%"

echo Operation completed.
pause
