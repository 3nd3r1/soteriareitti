class Location:
    def __init__(self, lat: float, lon: float):
        self.lat = lat
        self.lon = lon

    def as_tuple(self):
        return (self.lat, self.lon)
