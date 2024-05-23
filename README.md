# A-Large-Dataset-to-Enhance-Skin-Cancer-Classification-with-Transformer-Based-Deep-Neural-Networks
This repository contains the notebooks of the three best results presented in the paper and a read.me file that presents the construction of the Large Dataset proposed in the paper. For each dataset considered, a short explanation and references are presented. 


## Used Datasets

| Dataset |  Original classes | Final images[^1] | Download link |
|:-----|:-----:|-----:|-----:|
| HAM 10000 [[1]](#1) | 7 | 10.015 | https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/DBW86T |
| Consecutive biopsies for melanoma [[2]](#2)  |  21  |   1.116 | https://api.isic-archive.com/collections/216/ |
| MSK1 [[3]](#3)  | 17 |    1.380 | https://api.isic-archive.com/collections/289/ |
| MSK2 [[4]](#4)  | 22 |    4.374 | https://api.isic-archive.com/collections/290/ |
| MSK3 [[5]](#5)  | 25 |    434 | https://api.isic-archive.com/collections/288/ |
| MSK4 [[6]](#6)  | 24 |    1.806 | https://api.isic-archive.com/collections/287/ |
| MSK5 [[7]](#7)  | 17 |    111 | https://api.isic-archive.com/collections/286/ |
| Hospital Italiano de Buenos Aires Dataset [[8]](#8)  | 10 |    1.616 | https://api.isic-archive.com/collections/251/ |
| SKINL2 [[9]](#9)  | 51 |    397 | https://www.it.pt/AutomaticPage?id=3459 |
| BCN20000 [[10]](#10)  | 8 |    233 | https://api.isic-archive.com/collections/249/ |
| UDA-1 [[11]](#11)  | 7 |    555 | https://api.isic-archive.com/collections/292/ |
| UDA-2 [[12]](#12)  | 7 |    60 | https://api.isic-archive.com/collections/291/ |
| 7-point criteria evaluation (dermatoscopic) [[13]](#13)  | 20 |    963 | https://derm.cs.sfu.ca/Welcome.html |
| ISIC 2020 Challenge Training Set [[14]](#14)  | 8 |    5.949 | https://challenge.isic-archive.com/data/#2020 |
| ISIC Challenge 2018: Task 1-2 Test [[15]](#15)  | 3 |    539 | https://challenge.isic-archive.com/data/#2018 |
| ISIC Challenge 2018: Task 1-2 Validation [[16]](#16)  | 3 |    47 | https://challenge.isic-archive.com/data/#2018 |
| PH2 [[17]](#17)  | 3 |    200 | https://www.fc.up.pt/addi/ph2%20database.html |


## References

<a id="1">[1]</a>
Tschandl, Philipp, Cliff Rosendahl, and Harald Kittler. "The HAM10000 dataset, a large collection of multi-source dermatoscopic images of common pigmented skin lesions." Scientific data 5.1 (2018): 1-9.

<a id="2">[2]</a>
Consecutive biopsies for melanoma across year 2020, https://doi.org/10.34970/151324

<a id="9">[9]</a>
S. M. M. de Faria et al., "Light Field Image Dataset of Skin Lesions," 2019 41st Annual International Conference of the IEEE Engineering in Medicine and Biology Society (EMBC), Berlin, Germany, 2019, pp. 3905-3908. DOI: 10.1109/EMBC.2019.8856578

<a id="13">[13]</a>
7-Point Checklist and Skin Lesion Classification using Multi-Task Multi-Modal Neural Nets.
Jeremy Kawahara, Sara Daneshvar, Giuseppe Argenziano, and Ghassan Hamarneh
IEEE Journal of Biomedical and Health Informatics (IEEE JBHI) special issue on Skin Lesion Image Analysis for Melanoma Detection DOI: 10.1109/JBHI.2018.2824327

<a id="17">[17]</a>
Teresa Mendonça, Pedro M. Ferreira, Jorge Marques, Andre R. S. Marcal, Jorge Rozeira. PH² - A dermoscopic image database for research and benchmarking, 35th International Conference of the IEEE Engineering in Medicine and Biology Society, July 3-7, 2013, Osaka, Japan.



[^1]: Cardinality of images belonging only to the 7 chosen classes listed above.
