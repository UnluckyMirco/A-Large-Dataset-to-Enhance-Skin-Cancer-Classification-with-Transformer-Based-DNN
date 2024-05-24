# A-Large-Dataset-to-Enhance-Skin-Cancer-Classification-with-Transformer-Based-Deep-Neural-Networks
This repository contains the notebooks of the three best results presented in the paper and a read.me file that presents the construction of the Large Dataset proposed in the paper. For each dataset considered, a short explanation and references are presented. 


## Used Datasets

| Dataset |  Original classes | Final images[^1] | Download link |
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



[^1]: Cardinality of images belonging only to the 7 chosen classes listed above.
