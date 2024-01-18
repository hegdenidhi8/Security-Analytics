# Define the path to drebin_features.txt
file_path = '/Users/nidhi/Documents/Fall 2023/CS529/HW2/drebin_features.txt'

# Initialize a feature counter
num_features = 0

# Open and read the file
with open(file_path, 'r') as file:
    for line in file:
        # Check if the line contains a feature description
        if line.startswith("Feature: "):
            num_features += 1

# Print the number of features
print("Number of features in the Drebin dataset:", num_features)
