# Large Dataset Creation Process

## Overview
To replicate the experiments described in our paper and generate the same Large Dataset, please follow the steps outlined below. 
This involves downloading and organizing multiple skin lesion image datasets. Once the datasets are organized as instructed, you can run the Python script (`large_dataset_creation.py`) to filter and prepare the Large Dataset.

## Steps to Create the Large Dataset

### 1. Download the Datasets
- Download each dataset using the links provided in the following list of datasets.
- Ensure that all required datasets are downloaded for the experiments.

### 2. Organize the Datasets
- After downloading, rename the extracted dataset folders as specified (e.g., `HAM10000_images_part_1.zip`, `ISIC-msk1.zip`, `ISIC-consecutiveBiopsies2020.zip`, etc.).
- Place all renamed folders into a single directory named `Skin_Lesions_Datasets`.

### 3. Download the CSV File
Download the `LARGE_DATASET_METADATA.csv` file from this GitHub repository. This file contains the metadata for the images needed to create the Large Dataset.
Make sure to save the CSV file in a location where you can easily reference its path later.

### 4. Run the Python Script
- Once the datasets are organized, run the `large_dataset_creation.py` script.
- The script will filter the images based on the specifications from our paper and generate the final Large Dataset.
  During the execution, you will be prompted to input the following three paths:
  - The path to the LARGE_DATASET_METADATA.csv file you just downloaded.
  - The path to the folder  `Skin_Lesions_Datasets` where the ZIP/RAR datasets are located.
  - The path to the output folder where the extracted images will be saved.
  
  To run the script, use the following command:
  ```bash
  python large_dataset_creation.py
  ```
  The script will then guide you through specifying the correct paths.

## Datasets and Download Links

1. **HAM10000**
   - [Dataset Link](https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/DBW86T)
   - Folders: `HAM10000_images_part_1.zip`, `HAM10000_images_part_2.zip`
   - Structure:
     ```
     HAM10000/
     ├── ISIC_0029305.jpg
     ├── ISIC_0024306.jpg
     ...
     ```

