#SE IMPORTAN LAS LIBRERIAS NECESARIAS
import folium
import pandas as pd
#CON PANDAS SE LEE EL ARCHIVO CON EXTENCION CSV EN EL QUE SE ENCUENTRAN LAS COORDENADAS 
df=pd.read_csv("Coordenadas.csv")
#CREAMOS EL MAPA CON LALIBRERIA DE FOLIUM CON LA FUNCION MAP
map=folium.Map(location=[df["LAT"].mean(),df["LON"].mean()],zoom_start=20)
#ASIGNAMOS LA EDICION DEL MAPA EN UN GRUPO
fg=folium.FeatureGroup(name="luminaria")
#CREAMOS UNA VARIABLE PARA ASIGNAR COLOR SOLO A LOS PUNTOS CON CARACTERISTICAS DIFERENTES
marcador1 = folium.Marker(
    location=([df["LAT"].mean(),df["LON"].mean()]),
    popup=folium.Popup(df["COLOR"], max_width=500),
    icon=folium.Icon(color="black"))
#UTILIZAMOS UN CICLO PARA PODER ASIGNAR UN MARCADOR INDEPENDIENTE POR  CADA FILA DEL ARCHIVO CSV
for lat,lon,caracteristicas, in zip(df["LAT"],df["LON"],df["CARACTERISTICAS"]):
    fg.add_child(folium.Marker(location=[lat,lon],popup=(folium.Popup(caracteristicas))))
map.add_child(fg)
#GUARDAMOS EL MAPA CON EXTENCION HTML
map.save(outfile="Luminarias.html")
