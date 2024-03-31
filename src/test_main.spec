# -*- mode: python ; coding: utf-8 -*-

import os

# Get the directory of the current script
current_dir = os.path.dirname(os.path.abspath('test_main.spec'))

# Construct the relative paths to 'assets' and 'saves'
assets_path = os.path.join(current_dir, '..', 'src', 'assets')
saves_path = os.path.join(current_dir, '..', 'src', 'saves')

a = Analysis(
    ['test_main.py'],
    pathex=[],
    binaries=[],
    datas=[
        (assets_path, 'assets'), 
        (saves_path, 'saves')
    ],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='test_main',
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
)
coll = COLLECT(
    exe,
    a.binaries,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='test_main',
)
