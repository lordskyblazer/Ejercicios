import tkinter

root = tkinter.Tk()
root.geometry("300x300")
root.maxsize(400, 600)
boton = tkinter.Button(root, text="Minimizar", command=root.iconify)
boton.pack()
root.mainloop()
