@echo off
REM Cloudflare DNS Manager - Windows Startup Script
REM This script provides an easy way to run the DNS manager on Windows

echo.
echo ========================================
echo   Cloudflare DNS Manager v2.0.0
echo   Starting Application...
echo ========================================
echo.

REM Check if Python is available
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python is not installed or not in PATH
    echo Please install Python from https://python.org
    pause
    exit /b 1
)

REM Check if required files exist
if not exist "app.py" (
    echo ERROR: app.py not found
    echo Please make sure you're in the correct directory
    pause
    exit /b 1
)

if not exist ".env" (
    echo WARNING: .env file not found
    echo Please create a .env file with your Cloudflare credentials
    echo.
    echo Example .env content:
    echo API_TOKEN=your_cloudflare_api_token_here
    echo ZONE_ID=your_zone_id_here
    echo.
    pause
)

REM Install dependencies if needed
echo Checking dependencies...
pip install -q requests python-dotenv

REM Run the application
echo.
echo Starting Cloudflare DNS Manager...
echo.
python app.py

REM Keep window open on error
if errorlevel 1 (
    echo.
    echo Application exited with an error
    pause
)
