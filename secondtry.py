import osgeo.gdal as gdal
import osgeo.osr as osr
import numpy as np
from numpy import ma
geotifAddr="C:\Users\smadhu\Desktop\madhu\New Journey\elevation.bmp"
def maFromGDAL(filename):
 dataset = gdal.Open(filename, gdal.GA_ReadOnly)
 geotransform = dataset.GetGeoTransform()
 band = dataset.GetRasterBand(1)
 # We need to nodata value for our MaskedArray later.
 nodata = band.GetNoDataValue()
 # Load the entire dataset into one numpy array.
 image = band.ReadAsArray(0, 0, band.XSize, band.YSize)
 # Close the dataset.
 dataset = None
 # Create a numpy MaskedArray from our regular numpy array.
 # If we want to be really clever, we could subclass MaskedArray to hold
 # our georeference metadata as well.
 # see here: http://docs.scipy.org/doc/numpy/user/basics.subclassing.html
 # For details.
 masked_image = ma.masked_values(image, nodata, copy=False)
 masked_image.fill_value = nodata
 return masked_image, geotransform

def pixelToMap(gt, pos):
 return (gt[0] + pos[0] * gt[1] + pos[1] * gt[2],gt[3] + pos[0] * gt[4] + pos[1] * gt[5])

def mapToPixel(gt, pos):
 return (-(gt[0] + pos[1] * gt[2]) / gt[1], -(gt[3] + pos[0] * gt[5]) / gt[4])

def valueAtMapPos(image, gt, pos):
 pp = mapToPixel(gt, pos)
 x = int(pp[0])
 y = int(pp[1])
 return image[y, x]

try:
 image, geotransform = maFromGDAL(geotifAddr)
 val = valueAtMapPos(image, geotransform, (434323.0, 2984745.0))
 print val
except:
 print('Something went wrong.')