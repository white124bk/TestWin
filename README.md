# KivyMD - PyInstaller - One exe
**Помогите решить проблему**  

python -m pip install --upgrade pip, setuptools, wheel, pyinstaller  
pip install https://github.com/kivy/kivy/archive/master.zip  
pip install https://github.com/kivymd/KivyMD/archive/master.zip  
pip install cython  

Далее команда: python -m PyInstaller --name test scr\main.py  
В папке dist\test\test.exe файл запускается без проблем

После чего ввел команду: python -m PyInstaller win.spec  
В папке dist\test.exe файл  запускается но выдает ошибку:  
RecursionError: maximum recursion depth exceeded while calling a Python object  
полный лог ошибки в файле error.txt

Я так понимаю проблема в win.spec?  

Возможно нашел решение этой проблемы:  
python -m pip uninstall pyinstaller  
python -m pip install -U pyinstaller==5.6.2  
python -m pip install pyinstaller-hooks-contrib==2022.14