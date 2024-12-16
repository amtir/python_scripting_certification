import argparse
from geopy.geocoders import Nominatim

# pip install geopy

def get_location(address):
    geolocator = Nominatim(user_agent="location_script")
    location = geolocator.geocode(address)
    if location:
        print(f"Address: {location.address}")
        print(f"Latitude: {location.latitude}")
        print(f"Longitude: {location.longitude}")
    else:
        print("Location not found")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Get the location parameters of an address.")
    parser.add_argument('address', type=str, help="The address to lookup.")
    
    args = parser.parse_args()
    get_location(args.address)
