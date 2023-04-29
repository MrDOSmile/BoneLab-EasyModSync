@echo off

:try_pip_install
echo Attempting to install the required pip packages...
python -m pip install --upgrade pip >nul 2>&1 && (
    echo Successfully upgraded pip.
) || (
    goto pip_install_failed
)

python -m pip install requests >nul 2>&1 && (
    echo Successfully installed requests.
) || (
    goto pip_install_failed
)

echo Running the mod_downloader.py script...
python .\mod_downloader.py

echo Finished.
pause
exit /b 0

:pip_install_failed
echo Python 3.10 is not installed or there is a problem with your Python installation.
echo Downloading Python 3.10 installer for you...
powershell -Command "(New-Object Net.WebClient).DownloadFile('https://www.python.org/ftp/python/3.10.0/python-3.10.0-amd64.exe', 'python-3.10.0-amd64.exe')"
echo The Python 3.10 installer has been downloaded as python-3.10.0-amd64.exe.
echo Please install Python 3.10 and try running the script again.
pause
exit /b 1
