@echo off
REM Cleanup Script for Cloudflare DNS Manager
REM Removes temporary files and cache

echo.
echo ========================================
echo   Cloudflare DNS Manager - Cleanup
echo ========================================
echo.

echo Cleaning up temporary files...

REM Remove Python cache files
for /d /r . %%d in (__pycache__) do @if exist "%%d" rd /s /q "%%d"
echo ✅ Removed __pycache__ directories

REM Remove .pyc files
del /s /q "*.pyc" >nul 2>&1
echo ✅ Removed .pyc files

REM Remove log files (optional)
if exist "*.log" (
    del /q "*.log"
    echo ✅ Removed log files
)

REM Remove temporary export files (optional)
if exist "dns_records_*.txt" (
    del /q "dns_records_*.txt"
    echo ✅ Removed old export files
)

echo.
echo ✅ Cleanup completed successfully!
echo.
pause
