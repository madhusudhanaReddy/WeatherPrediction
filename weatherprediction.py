#!/usr/bin/env python
# encoding: utf-8

from osgeo import gdal
from osgeo import osr
latLonPairs=[[-34.92,138.62],[-33.86,151.21]]
geotifAddr="C:\Users\smadhu\Desktop\madhu\New Journey\elevation.bmp"

def latLonToPixel(geotifAddr, latLonPairs):
	# Load the image dataset
	ds = gdal.Open(geotifAddr)
	# Get a geo-transform of the dataset
	gt = ds.GetGeoTransform()
	# Create a spatial reference object for the dataset
	srs = osr.SpatialReference()
	srs.ImportFromWkt(ds.GetProjection())
	# Set up the coordinate transformation object
	srsLatLong = srs.CloneGeogCS()
	ct = osr.CoordinateTransformation(srsLatLong,srs)
	# Go through all the point pairs and translate them to latitude/longitude pairings
	pixelPairs = []
	for point in latLonPairs:
		# Change the point locations into the GeoTransform space
		(point[1],point[0],holder) = ct.TransformPoint(point[1],point[0])
		# Translate the x and y coordinates into pixel values
		x = (point[1]-gt[0])/gt[1]
		y = (point[0]-gt[3])/gt[5]
		# Add the point to our return array
		pixelPairs.append([int(x),int(y)])
	return pixelPairs
	

latLonPairs=[[-34.92,138.62],[-33.86,151.21]]
latLonToPixel(geotifAddr,latLonPairs)


#ds = gdal.Open('C:\Users\smadhu\Desktop\madhu\New Journey\elevation.bmp')
#ds = gdal.Open('C:\Users\smadhu\Desktop\madhu\New Journey\gebco_08_rev_elev_A1_grey_geo.tif')


from osgeo import gdal
from osgeo import osr
latLonPairs=[[-34.92,138.62],[-33.86,151.21]]
geotifAddr="C:\Users\smadhu\Desktop\madhu\New Journey\elevation.bmp"
pixelPairs=[[1,2],[3,4]]
def pixelToLatLon(geotifAddr,pixelPairs):
     # Load the image dataset
     #ds = gdal.Open(geotifAddr)
     ds = gdal.Open('C:\Users\smadhu\Desktop\madhu\New Journey\elevation.bmp')
     #ds = gdal.Open('C:\Users\smadhu\Desktop\madhu\New Journey\gebco_08_rev_elev_A1_grey_geo.tif')
     # Get a geo-transform of the dataset
     gt = ds.GetGeoTransform()
     # Create a spatial reference object for the dataset
     srs = osr.SpatialReference()
     srs.ImportFromWkt(ds.GetProjection())
     # Set up the coordinate transformation object
     srsLatLong = srs.CloneGeogCS()
     ct = osr.CoordinateTransformation(srs,srsLatLong)
     # Go through all the point pairs and translate them to pixel pairings
     latLonPairs = []
     for point in pixelPairs:
         # Translate the pixel pairs into untranslated points
         ulon = point[0]*gt[1]+gt[0]
         ulat = point[1]*gt[5]+gt[3]
         # Transform the points to the space
         (lon,lat,holder) = ct.TransformPoint(ulon,ulat)
         # Add the point to our return array
         latLonPairs.append([lat,lon])
     return latLonPairs
	
	
	
pixelToLatLon(geotifAddr,pixelPairs)





