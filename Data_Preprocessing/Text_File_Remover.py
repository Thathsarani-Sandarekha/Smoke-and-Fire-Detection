import os

def delete_files_starting_with_rs(folder_path):
    try:
        # List all files in the folder
        files = os.listdir(folder_path)

        # Iterate through the files
        for file in files:
            # Check if the file has a .txt extension and starts with "RS" after an underscore
            if file.endswith(".txt") and file.split('_')[-1].startswith("RS"):
                # Construct the full path to the file
                file_path = os.path.join(folder_path, file)

                # Delete the file
                os.remove(file_path)

                print(f"Deleted: {file_path}")

        print("Deletion of files starting with 'RS' completed.")

    except Exception as e:
        print(f"An error occurred: {e}")

# Specify the path to your folder
folder_path = "/home/ai_ds_team/HDD/Oshen_Temp/Research/Data_Now/Data5/annotations/YOLO/labels"

# Call the function to delete files starting with 'RS'
delete_files_starting_with_rs(folder_path)
