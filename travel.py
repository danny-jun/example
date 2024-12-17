import itertools
import folium
from IPython.display import display

# Function to calculate the total distance of a given route
def calculate_total_distance(route, distance_matrix):
    total_distance = 0
    for i in range(len(route) - 1):
        total_distance += distance_matrix[route[i]][route[i + 1]]
    total_distance += distance_matrix[route[-1]][route[0]]  # Return to starting point (Nairobi)
    return total_distance

# Function to find the optimal path using TSP
def find_optimal_path(counties, distance_matrix):
    all_routes = itertools.permutations(range(1, len(counties)))  # Start from 1 because 0 is Nairobi
    min_distance = float('inf')
    best_route = None
    for route in all_routes:
        route = (0,) + route + (0,)  # Start and end at Nairobi
        current_distance = calculate_total_distance(route, distance_matrix)
        if current_distance < min_distance:
            min_distance = current_distance
            best_route = route
    return best_route, min_distance

def main():
    counties = ["Nairobi", "Nyeri", "Nakuru", "Laikipia", "Nandi", "Meru"]
    county_coords = {
        "Nairobi": (-1.286389, 36.817223),
        "Nyeri": (-0.4245, 36.9434),
        "Nakuru": (-0.3031, 36.0800),
        "Laikipia": (0.3142, 36.7848),
        "Nandi": (0.1742, 35.0961),
        "Meru": (0.0470, 37.6499)
    }

    # Define distances (in km) between counties
    distance_matrix = [
        [0, 150, 162, 263, 314, 225],  # Nairobi
        [150, 0, 166, 130, 319, 136],  # Nyeri
        [162, 166, 0, 249, 156, 256],  # Nakuru
        [263, 130, 249, 0, 402, 143],  # Laikipia
        [314, 319, 156, 402, 0, 35],   # Nandi
        [225, 136, 256, 143, 35, 0]    # Meru
    ]

    best_route, min_distance = find_optimal_path(counties, distance_matrix)
    
    best_route_counties = [counties[i] for i in best_route]
    print("\nThe shortest route to deliver goods is:")
    print(" -> ".join(best_route_counties) + f" -> {best_route_counties[0]}")
    print(f"Total distance: {min_distance} km")

    # Create a folium map centered around Kenya
    m = folium.Map(location=[-1.286389, 36.817223], zoom_start=7)
    
    # Add markers for each county
    for county in counties:
        folium.Marker(location=county_coords[county], popup=county).add_to(m)
    
    # Add lines for the best route
    route_coords = [county_coords[county] for county in best_route_counties]
    route_coords.append(route_coords[0])  # To close the loop
    folium.PolyLine(route_coords, color="blue", weight=2.5, opacity=1).add_to(m)
    
    # Save and display the map
    m.save("shortest_route_map.html")
    display(m)

main()