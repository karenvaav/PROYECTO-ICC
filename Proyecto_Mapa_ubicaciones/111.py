from tkinter import *
import tkinter as tk
from tkinter import messagebox
import webbrowser
import folium
import pandas
import os
 
creds = 'tempfile.temp'
 
def Signup(): 
    global pwordE 
    global nameE
    global roots
 
    roots = Tk() 
    roots.title('REGISTRARSE')
    roots.configure(background='medium aquamarine')
    roots.geometry('380x150')
    intruction = Label(roots, text='NUEVAS CREDENCIALES\n', bg='medium aquamarine', fg='black',bd=1,font=(16))
    intruction.grid(row=0, column=1, sticky=E)
 
    nameL = Label(roots, text='Nuevo Usuario:', bg='medium aquamarine', fg='black',bd=3) 
    pwordL = Label(roots, text='Nueva Contraseña:', bg='medium aquamarine', fg='black', bd=3) 
    nameL.grid(row=1, column=0, sticky=W) 
    pwordL.grid(row=2, column=0, sticky=W) 
 
    nameE = Entry(roots) 
    pwordE = Entry(roots, show='*') 
    nameE.grid(row=1, column=1) 
    pwordE.grid(row=2, column=1)
    
 
    signupButton = Button(roots, text='Crear credencial', command=FSSignup, bg='light slate gray', fg='black')
    signupButton.grid(row=5, column=1, sticky=W)
    roots.mainloop()

def FSSignup():
    with open(creds, 'w') as f: 
        f.write(nameE.get()) 
        f.write('\n') 
        f.write(pwordE.get()) 
        f.close() 

    abrirventana() 

#no se we
def Login():
    global nameEL
    global pwordEL 
    global rootA
 
    rootA = Tk() 
    rootA.title('Login')
    rootA.configure(background='rosy brown')
    rootA.geometry('280x150') 
    intruction = Label(rootA, text='INICIAR SESIÓN\n', bg='rosy brown',fg='black',bd=1,font=(16)) 
    intruction.grid(row=0, column=1, sticky=E) 
 
    nameL = Label(rootA, text='Usuario:', bg='rosy brown',fg='black') 
    pwordL = Label(rootA, text='Contraseña:', bg='rosy brown', fg='black') 
    nameL.grid(row=1, sticky=W)
    pwordL.grid(row=2, sticky=W)
 
    nameEL = Entry(rootA) 
    pwordEL = Entry(rootA, show='*')
    nameEL.grid(row=1, column=1)
    pwordEL.grid(row=2, column=1)
 
    loginB = Button(rootA, text='Ingresar', command=CheckLogin,bg='dark salmon',fg='black') 
    loginB.grid(row=4,column=1, sticky=W)
 
    rmuser = Button(rootA, text='Registrate', bg='brown',fg='black', command=DelUser) 
    rmuser.grid(row=5,column=1, sticky=W)
    rootA.mainloop()
    if os.path.isfile(creds):
        Login()
    else: 
        Signup()
 
def CheckLogin():
    with open(creds) as f:
        data = f.readlines() 
        uname = data[0].rstrip() 
        pword = data[1].rstrip() 
 
    if nameEL.get() == uname and pwordEL.get() == pword:
        ventana1.withdraw
        borrar()
        abrirventana()


    else:
        r = Tk()
        r.title('D:')
        r.geometry('150x50')
        rlbl = Label(r, text='\n[!] Ingreso inválido')
        rlbl.pack()
        r.mainloop()
    abrirventana()

def DelUser():
    os.remove(creds) 
    rootA.destroy() 
    Signup()
def borrar():
    rootA.destroy()
 

    

#La ventana secundaria

    

