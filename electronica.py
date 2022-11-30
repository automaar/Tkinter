
from ast import Import
from tkinter import Tk, Button, Frame
from tkinter import CENTER, Entry, Label, Tk, Frame
import tkinter as tk
from tkinter.ttk import Combobox, Treeview
from tkinter import *

# Crear Ventana
ventana = Tk()
ventana.title("Agregar elementos a Treview")
ventana.geometry("700x300")
ventana.resizable(0,0)

# Crear Frame
frame1 = Frame(ventana, bg="#bfdaff")
frame1.place(x=0, y=0, width=100, height=270)

# Variables Var
producto = tk.StringVar()
precio = tk.DoubleVar()
cantidad = tk.DoubleVar()
subtotal = tk.DoubleVar()
total = tk.DoubleVar()
contador = IntVar()

# Variables lista
lst_productos = ["pc mesa", "laptop"]
lst_Precio = [20, 35, 22, 21, 15]

# Variables del TreV
listaEncabezados = ["Producto", "Precio", "Cantidad", "Subtotal"]
Columnas = ["#0", "col1", "col2", "col3"]


# Funciones de Calculo
def CargarPrecio(event):
    producto.set(ventana.cmbProductos.get())
    precio.set(lst_Precio[ventana.cmbProductos.current()])


def Calcular():
    subtotal.set(cantidad.get() * precio.get())
    return subtotal.set


def Agregar():
    ventana.tv.insert("", "end", text=producto.get(), values=(precio.get(), cantidad.get(), subtotal.get()))


def Total():
    ""



# Componentes visuales
ventana.btnAgregar = Button(frame1, text="Agregar", command=Agregar, bg="azure", fg="DIM GRAY")
ventana.btnAgregar.place(x=5, y=50, width=80, height=30)

ventana.btnSubtotal = Button(frame1, text="Subtotal", command=Calcular, bg="azure", fg="DIM GRAY")
ventana.btnSubtotal.place(x=5, y=90, width=80, height=30)

ventana.btnTotal = Button(frame1, text="Total", command=Total, bg="azure", fg="DIM GRAY")
ventana.btnTotal.place(x=5, y=130, width=80, height=30)

# Frame cajas
frameCajas = Frame(ventana, bg="#d3dde3")
frameCajas.place(x=95, y=0, width=195, height=259)

# Declaracion de etiquetas  y cajas
ventana.lblProducto = Label(frameCajas, text="Producto", bg="bisque2", fg="white",
                            font=("Courier new", 14, "italic")).place(x=10, y=5)
ventana.cmbProductos = Combobox(frameCajas, state="readonly")
ventana.cmbProductos.place(x=10, y=25)
ventana.cmbProductos["values"] = lst_productos
ventana.cmbProductos.current(0)
ventana.cmbProductos.bind("<<ComboboxSelected>>", CargarPrecio)

ventana.lblPrecio = Label(frameCajas, text="Precio", bg="bisque2", fg="white", font=("Courier new", 14, "italic")).place(
    x=10, y=50)
ventana.txtPrecio = Entry(frameCajas, textvariable=precio).place(x=10, y=75)

ventana.lblCantidad = Label(frameCajas, text="Cantidad", bg="bisque2", fg="white",
                            font=("Courier new", 14, "italic")).place(x=10, y=100)
ventana.txtCantidad = Entry(frameCajas, textvariable=cantidad).place(x=10, y=125)

ventana.lblSubtotal = Label(frameCajas, text="Subtotal", bg="bisque2", fg="white",
                            font=("Courier new", 14, "italic")).place(x=10, y=150)
ventana.txtSubtotal = Entry(frameCajas, textvariable=subtotal).place(x=10, y=175)

lblTotal = Label(ventana, text="Total a pagar: ", bg="BISQUE2", fg="white", font=("Courier new", 14, "italic")).place(x=10,
                                                                                                                   y=250)
txtTotal = Entry(ventana, textvariable=total, bg="bisque2").place(x=175, y=250, width=50, height=28)

# Tercer Frame Treeview
frameTv = Frame(ventana, bg="#5D8BF4")
frameTv.place(x=292, y=0, width=450, height=300)
ventana.tv = Treeview(frameTv, columns=(Columnas[1], Columnas[2], Columnas[3]))
for x in range(0, len(Columnas)):
    ventana.tv.column(Columnas[x], width=80, anchor=CENTER)
    ventana.tv.heading(Columnas[x], text=listaEncabezados[x], anchor=CENTER)
ventana.tv.pack()

ventana.mainloop()
