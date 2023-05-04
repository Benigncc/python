from tkinter import *
menu = Tk()
menu.title("ingreso")
#ingresa nombre
Label(menu, text="nombre").grid(row=1,column=0)
in_name = Entry(menu)
#in_name.insert(0,"ingrese nombre")
#in_name.bind("<Button-1>",lambda call : in_name.delete(0,END))
in_name.grid(row=1,column=1)

#ingresa edad
Label(menu, text="edad").grid(row=2,column=0)
in_edad = Entry(menu)
in_edad.grid(row=2,column=1) 
# in_edad.insert(0,"ingresa edad")
# in_edad.bind("<Button-1>", lambda call: in_edad.delete(0,END))
#funcion
def ingreso():
    name = in_name.get()
    edad = in_edad.get()
    Label(menu,text=f"tu nombre es : {name} y tu edad es : {edad}").grid(row=4,column=1)


#boton
Button(menu,text="ingresar", command = ingreso).grid(row=3,column=0)





menu.mainloop()