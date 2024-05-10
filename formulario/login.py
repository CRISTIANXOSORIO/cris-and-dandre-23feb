import tkinter 
from PIL import Image, ImageTk
from tkinter import messagebox

ventana= tkinter.Tk()
ventana.geometry("800x500")
ventana.resizable(False,False)

image = Image.open("logo.jpg")
logo = ImageTk.PhotoImage(image)
inicio_imagen = tkinter.Label(ventana,image=logo, height=510, width=800)
inicio_imagen.place(x=0,y=0)

login_panel = tkinter.Label(ventana,text="INGRESAR",font= "arial 14")
login_panel.place(x= "300", y="80",width= "200")

login_usuario = tkinter.Label(ventana,text="USUARIO: ",font= "arial 14")
login_usuario.place(x= "200", y="140",width= "200")

login_CLAVE = tkinter.Label(ventana,text="CLAVE: ",font= "arial 14")
login_CLAVE.place(x= "200", y="200",width= "200")

entrada_usurio = tkinter.Entry(ventana,font= "arial 14",bd=4)
entrada_usurio.place(x= "420", y="140",width= "120")

entrada_clave = tkinter.Entry(ventana,font= "arial 14",bd=4)
entrada_clave.place(x= "420", y="200",width= "120")

def ingreso():
    
    user = entrada_usurio.get()
    contra = entrada_clave.get()
    
    if user == "" and contra == "":
        messagebox.showinfo("","CAMPOS VACIOS " + str(user))
    else:
        messagebox.showinfo("","BIENVENIDO " + str(user))
    

boton_ingresar = tkinter.Button(ventana,text="INGRESAR",font= "arial 14",bd=4,command=ingreso)
boton_ingresar.place(x= "360", y="300",width= "120")


ventana.mainloop()