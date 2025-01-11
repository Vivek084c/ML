import os

# Define the directory structure
directories = [
    "src",         # Source code directory
    "experiments"  # Experiments directory
]

# Create the directories
for directory in directories:
    try:
        os.makedirs(directory, exist_ok=True)
        print(f"Directory '{directory}' created successfully.")
    except Exception as e:
        print(f"Error creating directory '{directory}': {e}")

# Create Python files in the src directory
src_files = ["src/main1.py", "src/main2.py"]

for file_path in src_files:
    try:
        with open(file_path, "w") as file:
            file.write("# This is a placeholder for the " + os.path.basename(file_path) + " script.\n")
        print(f"File '{file_path}' created successfully.")
    except Exception as e:
        print(f"Error creating file '{file_path}': {e}")