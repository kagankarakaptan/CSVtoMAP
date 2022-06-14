from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import pandas as pd

# veriler alındı sample dataya konuldu
sample_data = pd.read_csv('ais.csv')

# tekrarlar silindi gemi olmayan veriler silindi
dota = sample_data.drop_duplicates(subset=["CallSign"], keep='last')
for x in dota.index:
    if(len(str(dota.MMSI[x])) != 9):
        dota = dota.drop(index=x)
dota.plot.scatter(x="DimA", y="ShipandCargo",)
plt.show()

#harita sınırıları çizildi
m = Basemap(projection="mill",
            llcrnrlat=40.1642,
            llcrnrlon=26.6446,
            urcrnrlat=41.2324,
            urcrnrlon=28.8995,
            resolution="l")

#denizler göller karadan ayrıldı(musa the great lake divider and divisioner)
m.drawcoastlines(linewidth=0.5)
m.drawmapboundary(fill_color="aqua")
m.fillcontinents(color="coral", lake_color="aqua")

#pozisyonlar çekildi
for x in dota.index:
    lon=dota.Lon[x]
    lat=dota.Lat[x]
    xpt, ypt = m(lon, lat)
    m.plot(xpt, ypt, "co", markersize=2, color= "red")


#haritada gösterim başarı ile ifa edildi
plt.title("Çanakkale")
plt.show()


# 39,26,41,25
