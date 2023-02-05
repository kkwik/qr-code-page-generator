@ECHO OFF

call venv\Scripts\activate.bat

python scripts\scaffold.py links.txt

pause