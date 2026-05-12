# Results

## Method: XGBoost 

### TRAIN = [Train-1 + Train-2 + Train-3 + Train-4]

| Test Set | Accuracy | Precision | Recall | F1-score |
| -------- | -------- | --------- | ------ | -------- |
| Test 1   | 0.6266   | 0.6330    | 0.6266 | 0.5893   |
| Test 2   | 0.5400   | 0.5892    | 0.5400 | 0.5233   |
| Test 3   | 0.7098   | 0.6784    | 0.7098 | 0.6750   |
| Test 4   | 0.7065   | 0.6982    | 0.7065 | 0.6896   |

### Train-4

| Test Set | Accuracy | Precision | Recall | F1-score |
| -------- | -------- | --------- | ------ | -------- |
| Test 1   | 0.5934   | 0.5998    | 0.5934 | 0.5318   |
| Test 2   | 0.4431   | 0.5486    | 0.4431 | 0.4259   |
| Test 3   | 0.6738   | 0.6392    | 0.6738 | 0.6289   |
| Test 4   | 0.6812   | 0.6595    | 0.6812 | 0.6424   |

## Description

The XGBoost machine learning tool achieved better performance when trained on the combined training dataset from all groups (TRAIN) compared to using only our group's training set (Train-4). This demonstrates that increasing the amount and diversity of training data improves the model’s performance and precision.

Performance differences between test sets may be related to differences in annotation style and linguistic characteristics across datasets created by different groups.

Test set 2 got the lowest results in both cases, while Test sets 3 and 4 got the best results.
