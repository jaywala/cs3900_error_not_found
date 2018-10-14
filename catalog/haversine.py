#------------------------------------------------------------------------------+
#
#   Written by: Nathan A. Rooy
#   Adapted for COMP3900 project
#   Haversine Formula
#   June, 2016
#   https://github.com/nathanrooy/spatial-analysis/blob/master/haversine.py
#
#------------------------------------------------------------------------------+

import math

def haversine(coord1,coord2):
    '''
    The haversine method to calculates the distance between
    two long/lat coordnate pairs.
    Output distance available in kilometers, meters, miles, and feet.
    However, this method returns distance in kilometers.
    Example use: haversine([lon1,lat1],[lon2,lat2])
                or
                 haversine((lon1,lat1),(lon2,lat2))
    '''

    lon1,lat1=coord1
    lon2,lat2=coord2

    R=6371000                               # radius of Earth in meters
    phi_1=math.radians(lat1)
    phi_2=math.radians(lat2)

    delta_phi=math.radians(lat2-lat1)
    delta_lambda=math.radians(lon2-lon1)

    a=math.sin(delta_phi/2.0)**2+\
       math.cos(phi_1)*math.cos(phi_2)*\
       math.sin(delta_lambda/2.0)**2
    c=2*math.atan2(math.sqrt(a),math.sqrt(1-a))

    meters=R*c                         # output distance in meters
    km=meters/1000.0              # output distance in kilometers
    #miles=smeters*0.000621371      # output distance in miles
    #feet=miles*5280               # output distance in feet

    return km
