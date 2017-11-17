from tkinter import*
import tkinter as tk
from tkinter import messagebox
import webbrowser

def abrirventana():
    ventana1.withdraw()
    ventana = tk.Tk()
    ventana.title("¿Qué estas buscando?")
    ventana.geometry('500x700')
    ventana.configure(background='medium aquamarine')
    etiqueta1 = tk.Label(ventana, text="¿Qué estas buscando?", bg='navy', fg='white')
    etiqueta1.pack(padx=20, pady=20, ipadx=20, ipady=20)


    
    # Lista desplegable para la primera opción
    #var = tk.StringVar(ventana)
    #var.set('Seleccione alguna opción')
    e1 = tk.Label(ventana, text="1. Hospitales", bg='sea green', fg='white')
    e1.config(width=25)
    e1.pack(padx=5, pady=5, ipadx=5, ipady=5)
    def abrir_generales():
        webbrowser.open("file:///C:/Proyecto_Mapa_ubicaciones/Hospitales%20generales.html", new=2, autoraise=True)
    def abrir_privados():
        webbrowser.open("file:///C:/Proyecto_Mapa_ubicaciones/Hospitales%20privados.html", new=2, autoraise=True)
    def abrir_centros_de_salud():
        webbrowser.open("file:///C:/Proyecto_Mapa_ubicaciones/Hospitales%20centros%20de%20salud.html", new=2, autoraise=True)
    def abrir_en_otros_distritos():
        webbrowser.open("file:///C:/Proyecto_Mapa_ubicaciones/Hospitales%20en%20otros%20distritos.html", new=2, autoraise=True)

    Generales_button=tk.Button(ventana,text="Generales",bg="white",fg="black",command=abrir_generales)
    Generales_button.config(width=18)
    Generales_button.pack(padx=2, pady=2, ipadx=1, ipady=1)
    
    Generales_button=tk.Button(ventana,text="Privados",bg="white",fg="black",command=abrir_privados)
    Generales_button.config(width=18)
    Generales_button.pack(padx=2, pady=2, ipadx=1, ipady=1)

    Generales_button=tk.Button(ventana,text="Centros de salud",bg="white",fg="black",command=abrir_centros_de_salud)
    Generales_button.config(width=18)
    Generales_button.pack(padx=2, pady=2, ipadx=1, ipady=1)

    Generales_button=tk.Button(ventana,text="En otros distritos",bg="white",fg="black",command=abrir_en_otros_distritos)
    Generales_button.config(width=18)
    Generales_button.pack(padx=2, pady=2, ipadx=1, ipady=1)

    #opciones = ['Generales', 'Privados', 'Centros de salud', 'En otros distritos']
    #opcion = tk.OptionMenu(ventana, var, *opciones)
    #opcion.config(width=25)
    #opcion.pack(padx=5, pady=10)


    
    # Lista desplegable para la segunda opción
    #var2= tk.StringVar(ventana)
    #var2.set('Seleccione alguna opción')
    e2 = tk.Label(ventana, text="2. Bancos", bg='goldenrod', fg='white')
    e2.config(width=25)
    e2.pack(padx=5, pady=5, ipadx=5, ipady=5)
    def abrir_BN_BBVA_BCP():
        webbrowser.open("file:///C:/Proyecto_Mapa_ubicaciones/Bancos%20BBVA%20BCP%20BN.html", new=2, autoraise=True)
    def abrir_otros_bancos():
        webbrowser.open("file:///C:/Proyecto_Mapa_ubicaciones/Bancos%20otros%20bancos.html", new=2, autoraise=True)
    def abrir_en_otros_distritos2():
        webbrowser.open("file:///C:/Proyecto_Mapa_ubicaciones/Bancos%20en%20otros%20distritos.html", new=2, autoraise=True)

    Generales_button=tk.Button(ventana,text="BN/BBVA/BCP",bg="white",fg="black",command=abrir_BN_BBVA_BCP)
    Generales_button.config(width=18)
    Generales_button.pack(padx=2, pady=2, ipadx=1, ipady=1)
    
    Generales_button=tk.Button(ventana,text="Otros bancos",bg="white",fg="black",command=abrir_otros_bancos)
    Generales_button.config(width=18)
    Generales_button.pack(padx=2, pady=2, ipadx=1, ipady=1)

    Generales_button=tk.Button(ventana,text="En otros distritos",bg="white",fg="black",command=abrir_en_otros_distritos2)
    Generales_button.config(width=18)
    Generales_button.pack(padx=2, pady=2, ipadx=1, ipady=1)
    
    #opciones2 = ['BN/BBVA/BCP', 'Otros bancos', 'En otros distritos']
    #opcion2 = tk.OptionMenu(ventana, var2, *opciones2)
    #opcion2.config(width=25)
    #opcion2.pack(padx=5, pady=10)


    
    # Lista desplegable para la tercera opción
    #var3 = tk.StringVar(ventana)
    #var3.set('Seleccione alguna opción')
    e3 = tk.Label(ventana, text="3. Gasolineras", bg='firebrick', fg='white')
    e3.config(width=25)
    e3.pack(padx=5, pady=5, ipadx=5, ipady=5)

    def abrir_mas_cercanos():
        webbrowser.open("file:///C:/Proyecto_Mapa_ubicaciones/Gasolinerias%20cerca.html", new=2, autoraise=True)
    def abrir_en_otros_distritos3():
        webbrowser.open("file:///C:/Proyecto_Mapa_ubicaciones/Gasolinerias%20en%20otros%20distritos.html", new=2, autoraise=True)

    Generales_button=tk.Button(ventana,text="Más cercanos",bg="white",fg="black",command=abrir_mas_cercanos)
    Generales_button.config(width=18)
    Generales_button.pack(padx=2, pady=2, ipadx=1, ipady=1)
    
    Generales_button=tk.Button(ventana,text="En otros distritos",bg="white",fg="black",command=abrir_en_otros_distritos3)
    Generales_button.config(width=18)
    Generales_button.pack(padx=2, pady=2, ipadx=1, ipady=1)
    
    #opciones3 = ['Más cercanos', 'En otros distritos']
    #opcion3 = tk.OptionMenu(ventana, var3, *opciones3)
    #opcion3.config(width=25)
    #opcion3.pack(padx=5, pady=10)
    
    
    
    # Lista desplegable para la cuarta opción
    #var4 = tk.StringVar(ventana)
    #var4.set('Seleccione alguna opción')
    e4 = tk.Label(ventana, text="4. Hoteles", bg='steel blue', fg='white')
    e4.config(width=25)
    e4.pack(padx=5, pady=5, ipadx=5, ipady=5)

    def abrir_1a3():
        webbrowser.open("file:///C:/Proyecto_Mapa_ubicaciones/Hoteles%201-3.html", new=2, autoraise=True)
    def abrir_4a5():
        webbrowser.open("file:///C:/Proyecto_Mapa_ubicaciones/Hoteles%204-5.html", new=2, autoraise=True)
    def abrir_mejores_valoraciones():
        webbrowser.open("file:///C:/Proyecto_Mapa_ubicaciones/Hoteles%20mejores%20valoraciones.html", new=2, autoraise=True)
    def abrir_en_otros_distritos4():
        webbrowser.open("file:///C:/Proyecto_Mapa_ubicaciones/Hoteles%20en%20otros%20distritos.html", new=2, autoraise=True)

    Generales_button=tk.Button(ventana,text="* a ***",bg="white",fg="black",command=abrir_1a3)
    Generales_button.config(width=18)
    Generales_button.pack(padx=2, pady=2, ipadx=1, ipady=1)
    
    Generales_button=tk.Button(ventana,text="**** a *****",bg="white",fg="black",command=abrir_4a5)
    Generales_button.config(width=18)
    Generales_button.pack(padx=2, pady=2, ipadx=1, ipady=1)

    Generales_button=tk.Button(ventana,text="Mejores valoraciones",bg="white",fg="black",command=abrir_mejores_valoraciones)
    Generales_button.config(width=18)
    Generales_button.pack(padx=2, pady=2, ipadx=1, ipady=1)

    Generales_button=tk.Button(ventana,text="En otros distritos",bg="white",fg="black",command=abrir_en_otros_distritos4)
    Generales_button.config(width=18)
    Generales_button.pack(padx=2, pady=2, ipadx=1, ipady=1)
    
    #opciones4 = ['* a ***', '**** a *****', 'Mejores valoraciones', 'En otros distritos']
    #opcion4 = tk.OptionMenu(ventana, var4, *opciones4)
    #opcion4.config(width=25)
    #opcion4.pack(padx=5, pady=10)

    ventana.mainloop()
#Aabrir la ventana principal
ventana1=tk.Tk()
ventana1.geometry("498x281")
ventana1.title("Barrranco view - Entrada")
#Imagen de fondo
imagen_de_fondo=PhotoImage(file="fondofinal.gif")
lbldelaimagen1=tk.Label(ventana1,image=imagen_de_fondo).place(x=0,y=0)

#Boton para entrar

Boton_pa_entrar=tk.Button(ventana1,text="Ingresar",font=("Times New Roman",16),bg="white",fg="black",command=abrirventana).place(x=209,y=190)

ventana1.mainloop()
