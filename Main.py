from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import os


class Monitoramento(FileSystemEventHandler):

    def on_modified(self, event):
        print(f'Arquivo modificado: {event.src_path}')
    def on_created(self, event):
        print(f'Arquivo criado: {event.src_path}')
    def on_deleted(self, event):
        print(f'Arquivo deletado: {event.src_path}')


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

print(f'Monitorando a pasta: {caminho}')

while True:
    pass