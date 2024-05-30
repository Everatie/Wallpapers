import os

def rename_files_in_subfolders(directory):
    # Iterate through subdirectories
    for subdir in os.listdir(directory):
        subdir_path = os.path.join(directory, subdir)
        if os.path.isdir(subdir_path):
            try:
                # Convert folder name to an integer to determine the starting index
                start_index = int(subdir.split('.')[0]) * 1000 + 1
            except ValueError:
                # Skip folders that do not have numerical names
                continue
            
            # List all files in the subdirectory
            files = [f for f in os.listdir(subdir_path) if os.path.isfile(os.path.join(subdir_path, f))]
            files.sort()
            
            # Rename files with numerical order starting from start_index
            for i, filename in enumerate(files):
                ext = os.path.splitext(filename)[1]
                new_name = f"{start_index + i:04d}{ext}"
                old_path = os.path.join(subdir_path, filename)
                new_path = os.path.join(subdir_path, new_name)
                # Check if the new file name already exists
                if os.path.exists(new_path):
                    print(f"Skipping: {old_path} -> {new_path} (already exists)")
                else:
                    os.rename(old_path, new_path)
                    print(f"Renamed: {old_path} -> {new_path}")

# Define the main directory
mainDirectory = '../Wallpapers'  # Replace with your main directory path
rename_files_in_subfolders(mainDirectory)