2. **Consecutive biopsies for melanoma**
   - [Dataset Link](https://api.isic-archive.com/collections/216/)
   - File: `ISIC-consecutiveBiopsies2020.zip`
   - Structure:
     ```
     ISIC-consecutiveBiopsies2020/
     ├── licenses
     ├── metadata.csv
     ├── attribution.txt
     ├── ISIC_9963174.JPG
     ...
     ```

3. **MSK1 to MSK5**
   - MSK1 [Link](https://api.isic-archive.com/collections/289/)
   - MSK2 [Link](https://api.isic-archive.com/collections/290/)
   - MSK3 [Link](https://api.isic-archive.com/collections/288/)
   - MSK4 [Link](https://api.isic-archive.com/collections/287/)
   - MSK5 [Link](https://api.isic-archive.com/collections/286/)
   - Files: `ISIC-msk1.zip`, `ISIC-msk2.zip`, `ISIC-msk3.zip`, `ISIC-msk4.zip`, `ISIC-msk5.zip`
   - Structure (similar for each):
     ```
     ISIC-mskX/
     ├── licenses
     ├── metadata.csv
     ├── attribution.txt
     ├── ISIC_0015649.JPG
     ...
     ```

4. **Hospital Italiano de Buenos Aires Dataset**
   - [Dataset Link](https://api.isic-archive.com/collections/251/)
   - File: `ISIC-HIBAskinlesions.zip`
   - Structure:
     ```
     ISIC-HIBAskinlesions/
     ├── licenses
     ├── metadata.csv
     ├── attribution.txt
     ├── ISIC_9999251.JPG
     ...
     ```

5. **SKINL2**
   - [Dataset Link](https://www.it.pt/AutomaticPage?id=3459)
   - Files: `SKINL2_v1.zip`, `SKINL2_v2.zip`, `SKINL2_v3.zip`
   - Structure (v2 and v3 similar):
     ```
     SKINL2_v1/
     ├── PlenoISLA_DatasetV1_info.xlsx
     ├── Light Fields/
     │   │   ...
     ├── Dermatoscopic/
     │   ├── Seborrheic Keratosis/
     │   │   ├── 0243_Dermatoscopic.png
     │   │   |   ...
     │   ├── Nevus/
     │   │   |   ...
     │   ├── ...
     ```
     ```
     SKINL2_v2/
     ├── PlenoISLA_DatasetV2_info.xlsx
     ├── 0087/
     │   ├── Others/
     │   |   ├── Dermatoscopic/
     │   │   |   ├── 0087_Dermatoscopic.png
     │   |   ├── Light Field/
     │   │   |   |   ...
     │   ...
     ```

6. **BCN20000**
   - [Dataset Link](https://api.isic-archive.com/collections/249/)
   - File: `ISIC-bcn20000.zip`
   - Structure:
     ```
     ISIC-bcn20000/
     ├── licenses
     ├── metadata.csv
     ├── attribution.txt
     ├── ISIC_0073254.JPG
     ...
     ```

7. **UDA-1 and UDA-2**
   - UDA-1 [Link](https://api.isic-archive.com/collections/292/)
   - UDA-2 [Link](https://api.isic-archive.com/collections/291/)
   - Files: `ISIC-uda1.zip`, `ISIC-uda2.zip`
   - Structure (similar for each):
     ```
     ISIC-udaX/
     ├── licenses
     ├── metadata.csv
     ├── attribution.txt
     ├── ISIC_0000556.JPG
     ...
     ```

8. **7-point criteria evaluation**
   - [Dataset Link](https://derm.cs.sfu.ca/Welcome.html)
   - File: `7PointCriteria.zip`
   - Structure:
     ```
     7PointCriteria/
     ├── release_v0/
     │   ├── meta/
     │   ├── images/
     │   │   ├── NML/
     │   │   |   ├── Nml114.jpg
     │   │   |   |   ...
     │   |   ...
     │   ├── README.txt
     │   ├── derm.html
     │   ├── clinic.html
     ```

9. **ISIC Challenge 2018 Datasets**
   - 2018 Test [Link](https://challenge.isic-archive.com/data/#2018)
   - 2018 Validation [Link](https://challenge.isic-archive.com/data/#2018)
   - 2020 Training Set [Link](https://challenge.isic-archive.com/data/#2020)
   - Files: `ISIC-2018Test.zip`, `ISIC-2018Validation.zip`
   - Structure (similar for each):
     ```
     ISIC-2018Test/
     ├── licenses
     ├── metadata.csv
     ├── attribution.txt
     ├── ISIC_0036347.JPG
     ...
     ```
     ```
     ISIC-2018Validation/
     ├── licenses
     ├── metadata.csv
     ├── attribution.txt
     ├── ISIC_0036333.JPG
     ...
     ```
10. **ISIC Challenge 2020 Dataset**
   - 2020 Training Set [Link](https://challenge.isic-archive.com/data/#2020)
   - File: `ISIC-2020TrainingSet.zip`
   - Structure:
     ```
     ISIC-2020/
     ├── train
     │   ├── ISIC_0015719.jpg
     │   |   ...
     ```

11. **PH2**
    - [Dataset Link](https://www.fc.up.pt/addi/ph2%20database.html)
    - File: `PH2Dataset.rar`
    - Structure:
      ```
      PH2Dataset/
      ├── PH2 Dataset Images/
      │   ├── IMD437/
      │   │   ├── IMD437_Dermoscopic_Image/
      │   │   │   ├── IMD437.bmp
      │   │   │   ...
      │   ├── IMD002/
      │   │   ├── IMD002_Dermoscopic_Image/
      │   │   │   ├── IMD002.bmp
      │   │   │   ...
      ├── Readme.txt
      ├── PH2_dataset.xlsx
      ├── PH2_dataset.txt
      ```

### Additional notes
Following this process will help you recreate the Large Dataset used in the experiments. If you encounter any issues, please let us know for support.
