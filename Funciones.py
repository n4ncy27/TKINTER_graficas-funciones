from tkinter import *
from tkinter import messagebox
import numpy as np
import matplotlib.pyplot as plt
from numpy import pi,sin,cos,tan
import tkinter as tk
import random

N=100
def salir():
    messagebox.showinfo("Suma 1.0", "La app se cerrará..")
    ventana_principal.destroy()


#Funcion lineal
def calcularlineal(m,b,x):
  return int(m.get())*x+int(b.get())
def mostrar_lineal():
  y= calcularlineal(m,b,x)
  plt.plot(x,y,color="b")
  plt.xlabel("x")
  plt.ylabel("y")
  plt.title("Funcion lineal: y=mx+b")
  plt.grid()
  plt.axhline(y=0,color="b")
  plt.axvline(x=0, color="b")
  plt.show() 
def funcion_lineal():
  
  
  # etiqueta para m
  lb_x = Label(frame_operaciones, text = "m =  ")
  lb_x.config(bg="pink", fg="black", font=("Verdana", 14, "bold"))
  lb_x.place(x=10, y=20, width=115, height=30)
  # entry para m
  entry_x = Entry(frame_operaciones, textvariable=m)
  entry_x.config(font=("Verdana", 14, "bold"), justify=LEFT, fg="blue")
  entry_x.focus_set()
  entry_x.place(x=135,y=20,width=115, height=30)
  # etiqueta para b
  lb_x = Label(frame_operaciones, text = "b =  ")
  lb_x.config(bg="pink", fg="black", font=("Verdana", 14, "bold"))
  lb_x.place(x=10, y=60, width=115, height=30)
  # entry para b
  entry_x = Entry(frame_operaciones, textvariable=b)
  entry_x.config(font=("Verdana", 14, "bold"), justify=LEFT, fg="blue")
  entry_x.focus_set()
  entry_x.place(x=135,y=60,width=115, height=30)

  # etiqueta para c
  lb_x = Label(frame_operaciones, text = "   ")
  lb_x.config(bg="pink", fg="black", font=("Verdana", 14, "bold"))
  lb_x.place(x=10, y=100, width=115, height=30)

  # entry para c
  lb_x = Label(frame_operaciones, text = "     ")
  lb_x.config(bg="pink", fg="black", font=("Verdana", 14, "bold"))
  lb_x.place(x=135,y=100,width=115, height=30)

  # etiqueta para d
  lb_x = Label(frame_operaciones, text = "        ")
  lb_x.config(bg="pink", fg="black", font=("Verdana", 14, "bold"))
  lb_x.place(x=250, y=20, width=115, height=30)
  # entry para d
  lb_x = Label(frame_operaciones, text = "        ")
  lb_x.config(bg="pink", fg="black", font=("Verdana", 14, "bold"))
  lb_x.place(x=350,y=20,width=115, height=30)
  
  #boton cuadratica
  bt_cuadratica = Button(frame_operaciones, text="Calcular", command=mostrar_lineal)
  bt_cuadratica.place(x=50,y=150, width=100, height=30)

# Funcion cuadratica
def calcular_cuadratica(a,x,b,c):
    return int(a.get())*x**2+int(b.get())*x+int(c.get())
def funcion_cuadratica():
  # etiqueta para a
  lb_x = Label(frame_operaciones, text = "a =  ")
  lb_x.config(bg="pink", fg="black", font=("Verdana", 14, "bold"))
  lb_x.place(x=10, y=20, width=115, height=30)
  # entry para a
  entry_x = Entry(frame_operaciones, textvariable=a)
  entry_x.config(font=("Verdana", 14, "bold"), justify=LEFT, fg="blue")
  entry_x.focus_set()
  entry_x.place(x=135,y=20,width=115, height=30)
  # etiqueta para b
  lb_x = Label(frame_operaciones, text = "b =  ")
  lb_x.config(bg="pink", fg="black", font=("Verdana", 14, "bold"))
  lb_x.place(x=10, y=60, width=115, height=30)
  # entry para b
  entry_x = Entry(frame_operaciones, textvariable=b)
  entry_x.config(font=("Verdana", 14, "bold"), justify=LEFT, fg="blue")
  entry_x.focus_set()
  entry_x.place(x=135,y=60,width=115, height=30)
  # etiqueta para c
  lb_x = Label(frame_operaciones, text = "c =  ")
  lb_x.config(bg="pink", fg="black", font=("Verdana", 14, "bold"))
  lb_x.place(x=10, y=100, width=115, height=30)
  # entry para c
  entry_x = Entry(frame_operaciones, textvariable=c)
  entry_x.config(font=("Verdana", 14, "bold"), justify=LEFT, fg="blue")
  entry_x.focus_set()
  entry_x.place(x=135,y=100,width=115, height=30)
  # etiqueta para d
  lb_x = Label(frame_operaciones, text = "        ")
  lb_x.config(bg="pink", fg="black", font=("Verdana", 14, "bold"))
  lb_x.place(x=250, y=20, width=115, height=30)
  # entry para d
  lb_x = Label(frame_operaciones, text = "        ")
  lb_x.config(bg="pink", fg="black", font=("Verdana", 14, "bold"))
  lb_x.place(x=350,y=20,width=115, height=30)
  
  #boton calcular
  bt_cuadratica = Button(frame_operaciones, text="Calcular", command=mostrar_cuadratica)
  bt_cuadratica.place(x=50,y=150, width=100, height=30)

