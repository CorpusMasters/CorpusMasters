# Results

## Method: XGBoost 

### TRAIN = [Train-1 + Train-2 + Train-3 + Train-4]

| Test Set | Accuracy | Precision | Recall | F1-score |
| -------- | -------- | --------- | ------ | -------- | 
| Test 1   | 0.6266   | 0.6330    | 0.6266 | 0.5893   |
| Test 2   | 0.5400   | 0.5892    | 0.5400 | 0.5233   |
| Test 3   | 0.7098   | 0.6784    | 0.7098 | 0.6750   |
| Test 4   | 0.7065   | 0.6982    | 0.7065 | 0.6896   |

#### Confusion matrices
##### Test 1
```text
[[  0   0   0   2]
 [  0  30   3  18]
 [  3  37  15  51]
 [  2  21   9 200]]
```
#### Test 2
```text
[[  0  13   1  11   0]
 [  3 218  17 132   0]
 [  0  40  16  58   0]
 [  2  14   2 116   1]
 [  1   3   0   1   1]]
```
#### Test 3
```text
[[  2   5   0   8   1]
 [  3  81   5  61   0]
 [  0  16  10  46   0]
 [  3  23   5 340   0]
 [  0   0   0   1   0]]
```
#### Test 4
```text
[[  0   2   0   1   0]
 [  1  50   6  36   0]
 [  0   2  10  16   0]
 [  0  10   6 135   0]
 [  0   1   0   0   0]]
```

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
