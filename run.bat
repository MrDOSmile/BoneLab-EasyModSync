@echo off
echo Checking Python 3.10 installation...

set "python_exe=C:\Python310\python.exe"

if not exist "%python_exe%" (
    echo Python 3.10 is not found. Installing Python 3.10 to the default directory on the C: drive...
    powershell -Command "Invoke-WebRequest -Uri 'https://www.python.org/ftp/python/3.10.0/python-3.10.0-amd64.exe' -OutFile '%TEMP%\python-3.10.0-amd64.exe'"
    %TEMP%\python-3.10.0-amd64.exe /quiet InstallAllUsers=1 PrependPath=1 TargetDir="C:\Python310"
    echo Python 3.10 installed.
) else (
    for /f "delims=" %%v in ('"%python_exe%" --version') do set "py_version=%%v"
    echo %py_version% found at %python_exe%
    if not %py_version:~0,8% == Python 3. (
        echo Please manually install Python 3.10 to the default directory on the C: drive.
        pause
        exit
    )
)

echo Installing required packages...
"%python_exe%" -m pip install --upgrade pip
"%python_exe%" -m pip install requests

echo Running the Python script...
"%python_exe%" mod_downloader.py

pause
