import googlemaps
from itertools import permutations

# Replace with your actual API key
API_KEY = 'AIzaSyDD9Z2U0XR8RbEbjxPqhxD8yMfzJBpZks0'
gmaps = googlemaps.Client(key=API_KEY)

# Define the county headquarters, including Nairobi
counties = {
    'Nairobi': 'Nairobi, Kenya',
    'Nyeri': 'Nyeri, Kenya',
    'Nakuru': 'Nakuru, Kenya',
    'Laikipia': 'Nanyuki, Kenya',  # Assuming Nanyuki is the headquarters
    'Nandi': 'Nandi, Kenya',
    'Meru': 'Meru, Kenya'
}

# Get the distance matrix
def get_distance_matrix(locations):
    distance_matrix = {}
    for start in locations:
        for end in locations:
            if start != end:
                try:
                    result = gmaps.distance_matrix(start, end, mode='driving')
                    if result['status'] == 'OK':
                        distance = result['rows'][0]['elements'][0]['distance']['value']
                        distance_matrix[(start, end)] = distance
                    else:
                        print(f"Error: {result['status']}")
                except Exception as e:
                    print(f"Error fetching distance between {start} and {end}: {e}")
    return distance_matrix

# Get the total distance for a specific route
def calculate_route_distance(route, distance_matrix):
    total_distance = 0
    for i in range(len(route) - 1):
        total_distance += distance_matrix[(route[i], route[i + 1])]
    # Return to the starting point (Nairobi)
    total_distance += distance_matrix[(route[-1], route[0])]
    return total_distance

# Find the optimal route using brute-force (for simplicity)
def find_optimal_route(locations, distance_matrix):
    min_distance = float('inf')
    optimal_route = None
    for route in permutations(locations):
        if route[0] == 'Nairobi, Kenya':  # Ensure the route starts from Nairobi
            distance = calculate_route_distance(route, distance_matrix)
            if distance < min_distance:
                min_distance = distance
                optimal_route = route
    return optimal_route, min_distance

# Main script
locations = list(counties.values())

try:
    distance_matrix = get_distance_matrix(locations)
    optimal_route, min_distance = find_optimal_route(locations, distance_matrix)

    print("Optimal Route:")
    for location in optimal_route:
        print(location)
    print(f"Total Distance: {min_distance / 1000} km")

    # Generate a Google Maps URL to visualize the route
    route_str = '/'.join(location.replace(' ', '+') for location in optimal_route)
    google_maps_url = f"https://www.google.com/maps/dir/{route_str}"
    print("Google Maps URL to visualize the route:")
    print(google_maps_url)

except Exception as e:
    print(f"An error occurred: {e}")