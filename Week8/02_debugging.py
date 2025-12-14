"""
Week 8: Debugging Examples
Topics: pdb, logging, error handling
"""

import logging

# Setup logging
logging.basicConfig(level=logging.DEBUG, 
                   format='%(levelname)s: %(message)s')

def calculate_average(numbers):
    """Calculate average with logging"""
    logging.info(f"Calculating average of {len(numbers)} numbers")
    
    if not numbers:
        logging.error("Empty list provided!")
        raise ValueError("Cannot calculate average of empty list")
    
    total = sum(numbers)
    avg = total / len(numbers)
    
    logging.info(f"Average calculated: {avg}")
    return avg

# Demo
try:
    result = calculate_average([1, 2, 3, 4, 5])
    print(f"Average: {result}")
    
    # This will cause an error
    calculate_average([])
except ValueError as e:
    logging.error(f"Error occurred: {e}")
