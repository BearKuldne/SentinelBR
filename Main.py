from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import socket
import getpass
import time
import os
from senha import password

class Acao:
    def __init__(self, usuario, maquina, ip_local):
        self.usuario = usuario
        self.maquina = maquina
        self.ip_local = ip_local

    def mostrar_informacoes(self, caminho):
        print(f'Usuario: {self.usuario}')
        print(f'Maquina: {self.maquina}')
        print(f'IP Local: {self.ip_local}')
        print(f'Caminho: {caminho}')

usuario = getpass.getuser()
maquina = socket.gethostname()
ip_local = socket.gethostbyname(maquina)

dados = Acao(usuario, maquina, ip_local)


class Monitoramento(FileSystemEventHandler):

    def on_modified(self, event):
        if event.is_directory:
            return
        verificar = password().verificar_senha()
        if verificar == False:
            print('\nArquivo modificado')
            print('Informacoes de quem modificou:')
            dados.mostrar_informacoes(event.src_path)

    def on_created(self, event):
        if event.is_directory:
            verificar = password().verificar_senha()
            if verificar == False:
                print('\nPasta criada')
                print('Informacoes de quem criou:')
                dados.mostrar_informacoes(event.src_path)
        else:
            verificar = password().verificar_senha()
            if verificar == False:
                print('\nArquivo criado')
                print('Informacoes de quem criou:')
                dados.mostrar_informacoes(event.src_path)

    def on_deleted(self, event):
        if event.is_directory:
            verificar = password().verificar_senha()
            if verificar == False:
                print('\nPasta deletada')
                print('Informacoes de quem deletou:')
                dados.mostrar_informacoes(event.src_path)
        else:
            verificar = password().verificar_senha()
            if verificar == False:
                print('\nArquivo deletado')
                print('Informacoes de quem deletou:')
                dados.mostrar_informacoes(event.src_path)


downloads = r"C:\Users\Windows 10\Downloads"
caminho = os.path.join(downloads, "Confidencial")

if not os.path.exists(caminho):
    os.makedirs(caminho)

observador = Observer()
evento = Monitoramento()

observador.schedule(evento, caminho, recursive=True)
observador.start()

print(f'Monitorando a pasta: {caminho}')

while True:
    time.sleep(1)