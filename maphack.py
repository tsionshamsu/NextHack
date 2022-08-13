import folium
import pandas

data = pandas.read_excel("ngos.xlsx", sheet_name=1)

lat = list(data["Lat"])
lon = list(data["Long"])
pcode = list(data["PCODE"])
place = list(data["Name"])

samdata = pandas.read_excel("sam-data.xlsx")

woredapcode = list(samdata["Woreda P-Code"])
woreda = list(samdata["Woreda"])
maycum = list(samdata["May Cum"])
 
html = """
Place name:<br>
<a href="https://www.google.com/search?q=%%22%s%%22" target="_blank">%s</a><br>
PCODE: %s 
"""



map = folium.Map(location = [9, 38.7], zoom_start=6, tiles = "Stamen Terrain")
fgngos = folium.FeatureGroup("NGOs")

for lt, ln, el, name in zip(lat, lon, pcode, place):
    iframe = folium.IFrame(html=html % (name, name, el), width=200, height=100)
    fgngos.add_child(folium.CircleMarker(location=[lt, ln], popup= folium.Popup(iframe), radius = 6,  fill_color= "red", fill_opacity = 0.7))



def cool(numofsam):
    if numofsam < 200:
        return "darkgreen"
    elif numofsam > 200 and numofsam < 400:
        return "orange"
    else:
        return "red"

fgsam = folium.FeatureGroup("Severe Acute Malnutrition")

for place, lt, ln, cumulative in zip(woreda, lat, lon,  maycum):
    iframe = folium.IFrame(html=html % (place, place, cumulative), width=200, height=100)
    fgsam.add_child(folium.CircleMarker(location=[lt, ln], popup= folium.Popup(iframe), radius = 6,  fill_color= cool(cumulative), fill_opacity = 0.7))




# fgsam.add_child(folium.GeoJson(data= open("world.json", "r", encoding = "utf-8-sig").read(), 
# style_function= lambda x: { "fillColor": "yellow" if x["properties"]["POP2005"] < 10000000 
# else "orange" if  10000000<= x["properties"]["POP2005"] <= 20000000 else "red"} ))


map.add_child(fgngos)
map.add_child(fgsam)
map.add_child(folium.LayerControl())
map.save("ethmap.html")