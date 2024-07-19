@echo off
python -m pip show python-docx >nul 2>&1
if %errorlevel% neq 0 (
    echo Installing python-docx...
    python -m pip install python-docx
)

python GUI.py
pause
