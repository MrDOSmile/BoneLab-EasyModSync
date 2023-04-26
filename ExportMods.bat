@echo off
setlocal enabledelayedexpansion

:: Get the current script directory and set the "Incoming" and "Outgoing" folders
set script_directory=%~dp0
set outgoing_folder=%script_directory%Outgoing

:: Set the source directories for LevelsAvatarsAndEverythingElse and DLLs
set levelsavatars_source=C:\Users\%username%\AppData\LocalLow\Stress Level Zero\BONELAB\Mods

:: Clear contents of the "Outgoing" folder
echo Clearing contents of "Outgoing\DLLs" and "Outgoing\LevelsAvatarsAndEverythingElse"
del /S /Q "%outgoing_folder%\DLLs\*"
del /S /Q "%outgoing_folder%\LevelsAvatarsAndEverythingElse\*"

:: Copy contents from LevelsAvatarsAndEverythingElse source to the "Outgoing" folder
echo Copying contents from %levelsavatars_source% to "Outgoing\LevelsAvatarsAndEverythingElse"
xcopy /E /I /Y "%levelsavatars_source%" "%outgoing_folder%\LevelsAvatarsAndEverythingElse"

:: Prompt the user to select the "DLLs" source folder using folder picker
echo Please select the "DLLs" source folder...usually your install folder under BONELAB\Mods.
for /f "delims=" %%i in ('cscript //nologo folder_picker.vbs') do set dlls_source_folder=%%i
echo Selected "DLLs" source folder: %dlls_source_folder%

:: Copy contents from "DLLs" source folder to the "Outgoing" folder
echo Copying contents from "DLLs" source folder to "Outgoing\DLLs"
xcopy /E /I /Y "%dlls_source_folder%" "%outgoing_folder%\DLLs"

echo Operation completed.
pause
