@echo off
Rem Després es pot instal·lar fàcilment tot per fer la prova en un moment creant l'entorn virtual
py -m venv .
Rem Changing to Scripts directory & executing envinroment
CALL .\Scripts\activate.bat
Rem executa la comanda
py -m pip install -r requirements.txt

