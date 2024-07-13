import random
import matplotlib.pyplot as plt
from Facility import Facility
from Point import Point
from Operators import Operators

def main():
    operator = Operators()
    
    # Determine the number of candidate facilities
    candidate_facility_number = 15 
    # Set the number of points
    point_amount = 40 
    
    # Create coordinates of Facilities and Points
    facs_coordinates = operator.create_distance_matrix(candidate_facility_number, 2) 
    points_coordinates = operator.create_distance_matrix(point_amount, 2)  
    
    # Create Facility objects for candidate facilities and add them to the list
    # Set a random capacity (between 50 and 70) with the x and y coordinates of the facilities
    facs = [Facility(i, facs_coordinates[i][0], facs_coordinates[i][1], 20 * random.random() + 50) for i in range(candidate_facility_number)]
    
    # Create Point options for points and add them to the list
    # Set a random request (between 1 and 3) with the x and y coordinates of the points
    points = [Point(i, points_coordinates[i][0], points_coordinates[i][1], 2 * random.random() + 1 , 1 ) for i in range(point_amount)]
    
    # Create distance matrix between facilities and points
    distance_matrix = operator.distance_matrix(facs, points)
    
    # Store opened facilities and other lists, you need to use these arrays
    opened_facilities = []
    unopened_facilities = facs.copy()
    unassigned_points = []

    # Number of facilities to open
    open_p_num_of_facs = 3
    
    total_distance = 0
    min_value = float('inf')
    index_of = 0
    previous_min = -1
    max_val = 0

    # Find a huge value to set min_value for comparison
    for y in range(len(facs)):
        total_distance = sum(distance_matrix[y])
        if max_val < total_distance:
            max_val = total_distance
    min_value = max_val + 1

    # Start coding here
    # I code the algorithm for k-center algorithm solution with a greddy approach
    
    # The place closest to all points is chosen as the most suitable value for the starting facility
    distances = {}
    for fac in unopened_facilities:
      total_distance = 0
      for point in points:
        dist = operator.euclidean_distance(fac, point)
        total_distance += dist
        distances[fac] = total_distance
    start_facility = min(distances, key=distances.get)
    
    # This selected center is removed from closed facilities and open infrastructure is added
    opened_facilities.append(start_facility)
    unopened_facilities.remove(start_facility)
    
    # The cycle continues until all targeted facilities are opened
    while len(opened_facilities) < open_p_num_of_facs:

        # Calculate the minimum distance of each point to all opened facilities
        point_distances = {}
        for point in points:
            min_distance = float('inf')
            for fac in opened_facilities:
                # Calculate the Euclidean distance between the current facility and the point
                dist = operator.euclidean_distance(fac, point)
                if dist < min_distance:
                    min_distance = dist
            point_distances[point] = min_distance

        # Find the point that is furthest from any opened facility
        far_point = max(point_distances, key=point_distances.get)

        # Find the unopened facility that minimizes the distance to this farthest point
        new_facility_distances = {}
        for fac in unopened_facilities:
            # Calculate the Euclidean distance between the unopened facility and the farthest point
            dist = operator.euclidean_distance(fac, far_point)
            new_facility_distances[fac] = dist

        # Choose the facility with the minimum distance to the farthest point
        new_facility = min(new_facility_distances, key=new_facility_distances.get)

        # Open the new facility and remove it from the list of unopened facilities
        opened_facilities.append(new_facility)
        unopened_facilities.remove(new_facility)

    # Assign each point to the nearest facility
    for point in points:
        # Create a dictionary to store distances from each point to the facility
        facility_distances = {}
        for facility in opened_facilities:
            facility_distances[facility] = operator.euclidean_distance(point, facility)

        # Sort facilities by distance to the point (ascending order)
        sorted_facilities = sorted(facility_distances.items(), key=lambda item: item[1])

        # Assign the point to the nearest facility with sufficient supply
        for facility, distance in sorted_facilities:
            if facility.supply >= point.demand:
                point.assigned_facility_id = facility.id
                facility.supply -= point.demand  # Update facility supply
                break
                  # Stop after assigning to the nearest available facility
            else:
                point.assigned_facility_id = None  # Unassign if no facility can meet demand

    plot_facilities_and_points(opened_facilities, unopened_facilities, points)


def plot_facilities_and_points(opened_facilities, unopened_facilities, points):
    colors = {}
    color_list = ['blue', 'red', 'green', 'purple', 'orange', 'cyan', 'pink', 'yellow', 'brown', 'linen']
    for i, fac in enumerate(opened_facilities):
        colors[fac.id] = color_list[i % len(color_list)]

    for fac in unopened_facilities:
        plt.scatter(fac.x, fac.y, c='black', marker='^')

    for fac in opened_facilities:
        plt.scatter(fac.x, fac.y, c=colors[fac.id], marker='^')

    for point in points:
        if point.assigned_facility_id is not None:
            plt.scatter(point.x, point.y, c=colors[point.assigned_facility_id], marker='o')

    plt.xlabel('X Coordinate')
    plt.ylabel('Y Coordinate')
    plt.title('Facilities and Assigned Points')

    plt.show()

if __name__ == "__main__":
    main()