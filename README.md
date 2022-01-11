# GoProFusion

creare collegamento nella cartella di lavoro per facilità (>crea collegamento e cercati FUsionStudio_x64.exe o simile)
fonti utili https://github.com/anafaggiano/Mapillary
Per una immagine
```
.\FusionStudio_x64.exe.lnk --back C:\path\in\windowsBAck\GB010005.JPG --front C:\path\in\windowsFront\GF010005.JPG --output C:\path\in\windowsOutput\image.jpg -p 0 --pc 0 -videoCodec 4
```

# Python

per il virtual env https://uoa-eresearch.github.io/eresearch-cookbook/recipe/2014/11/26/python-virtual-env/
una volta creato attivalo se vuoi dalla cartella cogni
source mapillary/Scripts/activate

# Mapillary

scarica https://github.com/mapillary/mapillary_tools/releases/tag/v0.8.0
e gioca https://github.com/mapillary/mapillary_tools#quickstart

from cmd
```
C:\path\to\exe>mapillary_tools_win.exe process_and_upload .\output --user_name "FrancescoBrs1"
```

# Mantenere i processi in win

usare da powershell
```
query user
```
usare tscon dalla cartella sustem32 e mettere nome sessione al posto di tscon etc etc
 ```
 C:\WINDOWS\system32> .\tscon.exe rdp-tcp#11 /dest:console
 ```
