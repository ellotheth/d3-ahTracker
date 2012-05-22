import sys
from cx_Freeze import setup, Executable

# Run python setup.py build to create the exe

# might need this too? "includes":["tkinter._fix"]
build_exe_options = {"packages":["re"]}

base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(name = "ahCalculator",
      version = "0.02",
      description = "Diablo 3 auction house calculator",
      options = {"build_exe": build_exe_options},
      executables = [Executable("ahCalculator.pyw", base=base)])

