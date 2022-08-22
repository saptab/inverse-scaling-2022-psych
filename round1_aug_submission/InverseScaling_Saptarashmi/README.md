# Data Creation by Saptarashmi

## 8/21 goal completed

data_creation.py script can be rerun to replicate the automatically created datasets with prompts at the front and the back of the question for original answers and binarized answers. The following 4 commands can be run for the 4 datasets, namely CFCS, HBDS, SD3 and HSNS+DD, prepared in this repository

```bashs
$ python3 data_creation.py CFCS/manual.csv cfcs CFCS/final.csv
$ python3 data_creation.py HBDS-data/manual.csv hbds HBDS-data/final.csv
$ python3 data_creation.py HSNS+DD/manual.csv hsns+dd HSNS+DD/final.csv
$ python3 data_creation.py SD3/manual.csv sd3 SD3/final.csv
```





