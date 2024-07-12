import csv

# Creating the raw data
cities = [
  {"country": "France", "city": "Paris", "weather": 24},
  {"country": "Portugal", "city": "Lisbon", "weather": 30},
  {"country": "Australia", "city": "Canberra", "weather": 20} 
]

# Storing the csv file field names
field_names = ['country', 'city', 'weather']

# Storing the file name we want to create
file_name = 'cities.csv'

# Create the file
with open(file_name, 'w') as csvfile:
  # Create the writer
  writer = csv.DictWriter(csvfile, fieldnames=field_names)
  # Write the file header
  writer.writeheader()
  # Write the file rows
  writer.writerows(cities)

# Open the file
with open(file_name, 'r') as csvfile:
  # Create the reader
  reader = csv.DictReader(csvfile)
  # Reader each line one by one
  for line in reader:
    print(f"It is currently {line['weather']} in {line['city']}, {line['country']}.")