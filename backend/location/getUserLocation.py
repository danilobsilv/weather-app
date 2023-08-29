import geocoder


def get_user_location():
    return geocoder.ip("me").latlng
