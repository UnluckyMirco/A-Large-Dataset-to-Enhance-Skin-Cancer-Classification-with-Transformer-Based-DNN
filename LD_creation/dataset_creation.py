import pandas as pd
import zipfile
import rarfile 
import os

# Search of an image inside a ZIP file and all his subfolders
def extract_image_from_zip(zip_path, image_name_no_ext, output_dir):
    possible_extensions = ['.jpg', '.png', '.bmp', '.JPG']

    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        for file in zip_ref.namelist():
            for ext in possible_extensions:
                image_name = image_name_no_ext + ext
                if file.endswith(image_name): 
                    if not os.path.exists(output_dir):
                        os.makedirs(output_dir)
                    zip_ref.extract(file, output_dir)
                    print(f"Image extracted: {file} from {zip_path} in the folder {output_dir}")
                    return True
        print(f"Image {image_name_no_ext} not found in {zip_path}")
        return False


# Search of an image inside a RAR file and all his subfolders
def extract_image_from_rar(rar_path, image_name_no_ext, output_dir):
    possible_extensions = ['.jpg', '.png', '.bmp', '.JPG']

    with rarfile.RarFile(rar_path, 'r') as rar_ref:
        for file in rar_ref.namelist():
            for ext in possible_extensions:
                image_name = image_name_no_ext + ext
                if file.endswith(image_name):  
                    if not os.path.exists(output_dir):
                        os.makedirs(output_dir)
                    rar_ref.extract(file, output_dir) 
                    print(f"Image extracted: {file} from {rar_path} in the folder {output_dir}")
                    return True
        print(f"Image {image_name_no_ext} not found in {rar_path}")
        return False


# Main function for the extraction process
def main():
    # Input the file paths
    csv_file = input("Enter the path to your CSV file (e.g., C:/path/to/file.csv): ")
    image_folder = input("Enter the path to the image folder containing ZIP/RAR files (e.g., C:/path/to/folder/Skin_Lesions_Datasets): ")
    output_folder = input("Enter the path to the output folder where images should be extracted (e.g., C:/path/to/output/folder/Large_Dataset): ")

    archive_mapping = {
        'HAM10000_images_part_1.zip': 'HAM10000',
        'HAM10000_images_part_2.zip': 'HAM10000',
        'ISIC-consecutiveBiopsies2020.zip': 'Consecutive biopsies 2020',
        'ISIC-msk1.zip': 'MSK-1',
        'ISIC-msk2.zip': 'MSK-2',
        'ISIC-msk3.zip': 'MSK-3',
        'ISIC-msk4.zip': 'MSK-4',
        'ISIC-msk5.zip': 'MSK-5',
        'ISIC-HIBAskinlesions.zip': 'HIBA skin lesions',
        'SKINL2_v1.zip': 'SKINL2_v1',
        'SKINL2_v2.zip': 'SKINL2_v2',
        'SKINL2_v3.zip': 'SKINL2_v3',
        'ISIC-bcn20000.zip': 'BCN20000',
        'ISIC-uda1.zip': 'UDA-1',
        'ISIC-uda2.zip': 'UDA-2',
        '7PointCriteria.zip': '7 Point Criteria',
        'ISIC-2018Test.zip': 'ISIC 2018 Test Set',
        'ISIC-2018Validation.zip': 'ISIC 2018 Validation Set',
        'ISIC-2020TrainingSet.zip': 'ISIC 2020 Training Set',
        'PH2Dataset.rar': 'PH2',
    }

    # Read CSV and check for dataset column
    df = pd.read_csv(csv_file, delimiter=';')

    for archive_name, dataset_name in archive_mapping.items():
        archive_path = os.path.join(image_folder, archive_name)

        # Filter the CSV to only include rows corresponding to the current dataset
        filtered_df = df[df['dataset'] == dataset_name]

        if not filtered_df.empty:
            print(f"Processing {archive_name}...")

            for index, row in filtered_df.iterrows():
                image_name_no_ext = row['image_id']
                diagnosis = row['dx']  # Diagnosis (bkl, nv, etc.)

                # Output directory based on the diagnosis
                output_dir = os.path.join(output_folder, diagnosis)

                # Check and extract images from the archive
                if archive_name.endswith('.zip'):
                    extract_image_from_zip(archive_path, image_name_no_ext, output_dir)
                elif archive_name.endswith('.rar'):
                    extract_image_from_rar(archive_path, image_name_no_ext, output_dir)
        else:
            print(f"No images found in CSV for dataset {dataset_name}. Skipping {archive_name}.")
    
    print("Process completed.")

if __name__ == "__main__":
    main()