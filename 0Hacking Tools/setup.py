import sys
from cx_Freeze import setup, Executable

include_files = ["autorun.inf"]
base = None

if sys.platform == "win32":
    base = "Win32GUI"

setup(name="program",
    version="2.0",
    description="A program",
    options={"build_exe": {"include_files": include_files}},
    executables=[Executable("Vict_new.py", base=base)])
