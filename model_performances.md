# Block 2 Performances
## Horoma
Valid Accuracy | Test Accuracy | Test F1
--- | --- | --- 
baseline | 29.12% | 28.02%
b2phot1 | 40.36% | 35.55%
b2phot2 | 33.53% | 24.86%
b2phot3 | 27.31% | 19.61%
b2phot4 | 32.13% | 29.08%
b2phot5 | 31.12% | 21.38%

_Note: The differences between all results are statistically significant to each other._

## Humanware
Team | Test Accuracy | Statistically equivalent to baseline
--- | --- | ---
baseline | 92.3% | |
b2phut1 | 90.6% | - |
b2phut2 | 94.1% | 2 |
b2phut3 | 94.1% | 2 |
b2phut4 | 93.9% | 2 |
b2phut5 | 94.8% | 2 |


## OMSignal
Team | PR_Mean | RT_Mean | RR_Std | User_ID | Statistically equivalent to baseline
--- | --- | --- | --- | --- | ---
baseline | 65.99% | 81.00% | 67.34% | 51.31% |
b2pomt1 | 79.72% |81.18% | 25.77% | 13.55% | 2 1 - -
b2pomt2 | 65.99% |74.89% | 20.46% | 49.03% | 1 - - 1
b2pomt3 | 69.43% |83.90% | 73.14% | 80.64%| 2 2 2 2
b2pomt4 | 93.25% | 87.19% | 83.05% | 74.84% | 2 1 2 2
b2pomt5 | 75.22% | 79.12% | 3.82% | 30.97% | 2 2 - -

_Note: `-` = inferior to the baseline, `1` = equivalent to the baseline, `2` = superior to the baseline_


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
b1pomt1 | 6.62% |8.85% | 6.90% | 49.03% | - - - 2
b1pomt2 | 93.25% |87.19% | 83.05% | 80.64% | 2 2 2 2
b1pomt3 | 11.70% |51.93% | 21.68% | 10.97%|- - 2 -
b1pomt4 | 57.86% | 76.32% | 29.62% | 47.74% | - 1 2 2
b1pomt5 | 16.21% | 58.06% | 74.67% | 53.55% | - - 2 2

_Note: `-` = inferior to the baseline, `1` = equivalent to the baseline, `2` = superior to the baseline_
