import random
from tkinter import *

menu_inicial = Tk()
menu_inicial.title('Dados')
menu_inicial.geometry("220x300+500+200")
menu_inicial.resizable(FALSE, FALSE)
menu_inicial.iconbitmap("biblioteca/icon.ico")


bg = PhotoImage(file="biblioteca/DSEM.png")

imagem = Label(menu_inicial, image=bg)
imagem.place(x=0, y=0, relwidth=1, relheight=1)

resulText: Label = Label(menu_inicial, text="Resultado", font=("Verdana", "10", "italic", "bold"))
frame = Frame(menu_inicial)

def dice_20():
    valores = range(1, 21)
    dadoVar = random.choices(valores, k=1)
    resulText['text'] = dadoVar
    bg['file'] = 'biblioteca/D20.png'


botaoD20 = Button(frame, text="D20", command=dice_20)


def dice_12():
    valores = range(1, 13)
    dadoVar = random.choices(valores, k=1)
    resulText['text'] = dadoVar
    bg['file'] = 'biblioteca/D12.png'


botaoD12 = Button(frame, text="D12", command=dice_12)


def dice_d6():
    valores = range(1, 7)
    dadoVar = random.choices(valores, k=1)
    resulText['text'] = dadoVar
    bg['file'] = 'biblioteca/D6.png'


botaoD6 = Button(frame, text="D6", command=dice_d6)

texto = Label(text='Versão 1.0')

frame.pack()
botaoD20.pack(side=RIGHT, padx=5, pady=5)
botaoD12.pack(side=RIGHT, padx=5, pady=5)
botaoD6.pack(side=RIGHT, padx=5, pady=5)
resulText.pack(side=TOP, pady=105)
texto.pack(side=LEFT)


menu_inicial.mainloop()
