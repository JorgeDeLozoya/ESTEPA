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

- Com idea al menú de la dreta, es podria afegir una opció per canviar el tema del programa a light mode
- Estructura dels fitxers que es guarden