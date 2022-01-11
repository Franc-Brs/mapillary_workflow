Indicazioni per Windows, per SO diversi sarà necessario modificare qualche comando e qualche riga dello script Python
# GoProFusion

Creare collegamento nella cartella di lavoro per facilità (crea collegamento e cercati FUsionStudio_x64.exe o simile)
fonti utili https://github.com/anafaggiano/Mapillary
Per una singola immagine immagine, da linea di comando (cmd)
```
.\FusionStudio_x64.exe.lnk --back C:\path\in\windowsBAck\GB010005.JPG --front C:\path\in\windowsFront\GF010005.JPG --output C:\path\in\windowsOutput\image.jpg -p 0 --pc 0 -videoCodec 4
```

# Python

Per il virtual env https://uoa-eresearch.github.io/eresearch-cookbook/recipe/2014/11/26/python-virtual-env/
una volta creato attivalo dalla cartella cogni
```
source mapillary/Scripts/activate
```

# Mapillary

scarica https://github.com/mapillary/mapillary_tools/releases/tag/v0.8.0
e gioca https://github.com/mapillary/mapillary_tools#quickstart

Da cmd
```
C:\path\to\exe>mapillary_tools_win.exe process_and_upload .\output --user_name "FrancescoBrs1"
```

# Mantenere i processi in Windows

Dovendo lavorare in rdp su un desktop remoto, facevo andare lo script di notte.
Da Powershell aperta come admin
```
query user
```
Usare tscon dalla cartella sustem32 e mettere nome sessione al posto di tscon etc etc
 ```
 C:\WINDOWS\system32> .\tscon.exe rdp-tcp#11 /dest:console
 ```
# Indicazioni di massima

Lo script sostanziamente unisce le foto FRONT e BACk fatte da una macchina GoProFusion 360. E' facilmente modificabile e comprensibile, le foto frontali devono essere, pur se in sottocartelle diverse, in cartelle chiamate FRNT, quelle posteriori in cartelle chiamate BACK. Per fare un esempo

```
folderStrade
|____ Strada1
     |_______dataXXYYZZZZFRNT
     |_______dataXXYYZZZZBACK
     |_______dataXXYYZZZZFRNT_2
     |_______dataXXYYZZZZBACK_2
|____ Strada2
     |_______dataXXYYZZZZFRNT
     |_______dataXXYYZZZZBACK
     |_______dataXXYYZZZZFRNT_2
     |_______dataXXYYZZZZBACK_2

     ....

```

Per far girare lo script è necesario installare i requirements.txt, in questo caso ho fatto un ambiente virtuale, la cartella che contiene lo script sarà simile a quanto segue

```
folder
|     workflow.py
|     info.py
|     requirements.txt
|     workflow.log
|     mapillary_tools_win.exe
|     FusionStudio_x64.exe

     ....

```
info.py contiene il percorso in cui lo script andrà a cercare i file (le foto in folderStrade) da stichare con il programma di GoPro.
Ho aggiunto anche l'eseguibile di Mapillary, si può automatizzare tramite linea di comando (e tramite script) l'upload delle foto sulla piattaforma.
