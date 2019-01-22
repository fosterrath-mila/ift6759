The data can be find on Helios at `/rap/jvb-000-aa/COURS2019/etudiants/data/horoma`.

We ask for the project that you only use the data provided by Mila as we will keep the test set blind.
The data consits of pixel patches that we extracted from 3 different images. We have formatted the original data so that it can easily be imported in Python.
A shared disk contains the available training and validation sets.

# Pixel patches
32 x 32 pixel patches were extracted from labeled image subsections.

Inputs: each pixel in a 32 x 32 pixel patch has 4 dimensions:
- RGB colors in [0, 255] (3 values).
- Relative height originally defined as the tree height w.r.t. the sea level, where we subtracted from it the smallest pixel tree height within the 1024 pixels of the 32 x 32 pixel patch.

Outputs: each 32 x 32 pixel patch has 3 labels:
- Tree specie.
- Tree density.
- Tree height w.r.t. the forest floor.

A 32 x 32 pixel patch always contains trees of the same specie, density and height.

# Datasets
Each pixel patch has a shape of 32 x 32 x 4 (where 4 = [R, G, B, relative height]).

## Training set
__train_x.dat__: Float32 binary file containing 1,614,216 pixel patches. Can be converted into a 1,614,214 x 32 x 32 x 4 numpy array. It is recommended to use numpy.memmap for accessing small segments of a large file on disk without reading the entire file into memory.

## Validation set
__valid_x.dat__: Float32 binary file containing 201,778 pixel patches. Can be converted into a 201,778 x 32 x 32 x 4 numpy array.
__valid_y.txt__: Text file containing the labels of the 201,778 pixel patches. Can be used to evaluate models.
definition_labels.txt: text file containing a list of triples.
- 1st value: tree specie (2 characters).
- 2nd value: tree density (percentage*100 rounded at lowest unit of 5).
- 3rd value: tree height w.r.t. the forest floor (rounded at nearest 5m).
- The discrete value of each label in valid_y.txt is mapped to the triple corresponding to the row index (starting at 1) in definition_labels.txt that is equal to the value of the label.
- e.g. if label = 4 then triple = (TO,55,15) (4th row in definition_labels.txt).

Find clever ways to exploit the information that is given to you to determine the number of clusters.
