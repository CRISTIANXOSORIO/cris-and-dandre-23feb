import tkinter     

ventana= tkinter.Tk()
ventana.geometry("400x400")
ventana.configure(background="aqua")

def borrar():
      panel.config(text= "")



panel = tkinter.Label(ventana,text="",background="white", font="arial 15",bd=0, padx=10,pady=10)
panel.pack()

def cambio_de_texto():
      texto = entrada.get()
      panel.config(text= texto)
  
  
entrada=tkinter.Entry(ventana,font="arial 15",bd=6)
entrada.pack()

boton_c=tkinter.Button(ventana, text="nuevo texto", font="consolas 15 bold",command=cambio_de_texto)
boton_c.pack()
 
botonb=tkinter.Button(ventana, text="BORRAR", font="consolas 15 bold",command= borrar)
botonb.pack()

botond = tkinter.Button(ventana, text="DESHABILITADO", state="disabled")
botond.pack()


ventana.mainloop()