"""
Made by Brady Hodge
CSE 111
04 Team Activity: Writing Functions
"""

from math import pi

can_sizes = [
    {"name": "#1 Picnic", "radius": 6.83, "height": 10.16, "cost": 0.28},
    {"name": "#1 Tall", "radius": 7.78, "height": 11.91, "cost": 0.43},
    {"name": "#2", "radius": 8.73, "height": 11.59, "cost": 0.45},
    {"name": "#2.5", "radius": 10.32, "height": 11.91, "cost": 0.61},
    {"name": "#3 Cylinder", "radius": 10.79, "height": 17.78, "cost": 0.86},
    {"name": "#5", "radius": 13.02, "height": 14.29, "cost": 0.83},
    {"name": "#6Z", "radius": 5.40, "height": 8.89, "cost": 0.22},
    {"name": "#8Z short", "radius": 6.83, "height": 7.62, "cost": 0.26},
    {"name": "#10", "radius": 15.72, "height": 17.78, "cost": 1.53},
    {"name": "#211", "radius": 6.83, "height": 12.38, "cost": 0.34},
    {"name": "#300", "radius": 7.62, "height": 11.27, "cost": 0.38},
    {"name": "#303", "radius": 8.10, "height": 11.11, "cost": 0.42},
]


def main():

    best_storage_efficiency = None
    best_cost_efficiency = None

    for can in can_sizes:
        volume = compute_volume(can["radius"], can["height"])
        surface_area = compute_surface_area(can["radius"], can["height"])
        storage_efficiency = compute_storage_efficiency(volume, surface_area)
        cost_efficiency = compute_cost_efficiency(volume, can["cost"])
        print(can["name"])
        print(f"Volume: {volume:.2f}")
        print(f"Surface Area: {surface_area:.2f}")
        print(f"Storage Efficiency: {storage_efficiency:.2f}")
        print(f"Cost Efficiency: {cost_efficiency:.2f}")
        print()
        
        if best_storage_efficiency is None or storage_efficiency > best_storage_efficiency:
            best_storage_efficiency = storage_efficiency
            best_storage_efficiency_name = can["name"]
        if best_cost_efficiency is None or cost_efficiency > best_cost_efficiency:
            best_cost_efficiency = cost_efficiency
            best_cost_efficiency_name = can["name"]
    
    print(f"The can with the best storage efficiency is {best_storage_efficiency_name}.")
    print(f"The can with the best cost efficiency is {best_cost_efficiency_name}.")


def compute_volume(radius, height):
    volume = pi * radius ** 2 * height
    return volume


def compute_surface_area(radius, height):
    surface_area = 2 * pi * radius * (radius + height)
    return surface_area


def compute_storage_efficiency(volume, surface_area):
    storage_efficiency = volume / surface_area
    return storage_efficiency

def compute_cost_efficiency(volume, cost):
    cost_efficiency = volume / cost
    return cost_efficiency

main()
