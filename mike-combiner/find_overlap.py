import numpy as np

def find_overlap(ord1, ord2, tolerance=1e-6):
    # Find the common values using np.isclose
    ord1_expanded = ord1[:, None]  # Reshape ord1 for broadcasting
    matches = np.any(np.isclose(ord1_expanded, ord2, atol=tolerance), axis=1)
    
    # Extract common values from ord1
    common_values = ord1[matches]
    
    # Check if there are common values
    if common_values.size == 0:
        return None, None  # No common values
    
    # Find smallest and largest values
    smallest = np.min(common_values)
    largest = np.max(common_values)
    
    return smallest, largest