# -*- coding: utf-8 -*-
"""
Created on Wed Jun 15 18:08:57 2022

@author: ankit computer
"""

from tkinter import *
from PIL import ImageTk,Image
root=Tk()
root.title("Dice game")
root.geometry("600x600")
root.configure(background="yellow")
pikachu=ImageTk.PhotoImage(Image.open("pikachu.jpg"))
abra=ImageTk.PhotoImage(Image.open("abra.jpg"))
Iyvasour=ImageTk.PhotoImage(Image.open("Iyvasour.jpg"))
bulbasour=ImageTk.PhotoImage(Image.open("bulbasour.jpg"))
button=ImageTk.PhotoImage(Image.open("button.jpg"))
charmender=ImageTk.PhotoImage(Image.open("charmendar.jpg"))
jigglypuff=ImageTk.PhotoImage(Image.open("jigglypuff.jpg"))
kadabra=ImageTk.PhotoImage(Image.open("kadabra.jpg"))
meowth=ImageTk.PhotoImage(Image.open("meowth.jpg"))
nidoking=ImageTk.PhotoImage(Image.open("nidoking.jpg"))
paras=ImageTk.PhotoImage(Image.open("paras.jpg"))
ratata=ImageTk.PhotoImage(Image.open("ratata.jpg"))
squirtle=ImageTk.PhotoImage(Image.open("squirtle.jpg"))
persian=ImageTk.PhotoImage(Image.open("persian.jpg"))

player1=Label(root,text="Player 1",bg = "royal blue",fg="white")
player1.place(relx=0.1,rely=0.3,anchor=CENTER)
player2=Label(root,text="Player 2",bg = "royal blue",fg="white")
player2.place(relx=0.9,rely=0.3,anchor=CENTER)
player1_score=Label(root,bg = "royal blue",fg="white")
player1_score.place(relx=0.1,rely=0.4,anchor=CENTER)
player2_score=Label(root,bg = "royal blue",fg="white")
player2_score.place(relx=0.9,rely=0.4,anchor=CENTER)
pikachu = Label(root,bg="choclate1",fg="white")
pikachu.place(relx=0.5,rely=0.5,anchor=CENTER)
root.mainloop()