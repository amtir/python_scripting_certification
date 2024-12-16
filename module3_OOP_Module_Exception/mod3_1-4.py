import math

def calculate_distance(lat1, lon1, lat2, lon2):
    """
    Calculate the distance between two points on the earth (specified in decimal degrees).
    """
    # Convert decimal degrees to radians
    lat1, lon1, lat2, lon2 = map(math.radians, [lat1, lon1, lat2, lon2])

    # Haversine formula
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = math.sin(dlat/2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon/2)**2
    c = 2 * math.asin(math.sqrt(a))
    r = 6371  # Radius of earth in kilometers. Use 3956 for miles
    return c * r

# Example usage
lat1 = 52.2296756
lon1 = 21.0122287
lat2 = 41.8919300
lon2 = 12.5113300

distance = calculate_distance(lat1, lon1, lat2, lon2)
print(f"Distance: {distance:.2f} kilometers")