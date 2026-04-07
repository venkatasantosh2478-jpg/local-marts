@echo off
REM Amazon Clone - Automatic Setup & Run
REM This script will check, install, and run everything automatically

pushd %~dp0

echo.
echo ============================================
echo   AMAZON CLONE - AUTOMATIC SETUP
echo ============================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python is not installed!
    echo.
    echo Please download and install Python from:
    echo https://www.python.org
    echo.
    echo IMPORTANT: Check "Add Python to PATH" during installation!
    echo.
    pause
    exit /b 1
)

echo [1/3] Checking dependencies...
pip show flask >nul 2>&1
if errorlevel 1 (
    echo Installing required packages...
    pip install -r requirements.txt
    if errorlevel 1 (
        echo ERROR: Failed to install packages!
        pause
        exit /b 1
    )
)
echo OK - All dependencies installed
echo.

echo [2/3] Checking database...
if not exist "app\amazon_clone.db" (
    echo Creating database with sample data...
    python seed.py
    if errorlevel 1 (
        echo WARNING: Could not auto-seed database
        echo Please run manually: python seed.py
    )
) else (
    echo OK - Database exists
)
echo.

echo [3/3] Starting Flask server...
echo.
echo ============================================
echo   Server running at:
echo   http://localhost:5000
echo ============================================
echo.
echo Login with:
echo   Admin: admin / admin123
echo   User: testuser / test123
echo.
echo Press Ctrl+C to stop the server
echo ============================================
echo.

python start.py

popd
pause
