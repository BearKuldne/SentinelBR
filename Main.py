from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import socket
import getpass
import time
import os


class Monitoramento(FileSystemEventHandler):

    def on_modified(self, event):
        if event.is_directory:
            return
        else:
            print('\nArquivo modificado')
            print('Informacoes de quem modificou:')
            print(f'Usuario: {usuario}')
            print(f'Maquina: {maquina}')
            print(f'IP Local: {ip_local}')
            print(f'Caminho do arquivo modificado: {event.src_path}')
    def on_created(self, event):
        if event.is_directory:
            print('\nPasta criada')
            print('Informacoes de quem criou:')
            print(f'Usuario: {usuario}')
            print(f'Maquina: {maquina}')
            print(f'IP Local: {ip_local}')
            print(f'Caminho da pasta criada: {event.src_path}')
        else:
            print('\nArquivo criado')
            print('Informacoes de quem criou:')
            print(f'Usuario: {usuario}')
            print(f'Maquina: {maquina}')
            print(f'IP Local: {ip_local}')
            print(f'Caminho do arquivo criado: {event.src_path}')
    def on_deleted(self, event):
        if event.is_directory:
            print('\nPasta deletada')
            print('Informacoes de quem deletou:')
            print(f'Usuario: {usuario}')
            print(f'Maquina: {maquina}')
            print(f'IP Local: {ip_local}')
            print(f'Caminho da pasta deletada: {event.src_path}')
        else:
            print('\nArquivo deletado')
            print('Informacoes de quem deletou:')
            print(f'Usuario: {usuario}')
            print(f'Maquina: {maquina}')
            print(f'IP Local: {ip_local}')
            print(f'Caminho do arquivo deletado: {event.src_path}')
     

# Caminho da pasta Downloads
downloads = r"C:\Users\Windows 10\Downloads"

# Caminho da pasta que será protegida
caminho = os.path.join(downloads, "Confidencial")

# Se a pasta não existir, cria automaticamente
if not os.path.exists(caminho):
    os.makedirs(caminho)


observador = Observer()
evento = Monitoramento()



observador.schedule(evento, caminho, recursive=True)
observador.start()
usuario = getpass.getuser()
maquina = socket.gethostname()
ip_local = socket.gethostbyname(maquina)

print(f'Monitorando a pasta: {caminho}')

while True:
    time.sleep(1)