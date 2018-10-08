from geopy.geocoders import Nominatim

def Position(address):
    geolocator = Nominatim(user_agent="Google")
    location = geolocator.geocode("address")
    return (location.latitude, location.longitude)

