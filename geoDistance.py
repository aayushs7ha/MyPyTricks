#always better to convert lat/long columns to radians
df['Lat'] = np.radians(df['Lat'])
df['Long'] = np.radians(df['Long'])
df['gpsLatitude'] = np.radians(df['gpsLatitude'])
df['gpslongitude'] = np.radians(df['gpslongitude'])


import geopy
def distance(row):
    return geopy.distance.distance((row.Lat, row.Long),(row.gpsLatitude,row.gpslongitude)).meters
	
df['Distance'] = df.apply(lambda r: distance(r),axis = 1)