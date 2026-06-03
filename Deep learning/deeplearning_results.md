# Sentiment Analysis Results
Grupa 1 GRU:
Accuracy: 0.5123152709359606
              precision    recall  f1-score   support

           0       0.47      0.27      0.34       150
           1       0.19      0.65      0.29        72
           2       0.82      0.61      0.70       371
           3       0.00      0.00      0.00        16

    accuracy                           0.51       609
   macro avg       0.37      0.38      0.33       609
weighted avg       0.64      0.51      0.54       609

[[ 40  80  30   0]
 [ 11  47  14   0]
 [ 30 115 225   1]
 [  4   8   4   0]]

LSTM:
Accuracy: 0.5254515599343186
              precision    recall  f1-score   support

           0       0.67      0.17      0.28       150
           1       0.17      0.64      0.27        72
           2       0.83      0.67      0.74       371
           3       0.00      0.00      0.00        16

    accuracy                           0.53       609
   macro avg       0.42      0.37      0.32       609
weighted avg       0.69      0.53      0.55       609

[[ 26  99  25   0]
 [  4  46  22   0]
 [  9 114 248   0]
 [  0  11   5   0]]
_________________________________________________________

GRUPA 2: GRU:
Accuracy: 0.5652173913043478
              precision    recall  f1-score   support

           0       0.24      0.39      0.30        51
           1       0.43      0.45      0.44       106
           2       0.77      0.66      0.71       232
           3       0.00      0.00      0.00         2

    accuracy                           0.57       391
   macro avg       0.36      0.38      0.36       391
weighted avg       0.61      0.57      0.58       391

[[ 20  14  17   0]
 [ 31  48  27   0]
 [ 31  48 153   0]
 [  0   1   1   0]]

LSTM:
Accuracy: 0.5626598465473146
              precision    recall  f1-score   support

           0       0.37      0.25      0.30        51
           1       0.42      0.87      0.56       106
           2       0.86      0.50      0.63       232
           3       0.00      0.00      0.00         2

    accuracy                           0.56       391
   macro avg       0.41      0.40      0.37       391
weighted avg       0.67      0.56      0.57       391

[[ 13  26  11   1]
 [  6  92   7   1]
 [ 16 101 115   0]
 [  0   1   1   0]]
________________________________________________________

GRUPA 3: GRU:
Accuracy: 0.5090311986863711
              precision    recall  f1-score   support

           0       0.49      0.20      0.28       150
           1       0.17      0.61      0.27        72
           2       0.80      0.64      0.71       371
           3       0.00      0.00      0.00        16

    accuracy                           0.51       609
   macro avg       0.37      0.36      0.32       609
weighted avg       0.63      0.51      0.53       609

[[ 30  85  35   0]
 [  8  44  20   0]
 [ 21 114 236   0]
 [  2  11   3   0]]

LSTM:
Accuracy: 0.45977011494252873
              precision    recall  f1-score   support

           0       0.47      0.23      0.31       150
           1       0.18      0.79      0.29        72
           2       0.90      0.51      0.65       371
           3       0.00      0.00      0.00        16

    accuracy                           0.46       609
   macro avg       0.39      0.38      0.31       609
weighted avg       0.68      0.46      0.51       609

[[ 35 101  14   0]
 [ 11  57   4   0]
 [ 29 154 188   0]
 [  0  13   3   0]]
_________________________________________________________

GRUPA 4 (MI): GRU
Accuracy: 0.6086956521739131
              precision    recall  f1-score   support

           0       0.56      0.42      0.48        93
           1       0.40      0.07      0.12        28
           2       0.64      0.84      0.72       151
           3       0.00      0.00      0.00         3
           4       0.00      0.00      0.00         1

    accuracy                           0.61       276
   macro avg       0.32      0.27      0.26       276
weighted avg       0.58      0.61      0.57       276

[[ 39   2  52   0   0]
 [  8   2  18   0   0]
 [ 22   1 127   1   0]
 [  1   0   2   0   0]
 [  0   0   1   0   0]]

LSTM:
Accuracy: 0.6195652173913043
              precision    recall  f1-score   support

           0       0.55      0.51      0.53        93
           1       0.33      0.04      0.06        28
           2       0.65      0.81      0.73       151
           3       0.00      0.00      0.00         3
           4       0.00      0.00      0.00         1

    accuracy                           0.62       276
   macro avg       0.31      0.27      0.26       276
weighted avg       0.58      0.62      0.58       276

[[ 47   1  45   0   0]
 [ 10   1  17   0   0]
 [ 27   1 123   0   0]
 [  1   0   2   0   0]
 [  0   0   1   0   0]]

GRU/LSTM differences observed due to:
- different gating mechanism on the baseline of the Naive Bayes method
- better handling of dependencies in LSTM
- dataset is not balanced well with seldom sarcastic (1) and mixed (3) comments
# Conclusion

Both deep learning models outperform baseline ML model (Naive Bayes), showing benefit of contextual word representations and sequence modeling.
