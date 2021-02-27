

import folium 
from folium.features import DivIcon


AntalyaE,AntalyaB = 36.89, 30.70 
AnkaraE, AnkaraB = 39.92, 32.85
AntalyaAnkaraMesafe = 485 # antalya ankara arası 485 km

haritaMap = folium.Map(location = [37, 30.4099794], 
                                        zoom_start = 5) 
folium.Marker([AntalyaE,AntalyaB], 
              popup = 'ANTALYA',
              ).add_to(haritaMap) 

folium.Marker([AnkaraE, AnkaraB], 
              popup = 'ANKARA').add_to(haritaMap) 
  
  
folium.PolyLine(locations = [(AnkaraE, AnkaraB), (AntalyaE, AntalyaB)], 
                line_opacity = 0.5).add_to(haritaMap) 

# Display POI Name
folium.map.Marker(location=(39,32), icon=DivIcon(
    #icon_size=(150, 36),
    icon_anchor=(0, 0),
    html='<div style="font-size: 16pt; color: blue">{}</div>'.format("Ankara Antalya Mesafe" + str(AntalyaAnkaraMesafe) + "KM")
)).add_to(haritaMap)


haritaMap.save("haritaMapCizgiMesafe.html") 
