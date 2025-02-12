import os
import re

def extract_index_and_coordinates(filename):
    """Extract the index, latitude, and longitude from a filename."""
    match = re.search(r'(\d+)__(-?\d+\.\d+)_(-?\d+\.\d+)\.png$', filename)
    if match:
        index, latitude, longitude = match.groups()
        return int(index), float(latitude), float(longitude)
    return None

def check_unique_coordinates(directory):
    """Check if all files in a directory have unique latitude and longitude combinations."""
    seen_coords = {}
    duplicates = []

    # Get all PNG files in the directory
    file_list = [f for f in os.listdir(directory) if f.endswith('.png')]

    for filename in file_list:
        extracted = extract_index_and_coordinates(filename)
        if extracted:
            index, lat, lon = extracted
            coords = (lat, lon)

            if coords in seen_coords:
                duplicates.append((index, filename, seen_coords[coords]))  # Store duplicate index
            else:
                seen_coords[coords] = index  # Store first occurrence index

    if duplicates:
        print("\nFiles with duplicate latitude and longitude:")
        for index, file, original_index in duplicates:
            print(f"Duplicate at batch {index}: {file} (Same as batch {original_index})")
    else:
        print("All files have unique latitude and longitude combinations.")

# Example usage
directory_path = r"C:/Users/Admin/OneDrive/Documents/000_Year 4 Term 2/THS-2/5 _ Wide Roads (200)"  # Replace with your actual directory path
check_unique_coordinates(directory_path)