import os
import random
import shutil

def split_dataset(input_images_folder, input_labels_folder, output_train_images_folder, output_val_images_folder,
                  output_train_labels_folder, output_val_labels_folder, split_ratio=0.8):
    # Create output folders if they don't exist
    os.makedirs(output_train_images_folder, exist_ok=True)
    os.makedirs(output_val_images_folder, exist_ok=True)
    os.makedirs(output_train_labels_folder, exist_ok=True)
    os.makedirs(output_val_labels_folder, exist_ok=True)

    # Get the list of image files in the input folder
    image_files = [f for f in os.listdir(input_images_folder) if f.endswith(('.jpg', '.jpeg', '.png'))]

    # Calculate the number of images for training and validation
    num_images = len(image_files)
    num_train = int(num_images * split_ratio)
    num_val = num_images - num_train

    # Randomly shuffle the list of image files
    random.shuffle(image_files)

    # Split images
    train_images = image_files[:num_train]
    val_images = image_files[num_train:]

    # Copy images and labels to training folders
    for img_file in train_images:
        # Copy images
        src_image_path = os.path.join(input_images_folder, img_file)
        dest_image_path = os.path.join(output_train_images_folder, img_file)
        shutil.copy(src_image_path, dest_image_path)

        # Copy labels
        label_file = os.path.splitext(img_file)[0] + '.txt'
        src_label_path = os.path.join(input_labels_folder, label_file)
        dest_label_path = os.path.join(output_train_labels_folder, label_file)
        shutil.copy(src_label_path, dest_label_path)
        print("Images")

    # Copy images and labels to validation folders
    for img_file in val_images:
        # Copy images
        src_image_path = os.path.join(input_images_folder, img_file)
        dest_image_path = os.path.join(output_val_images_folder, img_file)
        shutil.copy(src_image_path, dest_image_path)

        # Copy labels
        label_file = os.path.splitext(img_file)[0] + '.txt'
        src_label_path = os.path.join(input_labels_folder, label_file)
        dest_label_path = os.path.join(output_val_labels_folder, label_file)
        shutil.copy(src_label_path, dest_label_path)
        print("Labels")

if __name__ == "__main__":
    # Replace these paths with your actual folder paths
    input_images_folder_path = "/home/ai_ds_team/HDD/Oshen_Temp/Research/Smoke and Fire/Dataset/images/train"
    input_labels_folder_path = "/home/ai_ds_team/HDD/Oshen_Temp/Research/Smoke and Fire/Dataset/labels/train"
    output_train_images_folder_path = "/home/ai_ds_team/HDD/Oshen_Temp/Research/Smoke and Fire/Dataset/train_i"
    output_val_images_folder_path = "/home/ai_ds_team/HDD/Oshen_Temp/Research/Smoke and Fire/Dataset/test_i"
    output_train_labels_folder_path = "/home/ai_ds_team/HDD/Oshen_Temp/Research/Smoke and Fire/Dataset/train_l"
    output_val_labels_folder_path = "/home/ai_ds_team/HDD/Oshen_Temp/Research/Smoke and Fire/Dataset/test_l"

    split_dataset(input_images_folder_path, input_labels_folder_path,
                  output_train_images_folder_path, output_val_images_folder_path,
                  output_train_labels_folder_path, output_val_labels_folder_path)
