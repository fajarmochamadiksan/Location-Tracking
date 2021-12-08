import geocoder
import folium

geolocation = geocoder.ip("180.251.183.74")
myAddress = g.latlng
mymap1 = folium.Map(location=myAddress,zoom_start=12)

#Output
my_map1.save("my_map.html")