def mostrar_cuadratica():
  y=calcular_cuadratica(a,x,b,c)
  plt.plot(x,y,color="r")
  plt.xlabel("x")
  plt.ylabel("y")
  plt.title("Funcion cuadratica: y=ax**2+bx+c")
  plt.grid()
  plt.axhline(y=0,color="b")
  plt.axvline(x=0, color="b")
  plt.show() 
def calcular_cubica(a,x,b,c,d):
    return int(a.get())*x**3+int(b.get())*x**2+int(c.get())*x+int(d.get())
def mostrar_cubica():
  y=calcular_cubica(a,x,b,c,d)
  plt.plot(x,y,color="r")
  plt.xlabel("x")
  plt.ylabel("y")
  plt.title("Funcion cubica: y=ax**3+bx**2+cx+d")
  plt.grid()
  plt.axhline(y=0,color="b")
  plt.axvline(x=0, color="b")
  plt.show() 

def funcion_cubica():
  
  lb_x = Label(frame_operaciones, text = "a =  ")
  lb_x.config(bg="pink", fg="black", font=("Verdana", 14, "bold"))
  lb_x.place(x=10, y=20, width=115, height=30)
  # entry para a
  entry_x = Entry(frame_operaciones, textvariable=a)
  entry_x.config(font=("Verdana", 14, "bold"), justify=LEFT, fg="blue")
  entry_x.focus_set()
  entry_x.place(x=135,y=20,width=115, height=30)
  # etiqueta para b
  lb_x = Label(frame_operaciones, text = "b =  ")
  lb_x.config(bg="pink", fg="black", font=("Verdana", 14, "bold"))
  lb_x.place(x=10, y=60, width=115, height=30)
  #entry para b
  entry_x = Entry(frame_operaciones, textvariable=b)
  entry_x.config(font=("Verdana", 14, "bold"), justify=LEFT, fg="blue")
  entry_x.focus_set()
  entry_x.place(x=135,y=60,width=115, height=30)
  # etiqueta para c
  lb_x = Label(frame_operaciones, text = "c =  ")
  lb_x.config(bg="pink", fg="black", font=("Verdana", 14, "bold"))
  lb_x.place(x=10, y=100, width=115, height=30)
  # entry para c
  entry_x = Entry(frame_operaciones, textvariable=c)
  entry_x.config(font=("Verdana", 14, "bold"), justify=LEFT, fg="blue")
  entry_x.focus_set()
  entry_x.place(x=135,y=100,width=115, height=30)

  # etiqueta para d
  lb_x = Label(frame_operaciones, text = "d =  ")
  lb_x.config(bg="pink", fg="black", font=("Verdana", 14, "bold"))
  lb_x.place(x=250, y=20, width=115, height=30)
  # entry para d
  entry_x = Entry(frame_operaciones, textvariable=d)
  entry_x.config(font=("Verdana", 14, "bold"), justify=LEFT, fg="blue")
  entry_x.focus_set()
  entry_x.place(x=350,y=20,width=115, height=30)

  #boton calcular
  bt_cuadratica = Button(frame_operaciones, text="Calcular", command=mostrar_cubica, borderwidth=5,relief="raised")
  bt_cuadratica.place(x=50,y=150, width=100, height=30)



  
def calcular_exponencial(x,a):
  return int(a.get())**x
