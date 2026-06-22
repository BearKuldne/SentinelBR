import tkinter as tk
from tkinter import Tk, simpledialog



class password:
     def verificar_senha(self):
        janela = tk.Tk()
        janela.withdraw()

        senha_digitada = simpledialog.askstring("Autorização", 
        "Digite a senha para modificar essa pasta: ", show="*")

        senha_correta = "123456"
        
        if senha_digitada == senha_correta:
            simpledialog.messagebox.showinfo("Autorização",
            "Senha correta! Ação permitida. ")
            janela.destroy()
            return True
            
        else:
            simpledialog.messagebox.showerror("Autorização",
            "Senha incorreta! Ação não permitida. ")
            janela.destroy()
            return False


