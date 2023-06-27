# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(
    ['callai.py'],
    pathex=[],
    binaries=[],
    datas=[],
    hiddenimports=['pyttsx3.drivers', 'pyttsx3.drivers.dummy', 'pyttsx3.drivers.espeak', 'pyttsx3.drivers.nsss', 'pyttsx3.drivers.sapi5'],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='callai',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=['callls.ico'],
)
coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='callai',
)
