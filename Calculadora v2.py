# !/usr/bin/python
# -*- coding: UTF-8 -*-
#Calculadora simples com GUI em Tkinter.


import math
from tkinter import *
import sys

class Calculadora:

    def __init__(self, master):

        # --------------------------------------TKINTER INTERFACE------------------------------------------------#
        self.frame1 = Frame(master, bg='sky blue')
        self.frame1.configure(relief=GROOVE)
        self.frame1.place(relheight=1, relwidth=1)

        # --------------------------Titulo--------------------------#
        # -- Texto 1 --#
        Label(self.frame1, text='CADASTRO', font=('Ariel', '15'), bg='sky blue').place(relx=0.29, rely=0.01)


        # -------------------------- Valor 1 --------------------------#
        # -- Texto 1 --#
        Label(self.frame1, text='Valor 1', font=('Ariel', '15'), bg='sky blue').place(relx=0.10, rely=0.12)

        # -- Entrada de valor 1 --#
        self.valor1 = Entry(self.frame1, font=('Ariel', '20'))
        self.valor1.place(relx=0.10, rely=0.20, relwidth=0.30)

        # -------------------------- Valor 2 --------------------------#
        # -- Texto 2 --#
        Label(self.frame1, text='Valor 2', font=('Ariel', '15'), bg='sky blue').place(relx=0.55, rely=0.12)
        # -- Entrada de valor 2 --#
        self.valor2 = Entry(self.frame1, font=('Ariel', '20'))
        self.valor2.place(relx=0.55, rely=0.20, relwidth=0.30)

        # -------------------------- Botão Somar --------------------------#
        # Botão somar
        self.somar = Button(self.frame1, text=' + ', font=('Ariel', '20'), fg='green', command=self.somar)
        self.somar.place(relx=0.10, rely=0.30, relheight=0.10, relwidth=0.15)



    def somar(self):
        valor1 = self.valor1.get()
        valor2 = self.valor2.get()
        valor1 = float(valor1)
        valor2 = float(valor2)
        c = valor1 + valor2
        c = float(c)
        self.msg['text'] = '%f' % (c)
    def subtrair(self):
        valor1 = self.valor1.get()
        valor2 = self.valor2.get()
        valor1 = float(valor1)
        valor2 = float(valor2)
        c = valor1 - valor2
        c = float(c)
        self.msg['text'] = '%f' % (c)

    def multiplicar(self):
        valor1 = self.valor1.get()
        valor2 = self.valor2.get()
        valor1 = float(valor1)
        valor2 = float(valor2)
        c = valor1 * valor2
        c = float(c)
        self.msg['text'] = '%f' % (c)

    def dividir(self):
        valor1 = self.valor1.get()
        valor2 = self.valor2.get()
        valor1 = float(valor1)
        valor2 = float(valor2)
        c = valor1 / valor2
        c = float(c)
        self.msg['text'] = '%f' % (c)

    def sqrt(self):
        try:
            valor1 = self.valor1.get()
            valor1 = float(valor1)
            c = math.sqrt(valor1)
            c = float(c)
            self.msg['text'] = '%f' % (c)
        except:
            valor2 = self.valor2.get()
            valor2 = float(valor2)
            c = math.sqrt(valor2)
            c = float(c)
            self.msg['text'] = '%f' % (c)

    def limpar(self):
        pass

    def sair(self):
        app.destroy()

app = Tk()
app.title("Calculadora")
app.geometry("300x500")
Calculadora(app)
app.mainloop()