import tkinter as tk
root = tk.Tk()

def destruir():
    root.destroy()

root.config(width=400, height=300)
b_menu = tk.Menu()

#Primera Opcion de Menu
menu_archivo = tk.Menu(b_menu, tearoff=False)

menu_sec_g = tk.Menu(b_menu)
b_menu.add_cascade(menu=menu_sec_g, label="Archivo")
menu_sec_g.add_command(label="Guardar")
root.config(menu=b_menu)
menu_sec_g.add_command(label="Reset")
menu_sec_g.add_command(label="Salir", command=destruir)


menu_sec_r = tk.Menu(b_menu)
b_menu.add_cascade(menu=menu_sec_r, label="Opciones")
menu_sec_r.add_command(label="Cargar")
menu_sec_r.add_command(label="Exportar")

menu_sec_a = tk.Menu(b_menu)
b_menu.add_cascade(menu=menu_sec_a, label="Ayuda")
menu_sec_a.add_command(label="Información")
menu_sec_a.add_command(label="Ver")



root.mainloop()