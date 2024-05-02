import tkinter as tk

def mostrar():
    frame=tk.Frame(ventana,width=200,height=200)
    frame.config(borderwidth=3,relief="solid")
    frame.grid(row=6,column=0)
    fnombre=tk.Label(frame,text="NOMBRE: ")
    fapellido=tk.Label(frame,text="APELLIDO: ")
    fedad=tk.Label(frame,text="EDAD: ")
    fsexo=tk.Label(frame,text="SEXO: ")
    fciudad=tk.Label(frame,text="CIUDAD: ")
    
    fnombre.place(x=0,y=0)
    fapellido.place(x=0,y=20)
    fedad.place(x=0,y=40)
    fsexo.place(x=0,y=60)
    fciudad.place(x=0,y=80)
    
    rnombre=tk.Label(frame,text=lnombre.get())
    rapellido=tk.Label(frame,text=lapellido.get())
    redad=tk.Label(frame,text=ledad.get())
    rsexo=tk.Label(frame,text=opcion.get())
    rciudad=tk.Label(frame,text=pciudad.get(pciudad.curselection()))
    
    rnombre.place(x=60,y=0)
    rapellido.place(x=60,y=20)
    redad.place(x=60,y=40)
    rsexo.place(x=60,y=60)
    rciudad.place(x=60,y=80)
    
    
    


ventana=tk.Tk()
ventana.title("Ventana miguel")
ventana.geometry("500x800")


nombre=tk.Label(ventana,text="Nombre:")
nombre.grid(row=0,column=0)
lnombre=tk.Entry(ventana,width=20)
lnombre.grid(row=0,column=1)

apellido=tk.Label(ventana,text="Apellido:")
apellido.grid(row=1,column=0)
lapellido=tk.Entry(ventana,width=20)
lapellido.grid(row=1,column=1)

edad=tk.Label(ventana,text="Edad:")
edad.grid(row=2,column=0)
ledad=tk.Entry(ventana,width=20)
ledad.grid(row=2,column=1)

sexo=tk.Label(ventana,text="Sexo:")
sexo.grid(row=3,column=0)
opcion=tk.StringVar()
rsexoM=tk.Radiobutton(ventana,text="Masculino",state="normal",variable=opcion,value="Masculino")
rsexoM.grid(row=3,column=1)
rsexoF=tk.Radiobutton(ventana,text="Femenino",state="normal",variable=opcion,value="femenino")
rsexoF.grid(row=3,column=2)

ciudad=tk.Label(ventana,text="Ciudad:")
ciudad.grid(row=4,column=0)
pciudad=tk.Listbox(ventana,width=20)
elementos=["Cartagena","Cali","Barranquilla"]
for elemento in elementos:
    pciudad.insert(tk.END, elemento)
pciudad.grid(row=4,column=1)

#boton
boton=tk.Button(ventana,text="Registrar",command=mostrar)
boton.grid(row=5,column=1)

ventana.mainloop()