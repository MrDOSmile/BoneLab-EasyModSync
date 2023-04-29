@echo off

where python 2>nul || (
    echo Python 3.10 is not installed. Downloading and installing...
    powershell -Command "(New-Object Net.WebClient).DownloadFile('https://www.python.org/ftp/python/3.10.0/python-3.10.0-amd64.exe', 'python-3.10.0-amd64.exe')"
    .\python-3.10.0-amd64.exe /quiet InstallAllUsers=1 PrependPath=1 Include_test=0
    echo Installation complete.
)

echo Installing requests module if not installed...
python -m pip install --upgrade pip
python -m pip install requests

echo Running the mod_downloader.py script...
python .\mod_downloader.py

echo Finished.
pause
