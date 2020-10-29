import math
from ipywidgets import widgets
def getBoundsZoomLevel(bounds):
	WORLD_DIM = {"height": 256, "width": 256}
	mapDim = { "height": 800, "width": 1000 }
	ZOOM_MAX = 21
	def latRad(lat):
		sin = math.sin(lat * math.pi / 180);
		radX2 = math.log((1 + sin) / (1 - sin)) / 2
		return max(min(radX2, math.pi), -math.pi) / 2
	def zoom(mapPx, worldPx, fraction):
		return math.floor(math.log(mapPx / worldPx / fraction) / math.log(2))
	ne = bounds[0]
	sw = bounds[1]

	latFraction = (latRad(ne[0]) - latRad(sw[0])) / math.pi

	lngDiff = ne[1] - sw[1]
	lngFraction = lngDiff + 360 if lngDiff < 0 else lngDiff / 360
	latZoom = zoom(mapDim["height"], WORLD_DIM["height"], latFraction)
	lngZoom = zoom(mapDim["width"], WORLD_DIM["width"], lngFraction);
	return min(latZoom, lngZoom, ZOOM_MAX)
def calculate_utm_zone(lat, lon):
    if lat >= 0:
            hemi = 'N'
    else:
            hemi = 'S'
    zone = int((180 + lon) // 6) + 1

    return (zone, hemi)

txt_get_api_key = widgets.Text() 
input_widgets = widgets.HBox([txt_get_api_key, widgets.Label(value="Enter API Key") ])
