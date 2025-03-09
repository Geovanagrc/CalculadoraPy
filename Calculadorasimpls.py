import tkinter as tk
from tkinter import *

teclado = ["0","1","2","3","4","5","6","7","8","9","+","-","*","/","="]

def limpar():
    return print("Em desenvolvimento")
    
def clicou (bot):
    if bot in teclado:
        entrada.config(text = bot)

janela = tk.Tk()
janela.geometry("300x450")
janela.title("Calculadora simples")
janela.resizable(0,0)
janela.iconbitmap("Calculadora.ico")

barra = LabelFrame(janela, text = "Calculadora") 
barra.place(x=0, y =0 )
barra.config (height=60,width=300)

entrada = Label(janela,text="Insira um número")
entrada.place(x = 0, y = 23)

#Teclado numerico
cordx = 0
cordy = 90
for x in teclado:
    botao = Button(janela, text=x,width=5,height=3, command=lambda x=x: clicou(x))
    botao.place(x = cordx,y = cordy)
    cordx += 60
    if cordx == 300:
        cordx=0
        cordy+=95

#Botao limpar
botao_limpar = Button(janela, text="Limpar", width=30, height=3,command=limpar)
botao_limpar.place(x=0, y=375)

janela.mainloop()