import tkinter as tk
import tkinter.messagebox
import tkinter.messagebox as tkMessageBox
import sqlite3

principal = tk.Tk()
principal.title("Notas de Alunos")
principal.geometry("300x300")

def banco():
  global conexao, cursor
  try:
    conexao = sqlite3.connect('banco.db')
    cursor = conexao.cursor()
  except:
    print("Erro ao conectar")
  else:
    cursor.execute("CREATE TABLE IF NOT EXISTS `notas` (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, nome TEXT, bimestre1 float, bimestre2 float)")
    print("Tabela criada com sucesso!")

def cadastrar():
  banco()
  cursor.execute("INSERT INTO notas (nome, bimestre1, bimestre2) values (?, ?, ?)", (str(nome_entrada.get()), float(bimestre1_entrada.get()), float(bimestre2_entrada.get())))
  conexao.commit()
  print("Dados cadastrados com sucesso!")
    

  
nome_label = tk.Label(principal,text="Nome:")
nome_label.place(x=50,y=50)
nome_entrada = tk.Entry(principal)
nome_entrada.place(x=100,y=50)
bimestre1_label = tk.Label(principal, text="Nota 1:")
bimestre1_label.place(x=50,y=100)
bimestre1_entrada = tk.Entry(principal)
bimestre1_entrada.place(x=100,y=100)
bimestre2_label = tk.Label(principal, text="Nota 2:")
bimestre2_label.place(x=50,y=150)
bimestre2_entrada = tk.Entry(principal)
bimestre2_entrada.place(x=100,y=150)
salvar_botao = tk.Button(text="Salvar", command=cadastrar)
salvar_botao.place(x=100,y=200)
cancelar_botao = tk.Button(text="Cancelar")
cancelar_botao.place(x=200,y=200)

tk.mainloop()