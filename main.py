import tkinter


def informacion():
    root = tkinter.Tk()
    root.title("informacion")
    root.geometry("440x100")
    root.resizable(0, 0)
    text=tkinter.Label(root,text="Creadores:Yondry Millano,Marcos Samudio,Brahian Tovar y Yosselin Montero")
    text.grid()


def ver():
    root = tkinter.Tk()
    root.title("informacion")
    root.geometry("440x100")
    root.resizable(0, 0)
    text=tkinter.Label(root,text="Version 0.1")
    text.grid()


def detruir():
    root.destroy()


root=tkinter.Tk()
root.title("inventario")
root.geometry("440x100")
root.resizable(0,0)
#botones
be=tkinter.Button(root,text="electronica",width=9,height=3,bg="#5CCCCC",cursor="hand2",activebackground="turquoise2")
be.grid(row=1,column=1)



bm=tkinter.Button(root,text="micelanio",width=9,height=3,bg="#9F3ED5",cursor="hand2",activebackground="#AD3ED5")
bm.grid(row=1,column=2)

bp=tkinter.Button(root,text="personal",width=9,height=3,bg="#FF4040",cursor="hand2",activebackground="#FF1540")
bp.grid(row=1,column=3)

ba=tkinter.Button(root,text="administrativo",width=9,height=3,bg="#6CFFBE",cursor="hand2",activebackground="#6BE3D3")
ba.grid(row=1,column=4)

bh=tkinter.Button(root,text="Heramientas",width=9,height=3,cursor="hand2",activebackground="#FF1540")
bh.grid(row=1,column=5)

bv=tkinter.Button(root,text="ver todo",width=9,height=3,cursor="hand2",activebackground="#FF1540")
bv.grid(row=1,column=6)



#menu
b_menu = tkinter.Menu()


menu_archivo = tkinter.Menu(b_menu, tearoff=False)

menu_sec_g = tkinter.Menu(b_menu)
b_menu.add_cascade(menu=menu_sec_g, label="Archivo")
menu_sec_g.add_command(label="Guardar")
root.config(menu=b_menu)
menu_sec_g.add_command(label="Reset")
menu_sec_g.add_command(label="Salir",command=detruir)


menu_sec_r = tkinter.Menu(b_menu)
b_menu.add_cascade(menu=menu_sec_r, label="Opciones")
menu_sec_r.add_command(label="Cargar")
menu_sec_r.add_command(label="Exportar")

menu_sec_a = tkinter.Menu(b_menu)
b_menu.add_cascade(menu=menu_sec_a, label="Ayuda")
menu_sec_a.add_command(label="Información",command=informacion)
menu_sec_a.add_command(label="Ver",command=ver)




root.mainloop()
