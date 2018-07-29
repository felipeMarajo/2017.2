import sys
from cx_Freeze import setup, Executable
import Interface

base = None
if sys.platform == "win32":
    base = "Win32GUI"

executables = [Executable("Main.py", base=base)]

buildOptions = dict(
    packages = ["Qt5"],
    includes = ["PyQt5", "Interface"],
    include_files = ["Interface"],
    excludes = []
)


setup(
    name = "Calculadora AHP",
    options = dict(buid_exe = buildOptions),
    version = "1.0",
    description = 'Programa para disciplina de Engenharia de Software',
    executables = executables
)