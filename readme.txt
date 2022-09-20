---------------------
Inici Projecte ESTEPA
---------------------

- Crear carpeta de projecte
H:\Python\Projecte Jorge\v1

- Anar a la carpeta i crear entorn virtual
python -m venv .
o
py -m venv .

- Activar entorn virtual
cd Scripts
activate.bat

- Desactivar entorn virtual
cd Scripts
deactivate.bat

- Assegurar-se de tenir instal·lat el Python 3.9 i actualitzat el pip
python.exe -m pip install --upgrade pip

- Instal·lar el PySide6 i totes les llibreries que es necessitin per el projecte
pip install PySide6

- Copiar el PyDracula del github (ho deixem a la carpeta H:\Python\Projecte Jorge\PyDracula) a la carpeta arrel (H:\Python\Projecte Jorge\v1)
https://github.com/Wanderson-Magalhaes/Modern_GUI_PyDracula_PySide6_or_PyQt6

- Executar el programa i comprovar el funcionament
python main.py


- Compilar resources y main
pyside6-rcc resources.qrc -o resources_rc.py
pyside6-rcc resources_wafer.qrc -o resources_wafer_rc.py
pyside6-rcc resources_plot.qrc -o resources_plot_rc.py
+
pyside6-uic main.ui> ui_main.py

- Hacer el build
python setup.py build

- Install from requeriments
py -m pip install -r requirements.txt

- Get requeriments file
pip3 freeze > requirements.txt

- Using environments
https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/
