@echo off

set "python_exe=python"

where python 2>nul || (
    echo Python not found in the system's PATH. Checking the default installation path...
    set "python_exe=C:\Python310\python.exe"
)

if not exist "%python_exe%" (
    echo Python 3.10 is not installed. Downloading and installing...
    powershell -Command "(New-Object Net.WebClient).DownloadFile('https://www.python.org/ftp/python/3.10.0/python-3.10.0-amd64.exe', 'python-3.10.0-amd64.exe')"
    .\python-3.10.0-amd64.exe /quiet InstallAllUsers=1 PrependPath=1 Include_test=0
    echo Installation complete.
)

echo Installing requests module if not installed...
"%python_exe%" -m pip install --upgrade pip
"%python_exe%" -m pip install requests

echo Running the mod_downloader.py script...
"%python_exe%" .\mod_downloader.py

echo Finished.
pause
