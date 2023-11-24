import os
import shutil

main_folder = '/home/ai_ds_team/HDD/Oshen_Temp/Research/Smoke and Fire/Dataset/Images'

# Create four destination folders
dest_folder1 = '/home/ai_ds_team/HDD/Oshen_Temp/Research/Smoke and Fire/New_Dataset/bothFireandSmoke'
dest_folder2 = '/home/ai_ds_team/HDD/Oshen_Temp/Research/Smoke and Fire/New_Dataset/fire'
dest_folder3 = '/home/ai_ds_team/HDD/Oshen_Temp/Research/Smoke and Fire/New_Dataset/neitherFireNorSmoke'
dest_folder4 = '/home/ai_ds_team/HDD/Oshen_Temp/Research/Smoke and Fire/New_Dataset/smoke'

# List all files in the main folder
files = os.listdir(main_folder)

# Iterate through the files and copy them to the destination folders
for file in files:
    if file.endswith('.jpg'):
        prefix = file.split('_')[0]
        source_path = os.path.join(main_folder, file)

        if prefix == 'bothFireAndSmoke':
            shutil.copy(source_path, os.path.join(dest_folder1, file))
        elif prefix == 'fire':
            shutil.copy(source_path, os.path.join(dest_folder2, file))
        elif prefix == 'neitherFireNorSmoke':
            shutil.copy(source_path, os.path.join(dest_folder3, file))
        elif prefix == 'smoke':
            shutil.copy(source_path, os.path.join(dest_folder4, file))

print("Files have been sorted into different folders.")
