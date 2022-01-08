import rasterio as rio
import rasterio.plot as rioplt
import matplotlib.pyplot as plt
from shapely import ops as shpops
import pyproj
import geopandas as gpd
import pandas as pd
import numpy


# Graphing 2020
raster = rio.open('C:\\Users\\kevin\\OneDrive\\Documents\\CSC_486_DataMiningMethods\\DataMiningProject3Folder\\polygonclip\\CDL_2020_clip_20211207232419_873250894.tif')
rioplt.show(raster)



bar2020 = raster.read(1)
(unique, counts) = numpy.unique(bar2020, return_counts=True)
count = numpy.asarray((unique, counts)).T
df2020 = pd.DataFrame(data = count, columns = ['value', 'Count'])

plt.bar(df2020['value'], df2020['Count'])
plt.title('Pixel Count for 2020')
plt.xlabel('Values')
plt.ylabel('Count')
plt.show()

#Graphing 2016
raster2016 = rio.open('C:\\Users\\kevin\\OneDrive\\Documents\\CSC_486_DataMiningMethods\\DataMiningProject3Folder\\polygonclip\\CDL_2016_clip_20211207232419_873250894.tif')
rioplt.show(raster2016)

bar2016 = raster2016.read(1)
(unique, counts) = numpy.unique(bar2016, return_counts=True)
count = numpy.asarray((unique, counts)).T
df2016 = pd.DataFrame(data = count, columns = ['value', 'Count'])

plt.bar(df2016['value'], df2016['Count'])
plt.title('Pixel Count for 2016')
plt.xlabel('Values')
plt.ylabel('Count')
plt.show()

#Graphing 2012
raster2012 = rio.open('C:\\Users\\kevin\\OneDrive\\Documents\\CSC_486_DataMiningMethods\\DataMiningProject3Folder\\polygonclip\\CDL_2012_clip_20211207232419_873250894.tif')
rioplt.show(raster2012)

bar2012 = raster2012.read(1)
(unique, counts) = numpy.unique(bar2016, return_counts=True)
count = numpy.asarray((unique, counts)).T
df2012 = pd.DataFrame(data = count, columns = ['value', 'Count'])

plt.bar(df2012['value'], df2012['Count'])
plt.title('Pixel Count for 2012')
plt.xlabel('Values')
plt.ylabel('Count')
plt.show()

#Graphing 2008
raster2008 = rio.open('C:\\Users\\kevin\\OneDrive\\Documents\\CSC_486_DataMiningMethods\\DataMiningProject3Folder\\polygonclip\\CDL_2012_clip_20211207232419_873250894.tif')
rioplt.show(raster2008)

bar2008 = raster2008.read(1)
(unique, counts) = numpy.unique(bar2008, return_counts=True)
count = numpy.asarray((unique, counts)).T
df2008 = pd.DataFrame(data = count, columns = ['value', 'Count'])

plt.bar(df2008['value'], df2008['Count'])
plt.title('Pixel Count for 2008')
plt.xlabel('Values')
plt.ylabel('Count')
plt.show()

#Graphing 2004
raster2004 = rio.open('C:\\Users\\kevin\\OneDrive\\Documents\\CSC_486_DataMiningMethods\\DataMiningProject3Folder\\polygonclip\\CDL_2012_clip_20211207232419_873250894.tif')
rioplt.show(raster2004)

bar2004 = raster2004.read(1)
(unique, counts) = numpy.unique(bar2008, return_counts=True)
count = numpy.asarray((unique, counts)).T
df2004 = pd.DataFrame(data = count, columns = ['value', 'Count'])

plt.bar(df2004['value'], df2004['Count'])
plt.title('Pixel Count for 2004')
plt.xlabel('Values')
plt.ylabel('Count')
plt.show()

# In all graphs Value 1 (Corn) is the largest land usage folling is 5 (soybeans), 176 (Grass/Pastures), 121 (Developed/open space), 142 (Decideous Forest )

