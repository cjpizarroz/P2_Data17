import folium
import webbrowser

longuitud = -58.475340
latitud = -34.687570
coordenada_centrar = [latitud, longuitud ]
mymap = folium.Map(
    location = coordenada_centrar,
    titles = 'OpenStreetMap ',
    zoom_start = 50
);

#lnicio de marcador
feature_group = folium.FeatureGroup(name =  'BsAs')
folium.Marker(location= coordenada_centrar).add_to(feature_group)
mymap.add_child(feature_group)
mymap.add_child(folium.map.LayerControl())
#Fin del marcador
#guardar
archivoHtml= 'lagoChinchaycocha.html' ;
mymap.save(archivoHtml)
#abrir en el navegador automaticamente
#utiliza el navegador por defecto
webbrowser.open(archivoHtml)