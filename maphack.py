import folium
import pandas

data = pandas.read_excel("./nexthack/ngos.xlsx", sheet_name=1)
# ngoNameData = pandas.read_excel("./nexthack/ngos.xlsx",sheet_name=0)
lat = list(data["Lat"])
lon = list(data["Long"])
pcode = list(data["PCODE"])
place = list(data["Name"])
# ngoName = list(ngoNameData["Implementing agency Name"])
samdata = pandas.read_excel("./nexthack/sam-data.xlsx")

woredapcode = list(samdata["Woreda P-Code"])
woreda = list(samdata["Woreda"])
maycum = list(samdata["May Cum"])

# NEW ADDITIONS
ngoNameData = pandas.read_excel("nexthack/ngos.xlsx",sheet_name=0, skiprows = [1])
ngoacr = ngoNameData.loc[:, "Implementing agency Acronym"]
ngotyp = ngoNameData.loc[:, "Programme Organization Type"]
ngo = ngoacr + " , "+ ngotyp
ngo

 
html = """
Place name:<br>
<a href="https://www.google.com/search?q=%s" target="_blank">%s</a><br>
NGO Name: %s
<a href="https://www.google.com/search?q=Ethiopia %s" target="_blank">%s</a><br>
<a href="https://www.google.com/maps/search/?api=1&query=%s,%s" target="_blank">NGO Address</a><br>
PCODE: %s 
Cumulative: %s 
"""
 
def cool(numofsam):
    if numofsam < 200:
        return "darkgreen"
    elif numofsam > 200 and numofsam < 400:
        return "orange"
    else:
        return "red"


map = folium.Map(location = [9, 38.7], zoom_start=6, tiles = "Stamen Terrain")
fgngos = folium.FeatureGroup("NGOs")

for lt, ln, el, name,maycum,ngo in zip(lat, lon, pcode, place,maycum,ngo):
    iframe = folium.IFrame(html=html % (name, name, ngo, ngo, ngo,lt,ln, el, maycum), width=200, height=300)
    fgngos.add_child(folium.CircleMarker(location=[lt, ln], popup= folium.Popup(iframe), radius = 6,  fill_color= cool(maycum), fill_opacity = 0.7))



# fgsam = folium.FeatureGroup("Severe Acute Malnutrition")

# for place, lt, ln, cumulative in zip(woreda, lat, lon,  maycum):
#     iframe = folium.IFrame(html=html % (place, place, cumulative), width=200, height=100)
#     fgsam.add_child(folium.CircleMarker(location=[lt, ln], popup= folium.Popup(iframe), radius = 6,  fill_color= cool(cumulative), fill_opacity = 0.7))




# fgsam.add_child(folium.GeoJson(data= open("world.json", "r", encoding = "utf-8-sig").read(), 
# style_function= lambda x: { "fillColor": "yellow" if x["properties"]["POP2005"] < 10000000 
# else "orange" if  10000000<= x["properties"]["POP2005"] <= 20000000 else "red"} ))


map.add_child(fgngos)
# map.add_child(fgsam)
map.add_child(folium.LayerControl())
map.save("./nexthack/ethmap.html")