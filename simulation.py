import csv

def load_population_data(file_path):
    """Load population data from CSV file."""
    with open(file_path, 'r') as f:
        reader = csv.DictReader(f)
        data = [row for row in reader]
    return data

def project_rabbit_population(data):
    """Calculate projected rabbit population for the next year."""
    # Get the most recent year's data
    last_row = data[-1]
    rabbit_pop = float(last_row['rabbit_population'])
    python_pop = float(last_row['python_population'])
    
    # Apply predator-prey formula
    new_rabbit_pop = (rabbit_pop * 1.1) - (python_pop * 20)
    return new_rabbit_pop

if __name__ == "__main__":
    data = load_population_data('population_data.csv')
    projected = project_rabbit_population(data)
    print(f"Projected rabbit population for next year: {projected:.0f}")