# Sentiment Analysis Results

## Dataset
- 5 classes: negative, neutral, positive, mixed, sarcastic
- Train/Validation/Test split used

---

# LSTM Model Results

## Accuracy
0.0.605072463768116

## Classification Report
              precision    recall  f1-score   support

           0       0.55      0.42      0.48        93
           1       0.33      0.04      0.06        28
           2       0.63      0.84      0.72       151
           3       0.00      0.00      0.00         3
           4       0.00      0.00      0.00         1

    accuracy                           0.61       276
   macro avg       0.30      0.26      0.25       276
weighted avg       0.56      0.61      0.56       276

## Confusion Matrix
[[ 39   0  54   0   0]
 [  9   1  18   0   0]
 [ 21   2 127   1   0]
 [  2   0   1   0   0]
 [  0   0   1   0   0]]

---

# GRU Model Results

## Accuracy
0.19927536231884058

## Classification Report
Accuracy: 0.19927536231884058
              precision    recall  f1-score   support

           0       0.40      0.02      0.04        93
           1       0.07      0.04      0.05        28
           2       0.74      0.34      0.46       151
           3       0.01      0.33      0.01         3
           4       0.00      0.00      0.00         1

    accuracy                           0.20       276
   macro avg       0.24      0.15      0.11       276
weighted avg       0.55      0.20      0.27       276

## Confusion Matrix
[[ 2  4 13 64 10]
 [ 0  1  4 18  5]
 [ 2  9 51 63 26]
 [ 0  1  1  1  0]
 [ 1  0  0  0  0]]

---

# Comparison

- LSTM performed: 0.61
- GRU performed: 0.20
- Better model: LSTM

GRU/LSTM differences observed due to:
- different gating mechanism on the baseline of the Naive Bayes method
- better handling of dependencies in LSTM
- dataset is not balanced well with seldom sarcastic (1) and mixed (3) comments
# Conclusion

Both deep learning models outperform baseline ML model (Naive Bayes), showing benefit of contextual word representations and sequence modeling.
