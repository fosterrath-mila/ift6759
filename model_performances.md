# Block 1 Performances
## Horoma
The baseline on the new dataset for block 1 was run with the following command. `python -u baseline.py data -k 50 -p`.

Valid Accuracy | Test Accuracy | Valid F1 | Test F1
--- | --- | --- | ---
36.91% | 28.31% | 33.89% | 25.35

Due to the issue with the dataset, the following scores table is not accurate anymore.

Team | Test Accuracy
--- | ---
baseline | 46.91%
b1phot1 | 46.07%
b1phot2 | 54.39%
b1phot3 | 54.37%
b1phot4 | 50.50%
b1phot5 | 57.86%

_Note: The differences between all results are statistically significant to each other._


## Humanware
Team | Test Accuracy | Statistically equivalent to baseline
--- | --- | ---
baseline | 96.7% |
b1phut1 | 8.5% | No
b1phut2 | 96.3% | Yes
b1phut3 | 97.2% | Yes
b1phut4 | 95.1% | No
b1phut5 | 96.6% | Yes


## OMSignal
Team | PR_Mean | RT_Mean | RR_Std | User_ID | Statistically equivalent to baseline
--- | --- | --- | --- | --- | ---
baseline | 65.99% | 76.33% | 18.25% | 27.74% |
b1pomt1 | 1.34% |11.02% | 4.17% | 36.77% | - - - 1
b1pomt2 | 91.09% |87.34% | 65.33% | 80.64% | 2 2 2 2
b1pomt3 | 3.60% |39.36% | 16.68% | 4.51%|- - 1 -
b1pomt4 | 55.82% | 76.21% | 23.79% | 36.13% | - 1 2 1
b1phom5 | 16.21% | 58.06% | 74.67% | 53.55% | - - 2 2

_Note: `-` = inferior to the baseline, `1` = equivalent to the baseline, `2` = superior to the baseline_
