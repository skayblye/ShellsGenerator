# Shell Generator

Esta herramienta te permite generar shells utilizando Python. 

![Funcionamiento](https://raw.githubusercontent.com/skayblye/ShellsGenerator/main/img/Blue-2023-04-07-18-53-51.png)
![Funcionamiento](https://raw.githubusercontent.com/skayblye/ShellsGenerator/main/img/Blue-2023-04-07-18-54-13.png)

## Requerimientos

- Python 3.x
- colorama

## Opciones

- `-i`: dirección IP
- `-p`: puerto
- `--type`: tipo de shell a generar (`bash`, `sh`, `cmd`, `powershell`)
- `-r`: agregar la ruta completa de la shell (solo para `bash` y `sh`)
- `-d`: codificar la shell en base64

## Ejemplos

### Ejemplo 1: Generar shells de Bash sin ruta completa
	
    python3 hackshell.py -i 192.168.1.100 -p 4444 --type bash
    
### Ejemplo 2: Generar shells de PowerShell

    python3 hackshell.py -i 192.168.1.100 -p 4444 --type powershell

### Ejemplo 3: Generar shells de Sh con ruta completa

    python3 hackshell.py -i 192.168.1.100 -p 4444 --type sh -r
    
### Ejemplo 4: Generar shells de Bash con ruta completa y codificadas en base64

    python3 hackshell.py -i 192.168.1.100 -p 4444 --type bash -r -d

