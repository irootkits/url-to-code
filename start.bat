@echo off
echo ww g j installe les dependance pour que le script marche..
pip install pillow requests >nul 2>&1
echo.
echo lancement du script..
python main.py
pause