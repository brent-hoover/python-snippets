#!/usr/bin/env python

import math

def haversine(lat1, lon1, lat2, lon2):
  R = 6372800
  # In meters
  dLat = math.radians(lat2 - lat1)
  dLon = math.radians(lon2 - lon1)
  lat1 = math.radians(lat1)
  lat2 = math.radians(lat2)

  a = math.sin(dLat / 2) * math.sin(dLat / 2) + math.sin(dLon / 2) * math.sin(dLon / 2) * math.cos(lat1) * math.cos(lat2)
  c = 2 * math.asin(math.sqrt(a))
  return R * c

if __name__ == '__main__':
    lat1 = 34.091510
    lon1 = -118.364829
    lat2 = 64.806881
    lon2 = -18.083496
    print(haversine(lat1, lon1, lat2, lon2))
    