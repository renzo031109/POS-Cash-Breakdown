from cx_Freeze import setup,Executable

includefiles = ['renlogo.ico', 'lining.gif']
includes = []
excludes = ['Tkinter']
packages = []

setup(
    name = 'Cash Breakdown',
    version = '1.3',
    description = 'A cashBreakdown',
    author = 'Renan Rivera',
    author_email = 'renzo031109@gmail.com',
    options = {'build_exe': {'excludes':excludes,'packages':packages,'include_files':includefiles}}, 
    executables = [Executable('cashculator.py',base = "Win32GUI")]
)
