import tkinter
from tkinter import ttk
ve =tkinter.Tk()
ve.geometry("1050x250")
ve.resizable(0,0)
ve.title("Electronica")
#funciones
def edit():
    tabla.insert(e1.get())

#tablas
tabla=ttk.Treeview(ve,columns=("Articulos","Precios","piesas"))
tabla.grid(row=0,column=3,columnspan=3)
tabla.heading("#0",text="id")
tabla.heading("#1",text="Articulos")
tabla.heading("#2",text="piesas")
tabla.heading("#3",text="total")
tabla.insert("",0,text="1",values=("pc gamer","","200"))
tabla.insert("",1,text="2",values=("laptop","2000"))
tabla.place(x=8,y=8)
#botones
b4=tkinter.Button(ve,text="Editar")
b4.grid(row=2,column=3)
b4.config(width=5,font=("Arial",8,"bold"),fg="white",bg="blue",cursor="hand2",activebackground="#33AFFF")
b4.place(x=850,y=200)
b3=tkinter.Button(ve,text="guardar")
b3.config(width=5,font=("Arial",8,"bold"),fg="white",bg="blue",cursor="hand2",activebackground="#33AFFF")
b3.place(x=900,y=200)
b2=tkinter.Button(ve,text="eliminar",command=edit)
b2.config(width=10,font=("Arial",8,"bold"),fg="white",bg="red",cursor="hand2",activebackground="#BD152E")
b2.place(x=950,y=200)
#entrar
e1=tkinter.Entry(ve,font=("calibri 13"))
e1.place(x=850,y=100,)
et1=tkinter.Label(ve,text="agregar articulo:")
et1.place(x=850,y=77)

ve.mainloop()
