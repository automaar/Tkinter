import tkinter
root=tkinter.Tk()
root.title("inventario")
root.geometry("900x800")
root.resizable(0,0)
be=tkinter.Button(root,text="electronica",width=9,height=3,bg="#5CCCCC",cursor="hand2",activebackground="turquoise2")
be.grid(row=1,column=1)
bm=tkinter.Button(root,text="micelanio",width=9,height=3,bg="#9F3ED5",cursor="hand2",activebackground="#AD3ED5")
bm.grid(row=1,column=2)
bp=tkinter.Button(root,text="persona",width=9,height=3,bg="#FF4040",cursor="hand2",activebackground="#FF1540")
bp.grid(row=1,column=3)
ba=tkinter.Button(root,text="administrativo",width=9,height=3,bg="#6CFFBE",cursor="hand2",activebackground="#6BE3D3")
ba.grid(row=1,column=4)
bh=tkinter.Button(root,text="Heramientas",width=9,height=3,cursor="hand2",activebackground="#FF1540")
bh.grid(row=1,column=5)
bv=tkinter.Button(root,text="ver todo",width=9,height=3,cursor="hand2",activebackground="#FF1540")
bv.grid(row=1,column=6)
img=tkinter.PhotoImage(file="tk.gif")
l=tkinter.Label(root,image=img).grid(row=6,column=6)



root.mainloop()
