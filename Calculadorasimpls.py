import tkinter as tk
from tkinter import *

teclado = ["0","1","2","3","4","5","6","7","8","9","+","-","*","/"]
ops = []# Se uma operação for a primeira coisa, o usuario deve começar dnv
numeros = ""
buffer = [] 
calculo = "{}{}{} = {}"
n1=""
n2=""

#Eventos
def eventos(event):# Usando o bind para identificar um evento
    global largura
    global altura
  
    if (event.type) == '22':#O evento <Configure> tem número 22.
        largura = janela.winfo_width()
        altura = janela.winfo_height()

    elif (event.type) == '7':#O evento <Enter> tem número 7.
        event.widget.config(bg="#666666",fg="black")
    elif (event.type) == '8':#O evento <Leave> tem número 8.
        event.widget.config(bg="SystemButtonFace")


#Funções para cálculo
def limpar():
    global n1
    global n2
    buffer.clear()
    ops.clear()
    n1 = ''
    n2 = ''
    entrada.config(text = "Insira um valor novamente.")

def verificacao():
    global buffer
    global n1
    global n2
    global indexDaOp
    global ops
    for x in range(indexDaOp):#Á esquerda da operação
        n1 += buffer[x]
    for y in range(indexDaOp+1,len(buffer)):
        n2 += buffer[y]
    match ops[0]:
        case '*':
           entrada.config(text = calculo.format(n1,ops[0],n2,int(n1)*int(n2)))
        case '/':
            entrada.config(text = calculo.format(n1,ops[0],n2,int(n1)/int(n2)))
        case '+':
            entrada.config(text = calculo.format(n1,ops[0],n2,int(n1)+int(n2)))
        case '-':
            entrada.config(text = calculo.format(n1,ops[0],n2,int(n1)-int(n2)))
    
def clicou (bot):
    global buffer
    global n1
    global n2
    global ops
    global indexDaOp
    buffer.append(bot)
    entrada.config(text=''.join(buffer))
    #Armazenando a operação(e se for inserida mais de uma?)
    ops = [x for x in buffer if x == "/" or x == "*" or x == "+" or x == "-" or x =="="]
    # Uma operação não pode ser a primeira coisa a ser digitada.
    if buffer[0] == "/" or buffer[0] == "*" or buffer[0] == "+" or buffer[0] == "-" or buffer[0] == "=":
        entrada.config(text="Inicialmente, insira um número")
        buffer.clear() # Limpa o buffer
        ops.clear()
    # Separando os números da operação
    if len(ops)>=1: 
        indexDaOp =  buffer.index(ops[0])

#Configurando janela
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
    botao = Button(janela, text=x,width=5,height=3,command=lambda bot=x: clicou(bot))
    botao.place(x = cordx,y = cordy)
    cordx += 60
    if cordx == 300:
        cordx=0
        cordy+=95
    botao.bind("<Enter>",eventos)
    botao.bind("<Leave>",eventos)


#Botao limpar
botao_limpar = Button(janela, text="Limpar", width=29, height=3,command=limpar)
botao_limpar.place(x=0, y=375)
botao_limpar.bind("<Enter>",eventos) # O especificador bind_class conflitou com algo no código
botao_limpar.bind("<Leave>",eventos)

#Botão de resultado
botao_resultado = Button(janela, text="=",width=5,height=3,command = verificacao)
botao_resultado.place(x=240,y=280)
botao_resultado.bind("<Enter>",eventos) # O especificador bind_class conflitou com algo no código
botao_resultado.bind("<Leave>",eventos)

janela.bind("<Configure>",eventos)

janela.mainloop()

