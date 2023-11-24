import os

def delete_tif_files(folder_path):
    try:
        # List all files in the folder
        files = os.listdir(folder_path)

        # Iterate through the files
        for file in files:
            # Check if the file has a .tif extension
            if file.endswith(".tif"):
                # Construct the full path to the file
                file_path = os.path.join(folder_path, file)

                # Delete the file
                os.remove(file_path)

                print(f"Deleted: {file_path}")

        print("Deletion of .tif files completed.")

    except Exception as e:
        print(f"An error occurred: {e}")

# Specify the path to your folder
folder_path = "/home/ai_ds_team/HDD/Oshen_Temp/Research/Data_Now/Data5/images"

# Call the function to delete .tif files
delete_tif_files(folder_path)
