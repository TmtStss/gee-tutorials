from os import path, makedirs
import ee
import geemap

def get_square_centroid(feature, edge = 100):
    # Get the centroid of the feature's geometry.
    centroid = feature.geometry().centroid().buffer(edge/2).bounds()
    # Return a new Feature, copying properties from the old Feature.
    return ee.Feature(centroid).copyProperties(feature)
    # Alternative: Keep this list of properties.
    # keepProperties = []
    # return ee.Feature(centroid).copyProperties(feature, keepProperties)

# Initialize Earth Engine
ee.Initialize()

# Get countries FeatureCollection
countries = ee.FeatureCollection("USDOS/LSIB_SIMPLE/2017")

# Create 1 ha Square Centroids
countries_square_centroids = countries.map(get_square_centroid)

# Set output directory
out_dir = path.join(path.dirname(__file__), 'raw_data', 'dummy')

if not path.exists(out_dir):
    makedirs(out_dir)

# Export locally
out_shp = path.join(out_dir, "countries_square_centroids.shp")
geemap.ee_export_vector(countries_square_centroids, out_shp, verbose=True)
