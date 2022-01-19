import mercantile, mapbox_vector_tile, requests, json
from vt2geojson.tools import vt_bytes_to_geojson


def main():
    # define an empty geojson as output
    output= { "type": "FeatureCollection", "features": [] }

    # vector tile endpoints -- change this in the API request to reference the correct endpoint
    tile_coverage = 'mly1_public'

    # tile layer depends which vector tile endpoints: 
    # 1. if map features or traffic signs, it will be "point" always
    # 2. if looking for coverage, it will be "image" for points, "sequence" for lines, or "overview" for far zoom
    #tile_layer = "sequence"
    tile_layer = "image"

    # Mapillary access token -- user should provide their own
    access_token = 'XXX'

    # a bounding box in [east_lng,_south_lat,west_lng,north_lat] format
    #west, south, east, north = [-80.13423442840576,25.77376933762778,-80.1264238357544,25.788608487732198]
    #Italy
    west, south, east, north = [9.48983,44.60285,10.1098775,45.1662309]
                            
    # get the list of tiles with x and y coordinates which intersect our bounding box
    # MUST be at zoom level 14 where the data is available, other zooms currently not supported
    tiles = list(mercantile.tiles(west, south, east, north, 14))

    # loop through list of tiles to get tile z/x/y to plug in to Mapillary endpoints and make request
    for tile in tiles:
        tile_url = 'https://tiles.mapillary.com/maps/vtp/{}/2/{}/{}/{}?access_token={}'.format(tile_coverage,tile.z,tile.x,tile.y,access_token)
        response = requests.get(tile_url)
        data = vt_bytes_to_geojson(response.content, tile.x, tile.y, tile.z,layer=tile_layer)

        # push to output geojson object if yes
        for feature in data['features']:
            # I wanted only some kind of images for my geoJSON
            if (('organization_id' in feature["properties"].keys()) and (feature["properties"]['organization_id'] == 2099172886922450)):
                output['features'].append(feature)

    # save a local geojson with the filtered data if you choose tile_layer = "sequence"
    #with open('sequences.geojson', 'w') as f:
    #    json.dump(output, f)

    with open('images.geojson', 'w') as f:
        json.dump(output, f)


if __name__ == "__main__":
    main()