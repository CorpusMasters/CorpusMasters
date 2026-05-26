# Results

### Method: XGBoost 

## TRAIN = [Train-1 + Train-2 + Train-3 + Train-4]

#### TEST 1

| Metric | Value |
|---|---|
| Accuracy | 0.6266 |
| Precision | 0.6330 |
| Recall | 0.6266 |
| F1-score | 0.5893 |

#### Confusion Matrix

```text
[[  0   0   0   2]
 [  0  30   3  18]
 [  3  37  15  51]
 [  2  21   9 200]]
```

---

#### TEST 2

| Metric | Value |
|---|---|
| Accuracy | 0.5400 |
| Precision | 0.5892 |
| Recall | 0.5400 |
| F1-score | 0.5233 |

#### Confusion Matrix

```text
[[  0  13   1  11   0]
 [  3 218  17 132   0]
 [  0  40  16  58   0]
 [  2  14   2 116   1]
 [  1   3   0   1   1]]
```

---

#### TEST 3

| Metric | Value |
|---|---|
| Accuracy | 0.7098 |
| Precision | 0.6784 |
| Recall | 0.7098 |
| F1-score | 0.6750 |

#### Confusion Matrix

```text
[[  2   5   0   8   1]
 [  3  81   5  61   0]
 [  0  16  10  46   0]
 [  3  23   5 340   0]
 [  0   0   0   1   0]]
```

---

#### TEST 4

| Metric | Value |
|---|---|
| Accuracy | 0.7065 |
| Precision | 0.6982 |
| Recall | 0.7065 |
| F1-score | 0.6896 |

#### Confusion Matrix

```text
[[  0   2   0   1   0]
 [  1  50   6  36   0]
 [  0   2  10  16   0]
 [  0  10   6 135   0]
 [  0   1   0   0   0]]
```

## Train-4

#### TEST 1

| Metric | Value |
|---|---|
| Accuracy | 0.5934 |
| Precision | 0.5998 |
| Recall | 0.5934 |
| F1-score | 0.5318 |

#### Confusion Matrix

```text
[[  0   0   0   2   0]
 [  1  22   2  25   1]
 [  3  27   7  69   0]
 [  1  25   3 203   0]
 [  0   0   0   0   0]]
```

---

#### TEST 2

| Metric | Value |
|---|---|
| Accuracy | 0.4431 |
| Precision | 0.5486 |
| Recall | 0.4431 |
| F1-score | 0.4259 |

#### Confusion Matrix

```text
[[  0   7   1  17   0]
 [  2 161  12 195   0]
 [  0  33   9  72   0]
 [  1  14   2 118   0]
 [  1   2   0   3   0]]
```

---

#### TEST 3

| Metric | Value |
|---|---|
| Accuracy | 0.6738 |
| Precision | 0.6392 |
| Recall | 0.6738 |
| F1-score | 0.6289 |

#### Confusion Matrix

```text
[[  1   6   0   9   0]
 [  2  75   2  71   0]
 [  0  18   4  50   0]
 [  7  31   2 331   0]
 [  0   0   0   1   0]]
```

---

#### TEST 4

| Metric | Value |
|---|---|
| Accuracy | 0.6812 |
| Precision | 0.6595 |
| Recall | 0.6812 |
| F1-score | 0.6424 |

#### Confusion Matrix

```text
[[  0   0   1   2   0]
 [  0  48   0  45   0]
 [  0   7   2  19   0]
 [  2   9   2 138   0]
 [  0   1   0   0   0]]
```
## Description

The XGBoost machine learning tool achieved better performance when trained on the combined training dataset from all groups (TRAIN) compared to using only our group's training set (Train-4). This demonstrates that increasing the amount and diversity of training data improves the model’s performance and precision.

Performance differences between test sets may be related to differences in annotation style and linguistic characteristics across datasets created by different groups.

Test set 2 got the lowest results in both cases, while Test sets 3 and 4 got the best results.
