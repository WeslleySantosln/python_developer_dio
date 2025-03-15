import tkinter as tk
from tkinter import messagebox
import random
import datetime
from app.auth.auth import Auth  # Classe Auth para lidar com autenticação
from app.database.database import DatabaseHandler  # Para manipulação do banco de dados
from app.core.calculations import factorial_and_cube, is_valid_triangle, max_side
from app.key_generator import generate_key


# Classe para a interface gráfica e fluxo da aplicação
class App:
    def __init__(self, root):
        self.db = DatabaseHandler()  # Conexão com o banco de dados
        self.auth = Auth()  # Objeto de autenticação
        self.root = root
        self.root.title("Gerador de Chaves")
        self.create_login_screen()

    def create_login_screen(self):

        """Tela de login do aplicativo"""
        self.clear_window()

        tk.Label(self.root, text="Usuário:").pack()
        self.username_entry = tk.Entry(self.root)
        self.username_entry.pack()

        tk.Label(self.root, text="Senha:").pack()
        self.password_entry = tk.Entry(self.root, show="*")
        self.password_entry.pack()

        tk.Button(self.root, text="Login", command=self.login).pack()
        tk.Button(self.root, text="Registrar", command=self.register).pack()

    def login(self):
        """Processa o login do usuário"""
        username = self.username_entry.get()
        password = self.password_entry.get()
        success, message, user_id = self.auth.login(username, password)
        
        if success:
            self.user_id = user_id
            self.create_main_screen()
        else:
            messagebox.showerror("Erro", message)

    def register(self):
        """Registra um novo usuário"""
        username = self.username_entry.get()
        password = self.password_entry.get()
        success, message = self.auth.register_user(username, password)
        if success:
            messagebox.showinfo("Sucesso", message)
        else:
            messagebox.showerror("Erro", message)

    def create_main_screen(self):
        """Tela principal após login"""
        self.clear_window()
        tk.Button(self.root, text="Gerar Chave", command=self.generate_key).pack()
        tk.Button(self.root, text="Ver Chaves", command=self.view_keys).pack()

    def generate_key(self):
        """Tela para gerar uma chave"""
        self.clear_window()
        tk.Label(self.root, text="Digite os três lados (1 a 57): (Os 3 lados devem ser diferentes)").pack()

        self.side1_entry = tk.Entry(self.root)
        self.side1_entry.pack()

        self.side2_entry = tk.Entry(self.root)
        self.side2_entry.pack()

        self.side3_entry = tk.Entry(self.root)
        self.side3_entry.pack()

        tk.Button(self.root, text="Gerar", command=self.process_key).pack()

    def process_key(self):

        try:
            sides = [
                int(self.side1_entry.get()),
                int(self.side2_entry.get()),
                int(self.side3_entry.get())
            ]
          
            key = generate_key(sides)

            success, message = self.db.insert_key(self.user_id, key)

            if success:
                messagebox.showinfo("Sucesso", f"Chave gerada: {key}")
                self.create_main_screen()
            else:
                messagebox.showerror("Erro", message)
        except ValueError as e:
            messagebox.showerror("Erro", "Insira valores numéricos válidos")
            


    def view_keys(self):
        """Exibe as chaves geradas pelo usuário"""
        self.clear_window()
        records = self.db.get_keys(self.user_id)
        total_value = sum([record[2] for record in records])
        for record in records:
            tk.Label(self.root, text=f"Chave: {record[0]} | Data: {record[1]} | Valor: R$ {record[2]}").pack()
        tk.Label(self.root, text=f"Valor total: R$ {total_value}").pack()
        tk.Button(self.root, text="Voltar", command=self.create_main_screen).pack()

    def clear_window(self):
        """Limpa a tela atual"""
        for widget in self.root.winfo_children():
            widget.destroy()




if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