counties_gdf = gpd.read_file('C:\\Users\\kevin\\OneDrive\\Documents\\CSC_486_DataMiningMethods\\DataMiningProject3Folder\\cb_2018_us_county_5m\\cb_2018_us_county_5m.shp')
Iowacountiesgdf = counties_gdf[counties_gdf['STATEFP'] == '19']
BHgdf = Iowacountiesgdf[Iowacountiesgdf['NAME'] == 'Black Hawk']
Butlergdf = Iowacountiesgdf[Iowacountiesgdf['NAME'] == 'Butler']
Frankgdf = Iowacountiesgdf[Iowacountiesgdf['NAME'] == 'Franklin']
Carrollgdf = Iowacountiesgdf[Iowacountiesgdf['NAME'] == 'Carroll']
Webgdf = Iowacountiesgdf[Iowacountiesgdf['NAME'] == 'Webster']


BHgdf['geometry'].plot()
Butlergdf['geometry'].plot()
Frankgdf['geometry'].plot()
Carrollgdf['geometry'].plot()
Webgdf['geometry'].plot()



wgs84 = pyproj.CRS('EPSG: 4326')
img_crs = pyproj.CRS(str(raster.crs))
project_func = pyproj.Transformer.from_crs(wgs84, img_crs, always_xy=True).transform
BlackHawkcnt = shpops.transform(project_func, BHgdf['geometry'].all())
Butlercnt = shpops.transform(project_func, Butlergdf['geometry'].all())
Frankcnt = shpops.transform(project_func, Frankgdf['geometry'].all())
Carrollcnt = shpops.transform(project_func, Carrollgdf['geometry'].all())
Webstercnt = shpops.transform(project_func, Webgdf['geometry'].all())

#Creating Boarders for each County
fig = plt.figure()
ax = fig.add_subplot(1,1,1)
rioplt.show(raster, ax = ax)
ext_x = [pt[0] for pt in list( BlackHawkcnt.exterior.coords)]
ext_y = [pt[1] for pt in list( BlackHawkcnt.exterior.coords)]
ax.plot(ext_x, ext_y, '-m')
ext_x = [pt[0] for pt in list( Butlercnt.exterior.coords)]
ext_y = [pt[1] for pt in list( Butlercnt.exterior.coords)]
ax.plot(ext_x, ext_y, '-r')
ext_x = [pt[0] for pt in list( Frankcnt.exterior.coords)]
ext_y = [pt[1] for pt in list( Frankcnt.exterior.coords)]
ax.plot(ext_x, ext_y, '-y')
ext_x = [pt[0] for pt in list( Carrollcnt.exterior.coords)]
ext_y = [pt[1] for pt in list( Carrollcnt.exterior.coords)]
ax.plot(ext_x, ext_y, '-c')
ext_x = [pt[0] for pt in list( Webstercnt.exterior.coords)]
ext_y = [pt[1] for pt in list( Webstercnt.exterior.coords)]
ax.plot(ext_x, ext_y, '-w')
fig.show()


#Computing the area for each county in square meters

print("Area of Black Hawk")
BlackHawkarea = shpops.transform(project_func, BHgdf['geometry'].all()).area
print(BlackHawkarea)
print("Area of Butler")
Butlerarea =  shpops.transform(project_func, Butlergdf['geometry'].all()).area
print(Butlerarea)
print("Area of Frank")
Frankarea = shpops.transform(project_func, Frankgdf['geometry'].all()).area
print(Frankarea)
print("Area of Carroll")
Carrollarea =  shpops.transform(project_func, Carrollgdf['geometry'].all()).area
print(Carrollarea)
print("Area of Webster")
Websterarea = shpops.transform(project_func, Webgdf['geometry'].all()).area
print(Websterarea)

px_vals = []
band_id = 1
band_arr = raster.read(band_id)
for x in range(band_arr.shape[0]):
    for y in range(band_arr.shape[1]):
        px_vals.append({'x': x, 
                       'y': y,
                        'value': band_arr[x, y]})
pixelpointsdf = pd.DataFrame(data = px_vals, columns = ['x', 'y', 'value'])

