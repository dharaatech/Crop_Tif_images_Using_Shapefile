import numbers
from osgeo import gdal
import natsort as natsorted
import glob
import os
from natsort import natsorted

shp_dir = 'vectors'

shp_lst = natsorted(list(glob.glob(os.path.join(shp_dir, '**/*.shp'))))

shp_lst = natsorted(list(glob.glob(os.path.join(shp_dir, '**/*.shp')))) # for folder
print(shp_lst)


out_path = "cropout"




for i in range(0, len(shp_lst)):
    
    n = i+1
    n=str(n)
    rasin = "PS150321RUDOK0_5.tif"
    output = "cropout/" + n + ".tif"
    
    shpin = shp_lst[i]

    gdal.Warp(output, rasin, cutlineDSName = shpin, format="GTiff", cropToCutline = True)