def funcion_exponencial():
  
  lb_x = Label(frame_operaciones, text = "a =  ")
  lb_x.config(bg="pink", fg="blue", font=("Verdana", 14, "bold"))
  lb_x.place(x=10, y=20, width=115, height=30)
  # entry para a
  entry_x = Entry(frame_operaciones, textvariable=a)
  entry_x.config(font=("Verdana", 14, "bold"), justify=LEFT, fg="blue")
  entry_x.focus_set()
  entry_x.place(x=135,y=20,width=115, height=30)
  # etiqueta para b
  lb_x = Label(frame_operaciones, text = "          ")
  lb_x.config(bg="pink", fg="black", font=("Verdana", 14, "bold"))
  lb_x.place(x=10, y=60, width=115, height=30)
  #entry para b
  lb_x = Label(frame_operaciones, text = "          ")
  lb_x.config(bg="pink", fg="black", font=("Verdana", 14, "bold"))
  lb_x.place(x=135,y=60,width=115, height=30)
  # etiqueta para c
  lb_x = Label(frame_operaciones, text = "           ")
  lb_x.config(bg="pink", fg="black", font=("Verdana", 14, "bold"))
  lb_x.place(x=10, y=100, width=115, height=30)
  # entry para c
  lb_x = Label(frame_operaciones, text = "           ")
  lb_x.config(bg="pink", fg="black", font=("Verdana", 14, "bold"))
  lb_x.place(x=135,y=100,width=115, height=30)
  # etiqueta para d
  lb_x = Label(frame_operaciones, text = "            ")
  lb_x.config(bg="pink", fg="black", font=("Verdana", 14, "bold"))
  lb_x.place(x=250, y=20, width=115, height=30)
  # entry para d
  lb_x = Label(frame_operaciones, text = "            ")
  lb_x.config(bg="pink", fg="black", font=("Verdana", 14, "bold"))
  lb_x.place(x=350,y=20,width=115, height=30)
  #boton calcular
  bt_cuadratica = Button(frame_operaciones, text="Calcular", command=mostrar_exponencial)
  bt_cuadratica.place(x=50,y=150, width=100, height=30)
def mostrar_exponencial():
  y=calcular_exponencial(x,a)
  plt.plot(x,y,color="r")
  plt.xlabel("x")
  plt.ylabel("y")
  plt.title("Funcion cubica: y=ax**3+bx**2+cx+d")
  plt.grid()
  plt.axhline(y=0,color="b")
  plt.axvline(x=0, color="b")
  plt.show() 
  
# funcion logaritmo
def funcion_logaritmica(x):
  return np.log(x)
def mostrar_logaritmo():
  y=funcion_logaritmica(x)
  plt.plot(x,y,color="r")
  plt.xlabel("x")
  plt.ylabel("y")
  plt.title("Funcion Logaritmica Y=log(x)")
  plt.grid()
  plt.axhline(y=0,color="b")
  plt.axvline(x=0, color="b")
  plt.show()
def funcion_trigonometrica():
  lb_x = Label(frame_operaciones, text = "        ")
  lb_x.config(bg="pink", fg="black", font=("Verdana", 14, "bold"))
  lb_x.place(x=10, y=20, width=115, height=30)
  # entry para a
  lb_x = Label(frame_operaciones, text = "        ")
  lb_x.config(bg="pink", fg="black", font=("Verdana", 14, "bold"))
  lb_x.place(x=135,y=20,width=115, height=30)
  
  # etiqueta para b
  lb_x = Label(frame_operaciones, text = "          ")
  lb_x.config(bg="pink", fg="black", font=("Verdana", 14, "bold"))
  lb_x.place(x=10, y=60, width=115, height=30)
  #entry para b
  lb_x = Label(frame_operaciones, text = "          ")
  lb_x.config(bg="pink", fg="black", font=("Verdana", 14, "bold"))
  lb_x.place(x=135,y=60,width=115, height=30)
  # etiqueta para c
  lb_x = Label(frame_operaciones, text = "           ")
  lb_x.config(bg="pink", fg="black", font=("Verdana", 14, "bold"))
  lb_x.place(x=10, y=100, width=115, height=30)
  # entry para c
  lb_x = Label(frame_operaciones, text = "           ")
  lb_x.config(bg="pink", fg="black", font=("Verdana", 14, "bold"))
  lb_x.place(x=135,y=100,width=115, height=30)
  # etiqueta para d
  lb_x = Label(frame_operaciones, text = "            ")
  lb_x.config(bg="pink", fg="black", font=("Verdana", 14, "bold"))
  lb_x.place(x=250, y=20, width=115, height=30)
  # entry para d
  lb_x = Label(frame_operaciones, text = "            ")
  lb_x.config(bg="pink", fg="black", font=("Verdana", 14, "bold"))
  lb_x.place(x=350,y=20,width=115, height=30)
  #boton calcular
  lb_x = Label(frame_operaciones, text = "            ")
  lb_x.config(bg="pink", fg="black", font=("Verdana", 14, "bold"))
  lb_x.place(x=50,y=150, width=100, height=30)

  #boton seno
  
  bt_seno = Button(frame_operaciones, text="sen(x)", command=mostrar_seno)
  bt_seno.place(x=50,y=150, width=100, height=30)

  bt_coseno = Button(frame_operaciones, text="cos(x)", command=mostrar_coseno)
  bt_coseno.place(x=180,y=150, width=100, height=30)

  bt_tangente= Button(frame_operaciones, text="tan(x)", command=mostrar_tangente)
  bt_tangente.place(x=350,y=150, width=100, height=30)
  return bt_coseno.destroy
  
