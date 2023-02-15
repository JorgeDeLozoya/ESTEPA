from cx_Freeze import setup, Executable

setup(name='ESTEPA',
      version='1.0',
      description='Statistics for the Parametric Test',
      executables=[Executable('main.py')])
