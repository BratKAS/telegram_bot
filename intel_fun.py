import subprocess
import os


def kill(name='Intel'):
    subprocess.run([f"powershell", f"-Command", "Stop-Process -Name {name} -Force"], check=True)


def dtp():
    return os.path.expanduser('~\\Desktop')


def cp():
    return os.getcwd()


def show(path):
    os.startfile(path)


def make_file(text, opn=True, path=os.path.join(dtp(), 'text_file.txt')):
    with open(path, 'w') as file:
        file.write(text)
    if opn:
        show(path)


def read_file(path=os.path.join(dtp(), 'text_file.txt')):
    with open(path, 'r') as file:
        text = file.read()
    return text
