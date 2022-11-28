import tkinter
ve =tkinter.Tk()
ve.geometry("900x400")
ve.resizable(0,0)
ve.title("Electronica")
#funciones

from tkinter import ttk
#tablas
tabla=ttk.Treeview(ve,columns=("Articulos","Precios"))
tabla.grid(row=0,column=3,columnspan=3)
tabla.heading("#0",text="id")
tabla.heading("#1",text="Articulos")
tabla.heading("#2",text="Precio")
tabla.insert("",0,text="1",values=("Harina","2000"))
tabla.insert("",1,text="2",values=("cereal","2000"))
tabla.place(x=8,y=8)
b4=tkinter.Button(ve,text="Editar")
b4.grid(row=2,column=3)
b4.config(width=5,font=("Arial",8,"bold"),fg="white",bg="blue",cursor="hand2",activebackground="#33AFFF")
b4.place(x=650,y=100)
b3=tkinter.Button(ve,text="guardar")
b3.config(width=5,font=("Arial",8,"bold"),fg="white",bg="blue",cursor="hand2",activebackground="#33AFFF")
b3.place(x=700,y=100)
ve.mainloop()
