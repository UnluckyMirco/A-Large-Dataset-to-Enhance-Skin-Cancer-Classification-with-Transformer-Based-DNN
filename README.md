# A-Large-Dataset-to-Enhance-Skin-Cancer-Classification-with-Transformer-Based-DNN
This is the repository of the paper "A Large Dataset to Enhance Skin Cancer Classification with Transformer-Based Deep Neural Networks," which contains the notebooks of the three best results presented in the paper and a read.me file that presents the construction of the Large Dataset proposed in the paper. For each dataset considered, a short explanation and references are presented. 

## HAM 10000 and its 7 classes

The HAM dataset consists of ten thousand images divided into seven classes: 
- **Melanoma** (MEL): Melanoma is a malignant neoplasm originating from melanocytes, the cells responsible for skin pigmentation. %It represents the most lethal form of skin cancer, characterized by high morphological variability and a tendency for early metastasis.

- **Melanocytic Nevi** (NV): Melanocytic nevi are benign lesions comprised of localized accumulations of melanocytes. %They are among the most common skin lesions, exhibiting a wide range of morphological appearances, typically circumscribed and with uniform pigmentation.

- **Basal Cell Carcinoma** (BCC): Basal cell carcinoma is the most common form of skin cancer, originating from the basal cells of the epidermal layer. %It is characterized by slow growth and a low risk of metastasis, typically manifesting as nodular or ulcerative lesions.

- **Actinic Keratoses** (AKIEC): Actinic keratoses are precancerous, scaly skin lesions induced by chronic exposure to ultraviolet rays. %They are considered precursors to squamous cell carcinoma and typically present as rough plaques on sun-exposed skin areas.

- **Benign Keratosis-like Lesions** (BKL): Benign keratosis-like lesions encompass a variety of benign conditions, such as seborrheic keratosis, sebaceous hyperplasia, and clear cell acanthoma. %An overgrowth of the keratin component of the epidermis characterizes these lesions.

- **Dermatofibroma** (DF): Dermatofibroma is a benign cutaneous nodule commonly resulting from a reaction to minor injuries or insect bites. %It typically presents as a firm, slightly raised lesion with a brown to reddish color.

- **Vascular Lesions** (VASC): Vascular lesions include a range of conditions characterized by abnormal proliferation or dilation of blood or lymphatic vessels. %Common examples are hemangiomas and vascular malformations. They typically present as red or purplish spots or nodules.


## Used Datasets

The Large Dataset consists of 41.975 images. For each dataset used, the following table shows:
- the original number of classes of skin deseases;
- the cardinality of images belonging only to the 7 chosen classes listed above;
- the link from which is possible to download the original dataset.



| Dataset |  Original classes | Selected images cardinality | Download link |
|:-----|:-----:|-----:|-----:|
| HAM 10000 [[1]](#1) | 7 | 10.015 | https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/DBW86T |
| Consecutive biopsies for melanoma [[2]](#2)  |  21  |   1.116 | https://api.isic-archive.com/collections/216/ |
| MSK1 [[3]](#3)  | 17 |    1.380 | https://api.isic-archive.com/collections/289/ |
| MSK2 [[3]](#3)  | 22 |    4.374 | https://api.isic-archive.com/collections/290/ |
| MSK3 [[3]](#3)  | 25 |    434 | https://api.isic-archive.com/collections/288/ |
| MSK4 [[3]](#3)  | 24 |    1.806 | https://api.isic-archive.com/collections/287/ |
| MSK5 [[3]](#3)  | 17 |    111 | https://api.isic-archive.com/collections/286/ |
| Hospital Italiano de Buenos Aires Dataset [[4]](#4)  | 10 |    1.616 | https://api.isic-archive.com/collections/251/ |
| SKINL2 [[5]](#5)  | 51 |    397 | https://www.it.pt/AutomaticPage?id=3459 |
| BCN20000 [[6]](#6)  | 8 |    233 | https://api.isic-archive.com/collections/249/ |
| UDA-1 [[3]](#3)  | 7 |    555 | https://api.isic-archive.com/collections/292/ |
| UDA-2 [[3]](#3)  | 7 |    60 | https://api.isic-archive.com/collections/291/ |
| 7-point criteria evaluation (dermatoscopic) [[7]](#7)  | 20 |    963 | https://derm.cs.sfu.ca/Welcome.html |
| ISIC 2020 Challenge Training Set [[8]](#8)  | 8 |    5.949 | https://challenge.isic-archive.com/data/#2020 |
| ISIC Challenge 2018: Task 1-2 Test [[9]](#9)  | 3 |    539 | https://challenge.isic-archive.com/data/#2018 |
| ISIC Challenge 2018: Task 1-2 Validation [[9]](#9)  | 3 |    47 | https://challenge.isic-archive.com/data/#2018 |
| PH2 [[10]](#10)  | 3 |    200 | https://www.fc.up.pt/addi/ph2%20database.html |
| **Total of selected images** |   | **41.975** |


## References

<a id="1">[1]</a>
Tschandl, Philipp, Cliff Rosendahl, and Harald Kittler. "The HAM10000 dataset, a large collection of multi-source dermatoscopic images of common pigmented skin lesions." Scientific data 5.1 (2018): 1-9.

<a id="2">[2]</a>
Consecutive biopsies for melanoma across year 2020, https://doi.org/10.34970/151324

<a id="3">[3]</a>
International Skin Imaging Collaborations. ISIC Archive, https://www.isic-archive.com

<a id="4">[4]</a>
Ricci Lara, María Agustina, et al. "A dataset of skin lesion images collected in Argentina for the evaluation of AI tools in this population." Scientific Data 10.1 (2023): 712.

<a id="5">[5]</a>
S. M. M. de Faria et al., "Light Field Image Dataset of Skin Lesions," 2019 41st Annual International Conference of the IEEE Engineering in Medicine and Biology Society (EMBC), Berlin, Germany, 2019, pp. 3905-3908. DOI: 10.1109/EMBC.2019.8856578

<a id="6">[6]</a>
Combalia, Marc, et al. "Bcn20000: Dermoscopic lesions in the wild." arXiv preprint arXiv:1908.02288 (2019).

<a id="7">[7]</a>
7-Point Checklist and Skin Lesion Classification using Multi-Task Multi-Modal Neural Nets.
Jeremy Kawahara, Sara Daneshvar, Giuseppe Argenziano, and Ghassan Hamarneh
IEEE Journal of Biomedical and Health Informatics (IEEE JBHI) special issue on Skin Lesion Image Analysis for Melanoma Detection DOI: 10.1109/JBHI.2018.2824327

<a id="8">[8]</a>
Rotemberg, Veronica, et al. "A patient-centric dataset of images and metadata for identifying melanomas using clinical context." Scientific data 8.1 (2021): 34.

<a id="9">[9]</a>
Codella, Noel CF, et al. "Skin lesion analysis toward melanoma detection: A challenge at the 2017 international symposium on biomedical imaging (isbi), hosted by the international skin imaging collaboration (isic)." 2018 IEEE 15th international symposium on biomedical imaging (ISBI 2018). IEEE, 2018.

<a id="10">[10]</a>
Teresa Mendonça, Pedro M. Ferreira, Jorge Marques, Andre R. S. Marcal, Jorge Rozeira. PH² - A dermoscopic image database for research and benchmarking, 35th International Conference of the IEEE Engineering in Medicine and Biology Society, July 3-7, 2013, Osaka, Japan.
