import tkinter as tk
import sqlite3

principal = tk.Tk()
principal.title("Notas de Alunos")
principal.geometry("350x450")

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
  conexao.close
  nome_entrada.delete(0,"end")
  bimestre1_entrada.delete(0,"end")
  bimestre2_entrada.delete(0,"end")

def listar_console():
  banco()
  cursor.execute("SELECT nome, bimestre1, bimestre2 FROM notas")
  alunos = cursor.fetchall()
  for i in alunos:
    print(i)
  conexao.close()

def listar_interface():
  dados_alunos = '' #variável para receber as tuplas do banco de dados
  banco()
  cursor.execute("SELECT nome, bimestre1, bimestre2 FROM notas")
  alunos = cursor.fetchall()
  for i in alunos:
    dados_alunos += str(i) + "\n" #concatenação das tuplas com uma quebra de linha
    dados_label["text"] = dados_alunos #label recebendo a variável que contém as tuplas
  conexao.close()

nome_label = tk.Label(principal,text="Nome:")
nome_label.place(x=50,y=50)
nome_entrada = tk.Entry(principal)
nome_entrada.place(x=110,y=50)
bimestre1_label = tk.Label(principal, text="Nota B1:")
bimestre1_label.place(x=50,y=100)
bimestre1_entrada = tk.Entry(principal)
bimestre1_entrada.place(x=110,y=100)
bimestre2_label = tk.Label(principal, text="Nota B2:")
bimestre2_label.place(x=50,y=150)
bimestre2_entrada = tk.Entry(principal)
bimestre2_entrada.place(x=110,y=150)
salvar_botao = tk.Button(text="Salvar", command=cadastrar)
salvar_botao.place(x=50,y=200)
cancelar_botao = tk.Button(text="Cancelar")
cancelar_botao.place(x=200,y=200)
listar_botao = tk.Button(text="Listar dados no console", command=listar_console)
listar_botao.place(x=50,y=250)
listar_botao = tk.Button(text="Listar dados na interface", command=listar_interface)
listar_botao.place(x=50,y=300)
dados_label = tk.Label(principal)
dados_label.place(x=50,y=350)


tk.mainloop()