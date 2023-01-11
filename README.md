# ESTEPA

Update v7.6.2 (17/08/2022)

- Opció de canviar de dades per veure els seus valors corresponents a la funció analyze_files
- Afegit un botó per canviar entre tema fosc o clar (així ens estalviem els problemes per saber com guardar en el tema clar)
- Actualment no es veuen les grafiques pero perque estic canviat el measurements[parameter]["medida"] per measurements[par]["medida"] i necessito fer més canvis
- Afegides les següents configuracions al inici de la classe MainWindow:
	 
        self.modo_histograma=True
        self.measurements=None
        self.directorio_trabajo=""  #PER ACABAR 


*Queda pendent per aquesta setmana:

- Una funció que guardi la ultima ubicació on es va obrir un fitxer (en comptes de crear un directori permanent)
- Com idea al menú de la dreta, es podria afegir una opció per canviar el tema del programa a light mode


Update v7.6.3 (30/08/2022)

- Configurat el botó per canviar entre tema fosc o clar per l'analisis
- Funció per guardar la ultima ubicació on es va obrir un fitxer

- Afegides les següents configuracions al inici de la classe MainWindow:
	 

        self.directorio_trabajo="C:"
        self.modo_grafico=True  #True = Anàlisi 
				#False = Correlació

*Queda pendent per aquesta setmana:

- Estructura dels fitxers que es guarden

Update v7.6.4 (08/09/2022)

- Afegida una finestra previa per donar-li nom als fixers que es volen guardar (de moment per els valors i els resultats)
- Treball perque es mostrin els tipus de correlació a la pantalla de resultats
- Exe creat


Update v7.6.5 (16/09/2022)

- Reconfigurada la pestanya principal
- Afegits stacked widgets per facilitar la navegació en la pestanya d'anàlisi
- Inici de configuració pels directoris


Update v7.6.6 (25/10/2022)

- Afegit Heatmap.py per fer proves per fer el wafermap

Update v7.7 (4/11/2022)

- Afegida la primera versió del wafermap al analyze

Update v8 (19/11/2022)

- Canviat el layout del programa
- Nova distribució amb tabwidgets per optimitzar les grafiques
- Canviada la pagina principal amb els directoris
- Nou menú lateral dret amb els directoris


Update v8.0.1 (5/12/2022)

- Canviat el layout del programa
- Configurats els directoris
- Optimització de distribució del programa
- ComboBox per canviar entre parametres més facilment al analitzar o fer correlació


Update v8.1 (11/01/2023)

- Canvis a la pantalla de Consulta
- Inici de configuració de la BBDD
- Optimització general del programa

*He deixat parts comentades en el programa en aquesta versió*

*Idees

- Al menú de la dreta, es podria afegir una opció per canviar el tema del programa a light mode
- Nous icons
- Configurar bé com es veuen els botons al ser presionats
- Directori, pero per guardar resultats
- Treure el toggle


- Correlació, aplicar outliers als dos parametres per tenir els mateixos numeros...
- Combobox a la llista de valors que es mostren
- Stacked Widget pels valors carregats
- Directori on es guarden les coses

- Botó per fer els reports

- Per guest, només visible consult, reports i analyze**




- Afegit el ReportLab per fer els reports i guardar els analisis
- Creat el directori de treball d'usuari al toml
- Canvis en la pantalla d'anàlisi
- Solucionats els problemes amb la correlació
