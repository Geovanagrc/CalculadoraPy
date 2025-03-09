import tkinter as tk
from tkinter import *

numeros = ["0","1","2","3","4","5","6","7","8","9"]
ops = ["+","-","*","/"]

def clicou (*args):
    entrada.config(text = "1")

janela = tk.Tk()
janela.geometry("300x400")
janela.title("Calculadora simples")
janela.resizable(0,0)
janela.iconbitmap("Calculadora.ico")

barra = LabelFrame(janela, text = "Calculadora") 
barra.place(x=0, y =0 )
barra.config (height=60,width=300)

entrada = Label(janela,text="Insira um número")
entrada.place(x=0, y = 25)

botao1 = Button(janela,text="1",command = clicou)
botao1.place(x=0, y = 60)

janela.mainloop()