def abrirventana():
    def atras():
            ventana.withdraw()
            ventana1.deiconify()
    ventana1.withdraw()
    roots.withdraw()

    ventana = tk.Tk()
    ventana.title("¿Qué estas buscando?")
    ventana.geometry('400x350')
    ventana.configure(background='medium aquamarine')
    etiqueta1 = tk.Label(ventana, text="Hola "+nameE.get()+", ¿Qué estas buscando?", bg='navy', fg='white')
    etiqueta1.pack(padx=20, pady=20, ipadx=20, ipady=20)
    
    # def de hospitales
    def abrir_hospitales():
        def atras():
            ventana2.withdraw()
            ventana.deiconify()
        ventana.withdraw()
        ventana2 = tk.Tk()
        ventana2.title("Hospitales")
        ventana2.geometry('400x370')
        ventana2.configure(background='medium aquamarine')
        etiqueta2 = tk.Label(ventana2, text="¿Buscas alguno en especial?, "+nameE.get(), bg='navy', fg='white')
        etiqueta2.pack(padx=20, pady=20, ipadx=20, ipady=20)

        def abrir_generales():
            a= folium.Map(location=[-12.143927, -77.019295], zoom_start=15)
            def Markers(lat,lon,label):
                fg=folium.FeatureGroup(name="Hospitales")
                fg.add_child(folium.Marker(location=[lat, lon],popup=label,icon=folium.Icon("red")))
                return fg
            data= pandas.read_csv("Base_Datos_Hospitales_Generales.txt")
            lat=list(data["Lat"])
            lon=list(data["Lon"])
            nombre=list(data["Hospital"])
            for lt,ln,est in zip(lat,lon,nombre):
                a.add_child(Markers(lt,ln,est))
            a.save("Hospitales generales.html")
            webbrowser.open("file:///C:/Proyecto_Mapa_ubicaciones/Hospitales%20generales.html", new=2, autoraise=True)

        def abrir_privados():
            a= folium.Map(location=[-12.143927, -77.019295], zoom_start=15)
            def Markers(lat,lon,label):
                fg=folium.FeatureGroup(name="Hospitales")
                fg.add_child(folium.Marker(location=[lat, lon],popup=label,icon=folium.Icon("red")))
                return fg
            data= pandas.read_csv("Base_Datos_Hospitales_Privados.txt")
            lat=list(data["Lat"])
            lon=list(data["Lon"])
            nombre=list(data["Hospital"])
            for lt,ln,est in zip(lat,lon,nombre):
                a.add_child(Markers(lt,ln,est))
            a.save("Hospitales privados.html")
                
            webbrowser.open("file:///C:/Proyecto_Mapa_ubicaciones/Hospitales%20privados.html", new=2, autoraise=True)

        def abrir_centros_de_salud():
            a= folium.Map(location=[-12.143927, -77.019295], zoom_start=15)
            def Markers(lat,lon,label):
                fg=folium.FeatureGroup(name="Hospitales")
                fg.add_child(folium.Marker(location=[lat, lon],popup=label,icon=folium.Icon("blue")))
                return fg
            data= pandas.read_csv("Base_Datos_Hospitales_Centros_De_Salud.txt")
            lat=list(data["Lat"])
            lon=list(data["Lon"])
            nombre=list(data["Hospital"])
            for lt,ln,est in zip(lat,lon,nombre):
                a.add_child(Markers(lt,ln,est))
            a.save("Hospitales centros de salud.html")
            webbrowser.open("file:///C:/Proyecto_Mapa_ubicaciones/Hospitales%20centros%20de%20salud.html", new=2,
                            autoraise=True)

        def abrir_en_otros_distritos():
            a= folium.Map(location=[-12.143927, -77.019295], zoom_start=15)
            def Markers(lat,lon,label):
                fg=folium.FeatureGroup(name="Hospitales")
                fg.add_child(folium.Marker(location=[lat, lon],popup=label,icon=folium.Icon("blue")))
            return fg
            data= pandas.read_csv("Base_Datos_Hospitales_En_Otros_Distritos.txt")
            lat=list(data["Lat"])
            lon=list(data["Lon"])
            nombre=list(data["Hospital"])
            for lt,ln,est in zip(lat,lon,nombre):
                a.add_child(Markers(lt,ln,est))
            a.save("Hospitales en otros distritos.html")
            webbrowser.open("file:///C:/Proyecto_Mapa_ubicaciones/Hospitales%20en%20otros%20distritos.html", new=2,
                            autoraise=True)


        Generales_button = tk.Button(ventana2, text="Generales", bg="white", fg="black", command=abrir_generales)
        Generales_button.config(width=18)
        Generales_button.pack(padx=2, pady=2, ipadx=1, ipady=1)

        Generales_button = tk.Button(ventana2, text="Privados", bg="white", fg="black", command=abrir_privados)
        Generales_button.config(width=18)
        Generales_button.pack(padx=2, pady=2, ipadx=1, ipady=1)

        Generales_button = tk.Button(ventana2, text="Centros de salud", bg="white", fg="black",
                                     command=abrir_centros_de_salud)
        Generales_button.config(width=18)
        Generales_button.pack(padx=2, pady=2, ipadx=1, ipady=1)

        Generales_button = tk.Button(ventana2, text="En otros distritos", bg="white", fg="black",
                                     command=abrir_en_otros_distritos)
        Generales_button.config(width=18)
        Generales_button.pack(padx=2, pady=2, ipadx=1, ipady=1)

        Generales_button = tk.Button(ventana2, text="Regresar", bg="black", fg="white",
                                     command=atras)
        Generales_button.config(width=18)
        Generales_button.pack(padx=2, pady=2, ipadx=1, ipady=1) 
        

        ventana2.mainloop()
    # Abrir la ventana de Hospitales
    e1= tk.Button(ventana, text="1. Hospitales", bg="sea green", fg="white", command=abrir_hospitales)
    e1.config(width=18)
    e1.pack(padx=2, pady=2, ipadx=1, ipady=1)
    # Definimos bancos
    def abrir_bancos():
        def atras():
            ventana4.withdraw()
            ventana.deiconify()
        ventana.withdraw()
        ventana4 = tk.Tk()
        ventana4.title("Bancos")
        ventana4.geometry('400x300')
        ventana4.configure(background='medium aquamarine')
        etiqueta1 = tk.Label(ventana4, text="¿Qué banco buscas?"+nameE.get(), bg='navy', fg='white')
        etiqueta1.pack(padx=20, pady=20, ipadx=20, ipady=20)
     
        def abrir_BN_BBVA_BCP():
            a= folium.Map(location=[-12.143927, -77.019295], zoom_start=15)
            def Markers(lat,lon,label):
                fg=folium.FeatureGroup(name="Bancos")
                fg.add_child(folium.Marker(location=[lat, lon],popup=label,icon=folium.Icon("red")))
                return fg
            data= pandas.read_csv("Base_Datos_Bancos_BBVA-BCP-BN.txt")
            lat=list(data["Lat"])
            lon=list(data["Lon"])
            nombre=list(data["Banco"])
            for lt,ln,est in zip(lat,lon,nombre):
                a.add_child(Markers(lt,ln,est))
            a.save("Bancos BBVA BCP BN.html")
            webbrowser.open("file:///C:/Proyecto_Mapa_ubicaciones/Bancos%20BBVA%20BCP%20BN.html", new=2, autoraise=True)

        def abrir_otros_bancos():
            a= folium.Map(location=[-12.143927, -77.019295], zoom_start=15)
            def Markers(lat,lon,label):
                fg=folium.FeatureGroup(name="Bancos")
                fg.add_child(folium.Marker(location=[lat, lon],popup=label,icon=folium.Icon("rosy brown")))
                return fg
            data= pandas.read_csv("Base_Datos_Bancos_otros_bancos.txt")
            lat=list(data["Lat"])
            lon=list(data["Lon"])
            nombre=list(data["Banco"])
            for lt,ln,est in zip(lat,lon,nombre):
                a.add_child(Markers(lt,ln,est))
            a.save("Bancos otros bancos.html")
            webbrowser.open("file:///C:/Proyecto_Mapa_ubicaciones/Bancos%20otros%20bancos.html", new=2, autoraise=True)

        def abrir_en_otros_distritos2():
            a= folium.Map(location=[-12.143927, -77.019295], zoom_start=15)
            def Markers(lat,lon,label):
                fg=folium.FeatureGroup(name="Bancos")
                fg.add_child(folium.Marker(location=[lat, lon],popup=label,icon=folium.Icon("blue")))
                return fg
            data= pandas.read_csv("Base_Datos_Bancos_en_otros_distritos.txt")
            lat=list(data["Lat"])
            lon=list(data["Lon"])
            nombre=list(data["Banco"])
            for lt,ln,est in zip(lat,lon,nombre):
                a.add_child(Markers(lt,ln,est))
            a.save("Bancos en otros distritos.html")
            webbrowser.open("file:///C:/Proyecto_Mapa_ubicaciones/Bancos%20en%20otros%20distritos.html", new=2,
                            autoraise=True)

        Generales_button = tk.Button(ventana4, text="BN/BBVA/BCP", bg="white", fg="black", command=abrir_BN_BBVA_BCP)
        Generales_button.config(width=18)
        Generales_button.pack(padx=2, pady=2, ipadx=1, ipady=1)

        Generales_button = tk.Button(ventana4, text="Otros bancos", bg="white", fg="black", command=abrir_otros_bancos)
        Generales_button.config(width=18)
        Generales_button.pack(padx=2, pady=2, ipadx=1, ipady=1)

        Generales_button = tk.Button(ventana4, text="En otros distritos", bg="white", fg="black",
                                     command=abrir_en_otros_distritos2)
        Generales_button.config(width=18)
        Generales_button.pack(padx=2, pady=2, ipadx=1, ipady=1)
        
        Generales_button = tk.Button(ventana4, text="Regresar", bg="black", fg="white",
                                     command=atras)
        Generales_button.config(width=18)
        Generales_button.pack(padx=2, pady=2, ipadx=1, ipady=1) 
        
        ventana4.mainloop()
    # Abrimos la ventana de bancos
    e2 = tk.Button(ventana, text="2. Bancos", bg='goldenrod', fg='white', command=abrir_bancos)
    e2.config(width=18)
    e2.pack(padx=2, pady=2, ipadx=1, ipady=1)
    # Definimos gasolinerias
    def abrir_gasolinerias():
        def atras():
            ventana5.withdraw()
            ventana.deiconify()
        ventana.withdraw()
        ventana5 = tk.Tk()
        ventana5.title("Gasolineras")
        ventana5.geometry('400x250')
        ventana5.configure(background='medium aquamarine')
        etiqueta1 = tk.Label(ventana5, text="Encuentra el mas cercano, "+nameE.get(), bg='navy', fg='white')
        etiqueta1.pack(padx=20, pady=20, ipadx=20, ipady=20)

        
        def abrir_mas_cercanos():
            a= folium.Map(location=[-12.143927, -77.019295], zoom_start=15)
            def Markers(lat,lon,label):
                fg=folium.FeatureGroup(name="Gasolinerias")
                fg.add_child(folium.Marker(location=[lat, lon],popup=label,icon=folium.Icon("blue")))
                return fg
            data= pandas.read_csv("Base_Datos_Gasolinerias_cerca.txt")
            lat=list(data["Lat"])
            lon=list(data["Lon"])
            nombre=list(data["Gasolineria"])
            for lt,ln,est in zip(lat,lon,nombre):
                a.add_child(Markers(lt,ln,est))
            a.save("Gasolinerias cerca.html")
            webbrowser.open("file:///C:/Proyecto_Mapa_ubicaciones/Gasolinerias%20cerca.html", new=2, autoraise=True)

        def abrir_en_otros_distritos3():
            a= folium.Map(location=[-12.143927, -77.019295], zoom_start=15)
            def Markers(lat,lon,label):
                fg=folium.FeatureGroup(name="Gasolinerias")
                fg.add_child(folium.Marker(location=[lat, lon],popup=label,icon=folium.Icon("blue")))
                return fg
            data= pandas.read_csv("Base_Datos_Gasolinerias_En_Otros_Distritos.txt")
            lat=list(data["Lat"])
            lon=list(data["Lon"])
            nombre=list(data["Gasolineria"])
            for lt,ln,est in zip(lat,lon,nombre):
                a.add_child(Markers(lt,ln,est))
            a.save("Gasolinerias en otros distritos.html")
            webbrowser.open("file:///C:/Proyecto_Mapa_ubicaciones/Gasolinerias%20en%20otros%20distritos.html", new=2,
                            autoraise=True)

        Generales_button = tk.Button(ventana5, text="Más cercanos", bg="white", fg="black", command=abrir_mas_cercanos)
        Generales_button.config(width=18)
        Generales_button.pack(padx=2, pady=2, ipadx=1, ipady=1)

        Generales_button = tk.Button(ventana5, text="En otros distritos", bg="white", fg="black",
                                     command=abrir_en_otros_distritos3)
        Generales_button.config(width=18)
        Generales_button.pack(padx=2, pady=2, ipadx=1, ipady=1)

        Generales_button = tk.Button(ventana5, text="Regresar", bg="black", fg="white",
                                     command=atras)
        Generales_button.config(width=18)
        Generales_button.pack(padx=2, pady=2, ipadx=1, ipady=1) 
        
        ventana5.mainloop()
    #Abrimos ventana de gasolineria
    e4 = tk.Button(ventana, text="3. Gasolineras", bg='firebrick', fg='white', command=abrir_gasolinerias)
    e4.config(width=18)
    e4.pack(padx=3, pady=3, ipadx=1, ipady=1)
    # Definimos hoteles
    def abrir_hoteles():
        def atras():
            ventana6.withdraw()
            ventana.deiconify()
        ventana.withdraw()
        ventana6 = tk.Tk()
        ventana6.title("Hoteles")
        ventana6.geometry('400x370')
        ventana6.configure(background='medium aquamarine')
        etiqueta1 = tk.Label(ventana6, text="¿Cual es tu eleccion?"+nameE.get(), bg='navy', fg='white')
        etiqueta1.pack(padx=20, pady=20, ipadx=20, ipady=20)
 
        def abrir_1a3():
            a= folium.Map(location=[-12.143927, -77.019295], zoom_start=15)
            def Markers(lat,lon,label):
                fg=folium.FeatureGroup(name="Hoteles")
                fg.add_child(folium.Marker(location=[lat, lon],popup=label,icon=folium.Icon("blue")))
                return fg
            data= pandas.read_csv("Base_Datos_Hoteles 1-3.txt")
            lat=list(data["Lat"])
            lon=list(data["Lon"])
            nombre=list(data["Hotel"])
            for lt,ln,est in zip(lat,lon,nombre):
                a.add_child(Markers(lt,ln,est))
            a.save("Hoteles 1-3.html")
            webbrowser.open("file:///C:/Proyecto_Mapa_ubicaciones/Hoteles%201-3.html", new=2, autoraise=True)

        def abrir_4a5():
            a= folium.Map(location=[-12.143927, -77.019295], zoom_start=15)
            def Markers(lat,lon,label):
                fg=folium.FeatureGroup(name="Hoteles")
                fg.add_child(folium.Marker(location=[lat, lon],popup=label,icon=folium.Icon("blue")))
                return fg
            data= pandas.read_csv("Base_Datos_Hoteles 4-5.txt")
            lat=list(data["Lat"])
            lon=list(data["Lon"])
            nombre=list(data["Hotel"])
            for lt,ln,est in zip(lat,lon,nombre):
                a.add_child(Markers(lt,ln,est))
            a.save("Hoteles 4-5.html")
            webbrowser.open("file:///C:/Proyecto_Mapa_ubicaciones/Hoteles%204-5.html", new=2, autoraise=True)

        def abrir_mejores_valoraciones():
            a= folium.Map(location=[-12.143927, -77.019295], zoom_start=15)
            def Markers(lat,lon,label):
                fg=folium.FeatureGroup(name="Hoteles")
                fg.add_child(folium.Marker(location=[lat, lon],popup=label,icon=folium.Icon("blue")))
                return fg
            data= pandas.read_csv("Base_Datos_Hoteles_mejores_valoraciones.txt")
            lat=list(data["Lat"])
            lon=list(data["Lon"])
            nombre=list(data["Hotel"])
            for lt,ln,est in zip(lat,lon,nombre):
                a.add_child(Markers(lt,ln,est))
            a.save("Hoteles mejores valoraciones.html")
            webbrowser.open("file:///C:/Proyecto_Mapa_ubicaciones/Hoteles%20mejores%20valoraciones.html", new=2,
                            autoraise=True)

        def abrir_en_otros_distritos4():
            a= folium.Map(location=[-12.143927, -77.019295], zoom_start=15)
            def Markers(lat,lon,label):
                fg=folium.FeatureGroup(name="Hoteles")
                fg.add_child(folium.Marker(location=[lat, lon],popup=label,icon=folium.Icon("blue")))
                return fg
            data= pandas.read_csv("Base_Datos_Hoteles_en_otros_distritos.txt")
            lat=list(data["Lat"])
            lon=list(data["Lon"])
            nombre=list(data["Hotel"])
            for lt,ln,est in zip(lat,lon,nombre):
                a.add_child(Markers(lt,ln,est))
            a.save("Hoteles en otros distritos.html")
            webbrowser.open("file:///C:/Proyecto_Mapa_ubicaciones/Hoteles%20en%20otros%20distritos.html", new=2,
                            autoraise=True)

        Generales_button = tk.Button(ventana6, text="* a ***", bg="white", fg="black", command=abrir_1a3)
        Generales_button.config(width=18)
        Generales_button.pack(padx=2, pady=2, ipadx=1, ipady=1)

        Generales_button = tk.Button(ventana6, text="**** a *****", bg="white", fg="black", command=abrir_4a5)
        Generales_button.config(width=18)
        Generales_button.pack(padx=2, pady=2, ipadx=1, ipady=1)

        Generales_button = tk.Button(ventana6, text="Mejores valoraciones", bg="white", fg="black",
                                     command=abrir_mejores_valoraciones)
        Generales_button.config(width=18)
        Generales_button.pack(padx=2, pady=2, ipadx=1, ipady=1)

        Generales_button = tk.Button(ventana6, text="En otros distritos", bg="white", fg="black",
                                     command=abrir_en_otros_distritos4)
        Generales_button.config(width=18)
        Generales_button.pack(padx=2, pady=2, ipadx=1, ipady=1)

        Generales_button = tk.Button(ventana6, text="Regresar", bg="black", fg="white",
                                     command=atras)
        Generales_button.config(width=18)
        Generales_button.pack(padx=2, pady=2, ipadx=1, ipady=1)
        
        ventana6.mainloop()
    # Abrimos ventana de hoteles
    e5 = tk.Button(ventana, text="4. Hoteles", bg='steel blue', fg='white',command=abrir_hoteles)
    e5.config(width=18)
    e5.pack(padx=5, pady=5, ipadx=2, ipady=2)
    e7 = tk.Button(ventana, text="Volver a MENU", bg="black", fg="white",
                                     command=atras)
    e7.config(width=18)
    e7.pack(padx=2, pady=2, ipadx=1, ipady=1) 
    ventana.mainloop()

# Aabrir la ventana principal
ventana1 = tk.Tk()
ventana1.geometry("498x281")
ventana1.title("Barrranco view - Entrada")
# Imagen de fondo
imagen_de_fondo = PhotoImage(file="fondofinal.gif")
lbldelaimagen1 = tk.Label(ventana1, image=imagen_de_fondo).place(x=0, y=0)

# Boton para entrar
Boton_pa_entrar = tk.Button(ventana1, text="Ingresar", font=("Times New Roman", 14), bg="snow", fg="black",
                            command=Login).place(x=209, y=190)
Boton_para_crear = tk.Button(ventana1, text="Registrate", font=("Times New Roman", 12), bg="snow", fg="black",
                            command=Signup).place(x=10, y=10)
ventana1.mainloop()



