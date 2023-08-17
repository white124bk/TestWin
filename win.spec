# python -m PyInstaller --name test scr\main.py
# python -m PyInstaller win.spec

# python -m pip install --upgrade pip, setuptools, wheel, pyinstaller
# pip install https://github.com/kivy/kivy/archive/master.zip
# pip install https://github.com/kivymd/KivyMD/archive/master.zip
# pip install cython

from kivy_deps import sdl2, glew
import sys

app_name = 'test'
sys.path += ["scr\\"]

block_cipher = None
a = Analysis(['scr\\main.py'],
  pathex=['C:\\Coding\\Py\\Kivy\\TestWin'],
  binaries=None,
  datas=None,
  hiddenimports=[
  'fsspec',
  ],
  hookspath=[],
  runtime_hooks=[],
  excludes=[],
  win_no_prefer_redirects=False,
  win_private_assemblies=False,
  cipher=block_cipher)

# exclusion list
from os.path import join
from fnmatch import fnmatch
exclusion_patterns = (
  join("kivy_install", "data", "images", "testpattern.png"),
  join("kivy_install", "data", "images", "image-loading.gif"),
  join("kivy_install", "data", "keyboards*"),
  join("kivy_install", "data", "settings_kivy.json"),
  join("kivy_install", "data", "logo*"),
  join("kivy_install", "data", "fonts", "DejaVuSans*"),
  join("kivy_install", "modules*"),
  join("Include*"),
  join("sdl2-config"),
)

def can_exclude(fn):
    for pat in exclusion_patterns:
        if fnmatch(fn, pat):
            return True

a.datas = [x for x in a.datas if not can_exclude(x[0])]
a.binaries = [x for x in a.binaries if not can_exclude(x[0])]
# Filter app directory
appfolder = [x for x in Tree('scr\\', excludes=['*.py','*.pyc']) if not can_exclude(x[0])]

pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)

exe = EXE(pyz,
  a.scripts,
  appfolder,
  a.binaries,
  a.zipfiles,
  a.datas,
  *[Tree(p) for p in (sdl2.dep_bins + glew.dep_bins )],
  name=app_name,
  debug=False,
  strip=False,
  upx=True,
  console=False,
  icon='scr\\gis.ico'
  )