def funcion_trigonometricaseno(x):
  return sin(x)
def mostrar_seno():
  y=funcion_trigonometricaseno(x)
  plt.plot(x,y,color="r")
  plt.xlabel("x")
  plt.ylabel("y")
  plt.title("Funcion sen(x)")
  plt.grid()
  plt.axhline(y=0,color="b")
  plt.axvline(x=0, color="b")
  plt.show()
  
def funcion_trigonometricacoseno(x):
  return cos(x)
def mostrar_coseno():
  y=funcion_trigonometricacoseno(x)
  plt.plot(x,y,color="r")
  plt.xlabel("x")
  plt.ylabel("y")
  plt.title("Funcion cos(x)")
  plt.grid()
  plt.axhline(y=0,color="b")
  plt.axvline(x=0, color="b")
  plt.show()
def funcion_trigonometricatangente(x):
  return tan(x)
def mostrar_tangente():
  y=funcion_trigonometricatangente(x)
  plt.plot(x,y,color="r")
  plt.xlabel("x")
  plt.ylabel("y")
  plt.title("Funcion tan(x)")
  plt.grid()
  plt.axhline(y=0,color="b")
  plt.axvline(x=0, color="b")
  plt.show()
    
ventana_principal = Tk()
c= StringVar()
a = StringVar()
b = StringVar()
m = StringVar()
d = StringVar()
x= np.linspace(-10,10, num=N)


# titulo de la ventana
ventana_principal.title("GRAFICA DE FUNCIONES")

# color de fondo ventana principal
ventana_principal.configure(bg="#db03fc", highlightbackground="black", highlightthickness=8)

# tamañan de la ventana
ventana_principal.geometry("500x500")

# deshabilitar boton de maximizar
ventana_principal.resizable(False,False)

# color de fondo de la ventana
ventana_principal.config(bg= "#db03fc")

# etiqueta para el titulo de la app
label_titulo = tk.Label(text="_Tipos de funciones_",background="#db03fc",foreground="#090909",font=("Verdana", 18, "bold"),)
label_titulo.place(x=122,y=10)

# boton lineal
boton_papel = tk.Button(ventana_principal,background="white",text="Lineal => y = mx + b",borderwidth=5,relief="raised",command=funcion_lineal)
boton_papel.place(x=150,y=60, width=200, height=30)

#boton cuadratica
boton_papel = tk.Button(ventana_principal,background="white",text="Cuadrática => y = ax^2 + bx + c",borderwidth=5,relief="raised",command=funcion_cuadratica)
boton_papel.place(x=150,y=95, width=200, height=30)


#boton cubica

boton_papel = tk.Button(ventana_principal,background="white",text="Cubica =>y= ax**3 + bx 2 + cx + d",borderwidth=5,relief="raised",command=funcion_cubica)
boton_papel.place(x=150,y=130, width=200, height=30)

#boton expotencial

boton_papel = tk.Button(ventana_principal,background="white",text="Exponencial =>y = a^x",borderwidth=5,relief="raised",command=funcion_exponencial)
boton_papel.place(x=150,y=165, width=200, height=30)

#funcion logaritmo
boton_papel = tk.Button(ventana_principal,background="white",text="logaritomo =>y = ln(ax) + b ",borderwidth=5,relief="raised",command=mostrar_logaritmo)
boton_papel.place(x=150,y=200, width=200, height=30)


#funcion trigonometrica
boton_papel = tk.Button(ventana_principal,background="white",text="trigonometrica=>sen-cos-tag",borderwidth=5,relief="raised",command=funcion_trigonometrica)
boton_papel.place(x=150,y=235, width=200, height=30)



# ------------------------
# frame operaciones
# ------------------------
frame_operaciones = Frame(ventana_principal)
frame_operaciones.config(bg="#b503fc", width=480, height=185)
frame_operaciones.place(x=2,y=300)


ventana_principal.mainloop()
