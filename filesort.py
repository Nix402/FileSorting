import os
import shutil

# Function to organize files
def organize_files(directory):
    # Dictionary to map file extensions to folder names
    file_types = {
        'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp'],
        'Documents': ['.pdf', '.docx', '.txt', '.xlsx', '.pptx'],
        'Videos': ['.mp4', '.mkv', '.avi', '.mov'],
        'Audios': ['.mp3', '.wav', '.flac'],
        'Archives': ['.zip', '.tar', '.rar', '.gz'],
    }
    
    # Go through each file in the directory
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)

        if os.path.isfile(file_path):
            # Get the file extension
            ext = os.path.splitext(filename)[1].lower()
            
            # Find the category for the file
            for category, extensions in file_types.items():
                if ext in extensions:
                    # Create a folder for the category if it doesn't exist
                    folder_path = os.path.join(directory, category)
                    if not os.path.exists(folder_path):
                        os.makedirs(folder_path)
                    
                    # Move the file to the respective folder
                    shutil.move(file_path, os.path.join(folder_path, filename))
                    print(f"Moved: {filename} -> {category}")
                    break

# Ask user for the directory to organize
directory = input("Enter the path of the directory you want to organize: ")

if os.path.isdir(directory):
    organize_files(directory)
else:
    print("Invalid directory.")
