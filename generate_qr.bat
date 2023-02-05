@ECHO OFF

call venv\Scripts\activate.bat

echo Clearing out qr_codes directory...
del qr_codes\* /q

echo Creating qr codes...
python scripts\generate_qr.py links.txt qr_codes

echo Scouring qr codes...
FOR /F "tokens=*" %%G IN ('dir /s /b *.svg') DO scour -i %%G -o %%~pG%%~nG.tmp --enable-viewboxing --enable-id-stripping --enable-comment-stripping --shorten-ids --indent=none 

echo Replacing origin qr codes with scoured version
FOR /F "tokens=*" %%G IN ('dir /s /b *.tmp') DO move %%G %%~pG%%~nG.svg
pause


