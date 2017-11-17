import folium
import pandas


a= folium.Map(location=[-12.143927, -77.019295])

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
