#!/usr/bin/env python
# encoding: utf-8

"""
Created on 05 july 2016

@author: Madhu
"""

# A python program which used some publically available
# web apis to find out what the forecast will be.
#
 
#API="PUT_YOUR_OWN_API_KEY_HERE"

API="763114e12219eede5f8f26120bdf4124"
URL="https://api.forecast.io/forecast/"
 
import sys
import os
import time
import json
import urllib2
from geopy.geocoders import Nominatim
geolocator = Nominatim()
now = time.time()

# SRC OF GEOGRAPHY 

SRC=[(+57.09700,+9.85000),(+13.80000,+77.30000),(+28.90000,+77.21670 ),(+36.09500,-115.04200),(+13.80000,+77.30000),(-23.43330,-70.60000),(-36.88320,+174.75000),(+51.50000,-0.11670),(+47.36670,+8.53330),(+52.70000,-8.91700),(+2.35000,+111.83330),(-33.91660,+151.28330),(+32.36700,-64.68300)]


for i in SRC :
 location = geolocator.reverse((i))
 (LAT,LNG)=location[1]
 req = urllib2.Request(URL+API+"/"+("%f,%f"%(LAT,LNG)))
 response = urllib2.urlopen(req)
 parsed = json.loads(response.read())
 c = parsed["currently"]
 print "\n ======= Reporting location ::: ==========\n"
 print "::: Location :",location[0]
 print ":::LAT ,LNG",location[1]
 print ":::",time.localtime(c["time"])
 print "::: Conditions:", c["summary"]
 print "::: Temperature:", ("%.1f" % c["temperature"])+u"\u00B0"
 print "::: Pressure:", ("%.1f" % c["pressure"])+u"\u00B0"
 print "::: Humidity:", ("%4.1f%%" % (c["humidity"]*100.))
 d = parsed["daily"]["data"][0]
 print "::: High:", ("%.1f" % d["temperatureMax"])+u"\u00B0"
 print "::: Low:", ("%.1f" % d["temperatureMin"])+u"\u00B0"
 
	
		