import tkinter as tK

ventana = tK.Tk()

ventana.title("VENTANA MIGUEL")

ventana.geometry("800x700")

lnombre = tK.Label(ventana, text="Nombre:")
lnombre.grid(row=0,column=0)
cnombre = tK.Entry(ventana, width=30)
cnombre.grid(row=0,column=1)

lapellido = tK.Label(ventana, text="apellido:")
lapellido.grid(row=1,column=0)
capellido = tK.Entry(ventana, width=30)
capellido.grid(row=1,column=1)

ledad = tK.Label(ventana, text="edad:")
ledad.grid(row=2,column=0)
cedad = tK.Entry(ventana, width=30)
cedad.grid(row=2,column=1)


lsexo = tK.Label(ventana, text="sexo: " )
lsexo.grid(row=3,column=0)
lsexo = tK.Label(ventana, text="masculino" )
lsexo.grid(row=3,column=1)
csexo = tK.Radiobutton(ventana, none=None, state="normal")
csexo.grid(row=3,column=2)
lsexo = tK.Label(ventana, text="femenino" )
lsexo.grid(row=3,column=3)
msexo = tK.Radiobutton(ventana, none=None, state="normal")
msexo.grid(row=3,column=4)

lciudad = tK.Label(ventana, text="ciudad:")
lciudad.grid(row=4,column=0)
Cciudad = tK.Listbox(ventana, width=20)
elementos =["cartagena", "bogota","cali"]
for elementos in elementos:
        Cciudad.insert(tK.END, elementos)
        Cciudad.grid(row=4, column=1)
        
        boton=tK.Button(ventana, text="registrar")
        boton.grid(row=5, column=1)



ventana.mainloop()