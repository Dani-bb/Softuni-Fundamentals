class Town:

    def __init__(self,name,latitute = "0°N", longitude = "0°E" ):
        self.name = name
        self.latitute = latitute
        self.longitude = longitude

    def set_latitude(self, latitude):
        self.latitute = latitude

    def set_longitude(self, longitude):
        self.longitude = longitude

    def __repr__(self):
        return f"Town: {self.name} | Latitude: {self.latitute} | Longitude: {self.longitude}"


