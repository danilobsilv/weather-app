import geocoder

def get_user_location():
    g = geocoder.ip('me')
    return g.latlng